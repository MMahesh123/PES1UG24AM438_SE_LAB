# Lab 7 — Fuzz Testing for Input Validation Bugs

Application: `marathon_registration_parser.py`

Hypothesis test module: `test_marathon_registration_parser.py`

Original buggy implementation preserved as: `marathon_registration_parser_original.py`.

## Setup

From the repository root:

```powershell
python -m pip install hypothesis pytest
cd lab07
```

## Screenshot sequence

### SS1 — Original application

Run:

```powershell
python marathon_registration_parser_original.py
```

Sample inputs: `Mahesh Kumar`, `3:45:10`, and `25 26 24`.

Observed output: bib name `M MAHESH`, finish time `13510` seconds, average split `25.0` minutes.

### SS2 — Hypothesis failures on original implementation

The test module imports `marathon_registration_parser`. Temporarily swap in the original implementation:

```powershell
Copy-Item marathon_registration_parser.py marathon_registration_parser_fixed_backup.py
Copy-Item marathon_registration_parser_original.py marathon_registration_parser.py -Force
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
python -m pytest test_marathon_registration_parser.py -v
```

Verified result: **3 failed, 3 passed**. Hypothesis exposed unexpected-input failures in all three functions: `format_bib_name`, `parse_finish_time`, and `average_split`.

### SS3 — Fixed application

Restore the fixed implementation:

```powershell
Copy-Item marathon_registration_parser_fixed_backup.py marathon_registration_parser.py -Force
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
python marathon_registration_parser.py
```

Using the same sample inputs, the fixed application produces the expected valid-input output.

### SS4 — Passing tests

```powershell
python -m pytest test_marathon_registration_parser.py -v
```

Verified result: **6 passed**.

## Fixed input behaviour

- `format_bib_name`: uppercase, trim and limit a valid string to 12 characters; invalid types return an empty string.
- `parse_finish_time`: convert valid H:MM:SS to seconds; invalid values return `None`.
- `average_split`: average non-negative integer split values; invalid or empty input returns `None`.

## Submission

The Lab 7 handout requests a PDF containing the four screenshots, plus the fixed application and updated test file. The fixed application, original implementation, and Hypothesis tests are included in this folder. Remove the temporary `marathon_registration_parser_fixed_backup.py` after testing; do not commit it.
