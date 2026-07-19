# Shared mermaid port diagram — conventions

The diagram is **one system-wide asset** at `docs/mermaid.md`. Every `domain-spec` run **amends it in
place**: add or refresh this domain's subgraph and any bridge edges. Never produce a per-domain copy.

## Model to diagram mapping

| Model-sketch artifact | Diagram element |
|---|---|
| Bounded context | a `subgraph` |
| Aggregate root + value objects | the hexagon core `{{...}}` |
| `INBOUND: driving` port | inbound stadium node → core |
| `INBOUND: sibling` port | separate inbound stadium node → core |
| `OUTBOUND` port | outbound stadium node, core → node |
| Cross-domain **bridge** | thick edge: caller's outbound port `==>` callee's inbound port |

## Shape & palette template

```mermaid
%%{init: {"layout": "elk", "elk": {"mergeEdges": true}}}%%
flowchart LR

    subgraph Domain [" "]
        X_Core{{"<Domain> Domain<br/>──────────────<br/>• <Aggregate><br/>• <ValueObject>"}}
        Xin1(["<UseCase>()"])
        Xin2(["<SiblingFacingPort>"])
        Xout1(["<OutboundPort>"])
        Xin1 & Xin2 --> X_Core
        X_Core --> Xout1
    end

    %% thick edge per bridge
    Xout1 == "synchronous bridge call" ==> Siblingin2

    classDef default fill:#f8fafc,stroke:#cbd5e1,color:#334155;
    style Domain fill:none,stroke:none;
    classDef inPort fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0c4a6e;
    classDef outPort fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12;
    class Xin1,Xin2 inPort;
    class Xout1 outPort;
    style X_Core fill:#f0fdfa,stroke:#0d9488,stroke-width:3px,color:#115e59
```

- Each domain core (`X_Core`) should use a distinct hue (teal / indigo / amber, etc.) so domains read apart visually.
- Prefix ids per domain (e.g. `X`/`O`/`A`) so they never collide.
