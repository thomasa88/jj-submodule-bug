# Sample Project with Submodules

This is a small sample project created to demonstrate adding submodules.

Structure:
- src/: main project source
- _subrepos/submodule-a: first submodule repo
- _subrepos/submodule-b: second submodule repo

Greeting generator
------------------

This repository now includes a small greeting message generator with a CLI.

Example usage:

```bash
# From the repository root (uses the package import path)
python -m src.cli --name Alice --occasion birthday --tone friendly --seed 42
```

From Python:

```py
from src.greetings import GreetingGenerator
g = GreetingGenerator(seed=1)
print(g.generate_greeting(name="Eve", occasion="new year", tone="playful"))
```
