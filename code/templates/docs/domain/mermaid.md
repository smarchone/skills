# System Port Diagram

> Conventions: `mermaid-diagram.md` in the `hex-domain` skill.

```mermaid
%%{init: {"layout": "elk", "elk": {"mergeEdges": true}}}%%
flowchart LR

    subgraph DomainX [" "]
        X_Core{{"<DomainX> Domain<br/>──────────────<br/>• <Aggregate><br/>• <ValueObject>"}}
        Xin1(["<UseCase>()"])
        Xin2(["<DomainX>For<DomainO>"])
        Xout1(["<OutboundPort>"])
        Xin1 & Xin2 --> X_Core
        X_Core --> Xout1
    end

    subgraph DomainO [" "]
        O_Core{{"<DomainO> Domain<br/>──────────────<br/>• <Aggregate><br/>• <ValueObject>"}}
        Oin1(["<UseCase>()"])
        Oin2(["<DomainO>For<DomainX>"])
        Oout1(["<OutboundPort>"])
        Oin1 & Oin2 --> O_Core
        O_Core --> Oout1
    end

    %% one thick edge per bridge: caller's outbound port ==> callee's inbound port
    Xout1 == "synchronous bridge call" ==> Oin2

    classDef default fill:#f8fafc,stroke:#cbd5e1,color:#334155;
    style DomainX fill:none,stroke:none;
    style DomainO fill:none,stroke:none;
    classDef inPort fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0c4a6e;
    classDef outPort fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12;
    class Xin1,Xin2,Oin1,Oin2 inPort;
    class Xout1,Oout1 outPort;
    style X_Core fill:#f0fdfa,stroke:#0d9488,stroke-width:3px,color:#115e59
    style O_Core fill:#eef2ff,stroke:#4f46e5,stroke-width:3px,color:#312e81
```

## Domains in this diagram
| Domain | Id prefix | Core hue | Sketch |
|---|---|---|---|
| <DomainX> | `X` | teal | `<domainx>.md` |
| <DomainO> | `O` | indigo | `<domaino>.md` |

## Bridges
| From (outbound port) | To (inbound port) | Purpose |
|---|---|---|
| `<DomainX>.<OutboundPort>` | `<DomainO>.<DomainO>For<DomainX>` | <one line> |
