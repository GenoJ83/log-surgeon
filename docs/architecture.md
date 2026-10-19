# Architecture

```mermaid
flowchart LR
    Input[Log Stream] --> Parser[Regex/JSON Parser]
    Parser --> Filter[Query Filter]
    Filter --> Format[CSV/JSON/HTML]
    Format --> Output[Console/File]
```
