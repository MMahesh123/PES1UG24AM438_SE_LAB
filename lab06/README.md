# Lab 6 — Code and Branch Coverage

Application under test: `marathon_registration.py`

Test module: `test_marathon_registration.py`

## Setup

From this folder:

```powershell
py -m pip install pytest coverage
py -m pytest -v
```

## Line coverage

```powershell
py -m coverage erase
py -m coverage run --source=marathon_registration -m pytest -q
py -m coverage report -m
```

## Branch coverage

```powershell
py -m coverage erase
py -m coverage run --branch --source=marathon_registration -m pytest -q
py -m coverage report -m
```

Save terminal screenshots showing the actual successful test run and coverage report. Do not edit the reported percentages manually.

## Required commits

1. Add test cases for code coverage.
2. Add test cases for branch coverage.

The same comprehensive test module supports both runs; use separate commits as required by the lab handout.
