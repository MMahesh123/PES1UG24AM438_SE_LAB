# Lab 7 — Fuzz Testing for Input Validation Bugs

Application: `marathon_registration_parser.py`

Hypothesis test module: `test_marathon_registration_parser.py`

## Setup

From this folder:

```powershell
py -m pip install hypothesis pytest
```

## Required evidence sequence

Capture screenshots from real terminal runs in this order:

1. **SS1 — Original program:** run the original starter application using valid sample inputs.
2. **SS2 — Fuzz failures:** run the completed Hypothesis tests against the original buggy application and capture the failing output.
3. **SS3 — Fixed program:** replace the starter implementation with the hardened implementation and run it with valid sample inputs.
4. **SS4 — Passing tests:** run the completed Hypothesis tests against the fixed implementation and capture the passing output.

Commands:

```powershell
py marathon_registration_parser.py
py -m pytest test_marathon_registration_parser.py -v
```

Do not claim the original tests failed or the fixed tests passed until the corresponding commands have actually been run.

## Fixed input behaviour

- `format_bib_name`: returns an uppercase, trimmed name limited to 12 characters; invalid types return an empty string.
- `parse_finish_time`: returns seconds for valid H:MM:SS input; invalid values return `None`.
- `average_split`: returns the average of non-negative integer splits; invalid or empty values return `None`.

## Submission

Include the fixed application, Hypothesis tests, and a PDF containing SS1–SS4 plus answers to the handout's reflection questions.
