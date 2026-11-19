# Lab 7 — Fuzz Testing for Input Validation Bugs

Application: `marathon_registration_parser.py`

Hypothesis test module: `test_marathon_registration_parser.py`

Original buggy implementation preserved as: `marathon_registration_parser_original.py`.

## Setup

From the repository root:

```powershell
py -m pip install hypothesis pytest
cd lab07
```

## Screenshot sequence

Capture the four screenshots from real terminal runs in this order.

### SS1 — Run the original application

For valid sample inputs, run the original application using valid sample inputs. If needed, execute the original file directly after renaming/copying it to the expected application name.

### SS2 — Show Hypothesis finding failures

The test module imports `marathon_registration_parser`. Temporarily swap the original implementation into that filename:

```powershell
Copy-Item marathon_registration_parser.py marathon_registration_parser_fixed_backup.py
Copy-Item marathon_registration_parser_original.py marathon_registration_parser.py -Force
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
py -m pytest test_marathon_registration_parser.py -v
```

Capture the failing Hypothesis output. These failures are expected against the original implementation.

### SS3 — Run the fixed application

Restore the fixed implementation:

```powershell
Copy-Item marathon_registration_parser_fixed_backup.py marathon_registration_parser.py -Force
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
py marathon_registration_parser.py
```

Use sample inputs such as `Mahesh Kumar`, `3:45:10`, and `25 26 24`. Capture the output.

### SS4 — Show all tests passing

```powershell
py -m pytest test_marathon_registration_parser.py -v
```

Capture the passing output.

## Fixed input behaviour

- `format_bib_name`: uppercase, trim and limit a valid string to 12 characters; invalid types return an empty string.
- `parse_finish_time`: convert valid H:MM:SS to seconds; invalid values return `None`.
- `average_split`: average non-negative integer split values; invalid or empty input returns `None`.

## PDF submission

Create `PES1UG24AM438_MAHESH_LAB7.pdf` containing SS1–SS4 and the reflection answers requested by your instructor/handout. Also submit the fixed application and Hypothesis test file.

Do not claim a test passed or failed until the corresponding command has actually been run.
