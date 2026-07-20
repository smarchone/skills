# Go file layout — `internal/<domain>/`

Five files per domain. Nothing else belongs here.

| File | Holds |
|---|---|
| `model.go` | aggregate, value objects, invariants, errors |
| `ports.go` | interfaces this domain declares |
| `service.go` | use cases: orchestration, cross-aggregate and policy rules |
| `model_test.go` | one case per invariant — no mocks |
| `service_test.go` | use-case flows with fake ports |

## `model.go`

```go
package <domain>

import "errors"

// --- value objects ---
type <ValueObject> struct {
	// unexported fields when an invariant must hold on construction
}

func New<ValueObject>(<args>) (<ValueObject>, error)

// --- enums, prefixed to avoid collisions within the package ---
type <Type><Concept> string

const (
	<Type><Concept><Value> <Type><Concept> = "<value>"
)

// --- aggregate root ---
type <Aggregate> struct {
	// unexported: invariants cannot be enforced on fields callers can set
}

func New<Aggregate>(<args>) (*<Aggregate>, error)

// --- domain methods: state transitions named for the canonical verb ---
func (a *<Aggregate>) <Verb>(<args>) error

// --- errors: one per invariant, names matching the spec exactly ---
var (
	Err<Condition> = errors.New("<domain>: <condition in canonical terms>")
)
```

## `ports.go`

```go
package <domain>

import "context"

// --- INBOUND: driving (invoked by transport adapters) ---
type <Domain>Service interface {
	<UseCase>(ctx context.Context, <args>) (<Result>, error)
}

// --- INBOUND: driven by siblings (invoked through a bridge) ---
type <Domain>For<SiblingDomain> interface {
	<SiblingFacingOperation>(ctx context.Context, <args>) (<Result>, error)
}

// --- OUTBOUND: driven (persistence, publishing, sibling calls) ---
type <Aggregate>Repository interface {
	Load(ctx context.Context, id <IDType>) (*<Aggregate>, error)
	Save(ctx context.Context, a *<Aggregate>) error
}
```

Keep the three headings and their order — a reader should be able to tell a port's role without tracing who implements it.

## `service.go`

Implements the inbound driving port. Holds outbound ports as dependencies — never concrete types.

The shape of a use case is: load, call the aggregate, persist, publish. Rules the aggregate can't check itself belong here, before the domain call.

```go
package <domain>

import "context"

type service struct {
	repo <Aggregate>Repository
	// other outbound ports
}

// Returns the inbound port, not the struct — callers depend on the interface.
func NewService(repo <Aggregate>Repository) <Domain>Service {
	return &service{repo: repo}
}

func (s *service) <UseCase>(ctx context.Context, <args>) (<Result>, error) {
	a, err := s.repo.Load(ctx, id)
	if err != nil {
		return <Result>{}, err
	}

	// cross-aggregate and policy rules: everything needing data the aggregate doesn't own
	// e.g. count sibling aggregates, check caller permission, verify idempotency

	if err := a.<Verb>(<args>); err != nil { // invariants enforced inside
		return <Result>{}, err
	}

	if err := s.repo.Save(ctx, a); err != nil {
		return <Result>{}, err
	}
	return <Result>{}, nil
}
```

Keep decisions about the aggregate's own state inside the aggregate. A service that starts reaching into fields to decide things is a domain going anaemic.

## `model_test.go`

One table test per invariant row in the spec. The spec's invariant table and this file should be checkable against each other by eye.

```go
package <domain>

import (
	"errors"
	"testing"
)

func Test<Aggregate>_<Verb>_Invariants(t *testing.T) {
	tests := []struct {
		name    string // the invariant, in the spec's own words
		setup   func() *<Aggregate>
		wantErr error  // the Err… value the spec names, or nil
	}{
		{
			name:    "<a Noun must always ...>",
			setup:   func() *<Aggregate> { /* state that violates it */ },
			wantErr: Err<Condition>,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := tt.setup().<Verb>()
			if !errors.Is(err, tt.wantErr) {
				t.Fatalf("got %v, want %v", err, tt.wantErr)
			}
		})
	}
}
```

Use the invariant's wording from the spec as the test name. When a test fails, the failure output then states the business rule that broke, not just a symbol.

## `service_test.go`

Use-case flows, with in-memory fakes for the outbound ports. What's worth testing here is what `model_test.go` cannot reach: the cross-aggregate and policy rules, and the orchestration itself — that a failed domain call doesn't persist, that a successful one does.

```go
package <domain>

import (
	"context"
	"errors"
	"testing"
)

type fake<Aggregate>Repo struct {
	items map[<IDType>]*<Aggregate>
	saved bool
}

func (f *fake<Aggregate>Repo) Load(ctx context.Context, id <IDType>) (*<Aggregate>, error) {
	a, ok := f.items[id]
	if !ok {
		return nil, Err<NotFound>
	}
	return a, nil
}

func (f *fake<Aggregate>Repo) Save(ctx context.Context, a *<Aggregate>) error {
	f.saved = true
	f.items[a.ID()] = a
	return nil
}

func Test<UseCase>(t *testing.T) {
	t.Run("<the cross-aggregate rule, in the spec's words>", func(t *testing.T) {
		repo := &fake<Aggregate>Repo{items: /* state that violates the rule */}
		err := NewService(repo).<UseCase>(context.Background(), <args>)

		if !errors.Is(err, Err<Condition>) {
			t.Fatalf("got %v, want %v", err, Err<Condition>)
		}
		if repo.saved {
			t.Fatal("rejected use case must not persist")
		}
	})
}
```

Don't retest invariants here — they're covered in `model_test.go` without mocks, and duplicating them just makes the fakes carry weight they shouldn't.
