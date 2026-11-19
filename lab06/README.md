# Lab 6 — Code and Branch Coverage Analysis

Application under test: `marathon_registration.py`

## Files

- `marathon_registration.py` — application supplied in the assigned repository
- `CodeCoverageTest_PES1UG24AM438_marathon_registration.py` — line/code coverage test cases
- `BranchCoverageTest_PES1UG24AM438_marathon_registration.py` — branch coverage test cases

## Setup

From the repository root:

```powershell
py -m pip install pytest coverage
cd lab06
```

## 1. Code coverage

```powershell
py -m coverage erase
py -m coverage run --source=marathon_registration -m pytest -v CodeCoverageTest_PES1UG24AM438_marathon_registration.py
py -m coverage report -m
```

Save a screenshot of the passing test run and the actual coverage report. Target: at least 90%.

## 2. Branch coverage

```powershell
py -m coverage erase
py -m coverage run --branch --source=marathon_registration -m pytest -v BranchCoverageTest_PES1UG24AM438_marathon_registration.py
py -m coverage report -m
```

Save a screenshot of the passing test run and the actual branch coverage report. Target: at least 90%.

## Commits

The two dedicated test files have been added in separate commits as required by the handout. Do not edit or invent coverage percentages; submit the output produced by your actual run.
