# Lab 6 — Code and Branch Coverage Analysis

Application under test: `marathon_registration.py`

## Files

- `marathon_registration.py` — application under test
- `CodeCoverageTest_PES1UG24AM438_marathon_registration.py` — code/line coverage tests
- `BranchCoverageTest_PES1UG24AM438_marathon_registration.py` — branch coverage tests
- `test_marathon_registration.py` — additional application tests

## Setup

From the repository root:

```powershell
python -m pip install pytest coverage
cd lab06
```

## Code coverage

```powershell
python -m coverage erase
python -m coverage run --source=marathon_registration -m pytest -v CodeCoverageTest_PES1UG24AM438_marathon_registration.py
python -m coverage report -m
```

Verified local result: **4 passed; 97% statement coverage** (38 statements, 1 missing).

## Branch coverage

```powershell
python -m coverage erase
python -m coverage run --branch --source=marathon_registration -m pytest -v BranchCoverageTest_PES1UG24AM438_marathon_registration.py
python -m coverage report -m
```

Verified local result: **18 passed; 100% coverage** (38 statements, 28 branches, 0 partial branches).

Both results exceed the handout's 90% target. The terminal screenshots should be included with the lab submission evidence.
