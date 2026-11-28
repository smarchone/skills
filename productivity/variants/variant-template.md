# variants/N-&lt;slug&gt;.md template

Keep each file to a single screen of reading. Every section needs a concrete example.

````
# Variant N · <short name>

> <one or two lines: the core idea, and what makes this variant different>

<one line: how it relates to the others ("Variant 1 + memory")>

## File structure
```
<tree with a short comment per entry>
```

## Storage
<the main stored object(s) as real example data (yaml/json/md) using the project's domain>
<one line on what is NOT stored, if that matters>

## Contract
<the one interface everything plugs into (function signature, or prompt paragraph), ≤20 lines>

## Pipeline
```
<ascii flow: inputs ─▶ steps ─▶ outputs>
```

## Compounding loop
<what builds up across runs and how it feeds back; an ascii loop and/or a sample command output>

## Example run
```
$ <command>
```
<the real-looking output the user would see>

## Feel
| good | bad |
|---|---|
| … | … |

**Pick it when** <one honest sentence>.
````

README.md shape:

````
# Variants · <project>

<one line: the shared pieces all variants have>

| | <axis 1> | <axis 2> | … | effort |
|---|---|---|---|---|
| [1 · name](1-name.md) | … | … | … | weekend |

## How they relate
```
1 ──add X──▶ 2 ──add Y──▶ 3
4 ── combines with 2 ──┘
```

## A likely path
<2-3 lines of recommendation, including hybrids>
````
