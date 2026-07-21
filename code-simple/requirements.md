we are trying to manage a project which is just accumulation of features (code changes).
we will follow hexagonal architecture with golang.

hexagonal golang codebase = domain + adapters + wiring
domain is the core.
- business usecases or state machine
- business type system and behaviour
- needs much thinking and modelling (concise domain modelling)
adapter is mechanical
- no/minimal business references
- coding models can generate code easily with little context.



create a simple skill that help create reviewable specs/artifacts to support the domain code generation.

- it must maintain and evolve a business language (ubiquitous language) to describe the domain(s). - `language.md`
- it must explain/refine the product and features in that language to be consistent. - `product.md` and `feature/<>.md`
    - product - description/vision/goal/out-of-scope - grounded by language.md
    - usecases, constraints, business processes etc.. - grounded by language.md
- it must create domain artifacts to help navigate the code level decisions  - `domain/<>.md`
    - domain type system - only the core important ones
    - port interfaces and service
    - any business statemachine
    - everything abiding by the language.md


workflow: 
- the user will be grilled to establish the feature and align with the product (if there is no product.md it must also be generated). 
- any implicit assumptions, or gaps, or blindspots, or failure modes must be explored and established in this session. 
- use this ƒeature spec to update the language and project specs
- then do the domain modelling

refer to the templates for specs in ../code/templates/docs/
they dont have to be exact, use your judgment to adopt for this workflow.






