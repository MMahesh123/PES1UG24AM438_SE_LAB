# Lab 5 — Static Code Analysis Issue Table

| Issue | Tool | Original Location | Description | Fix Applied |
|---|---|---|---|---|
| Missing module docstring | Pylint | Line 1 | Module purpose was undocumented. | Added module docstring. |
| Missing function docstrings | Pylint | Multiple lines | Functions lacked documentation. | Added docstrings to all functions. |
| Non-snake_case names | Pylint | Multiple lines | Function names did not follow Python naming conventions. | Renamed functions using snake_case. |
| Mutable default argument | Pylint | Line 9 | A default list could be shared across calls. | Used `None` and initialized the list inside the function. |
| SQL injection risk | Bandit | Line 10 | SQL was constructed using string interpolation. | Used parameterized SQL queries. |
| Unsafe deserialization | Bandit | Line 33 | `pickle.loads()` can execute malicious payloads. | Replaced pickle with JSON serialization. |
| Random generator warning | Bandit | Line 17 | `random.choice()` triggered a security warning. | Replaced it with `secrets.choice()`. |
| Bare exception | Pylint / Flake8 | Line 39 | Broad exception handling could hide unrelated errors. | Caught `sqlite3.Error`. |
| Long lines | Pylint / Flake8 | Multiple lines | Lines exceeded the configured length limits. | Reformatted long statements. |
| Multiple statements per line | Flake8 | Line 48 | Reduced readability. | Split statements onto separate lines. |
| Ambiguous variable name | Flake8 | Line 47 | Variable `l` was difficult to read. | Renamed it to `loaded_playlist`. |
| Unnecessary `else` | Pylint | Line 22 | An `else` followed a `return`. | Removed the unnecessary `else`. |

## Verification Results

- Pylint: 4.57/10 before; 10.00/10 after.
- Bandit: Four findings before; zero findings after.
- Flake8: Violations before; exit code 0 after.