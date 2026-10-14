# Lab 5 — Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style violations.

### 2. What did Pylint, Bandit, and Flake8 detect?

Pylint identified code-quality problems, including missing docstrings, naming violations, a mutable default argument, and broad exception handling. Bandit flagged SQL query construction, unsafe pickle deserialization, and random-number generation. Flake8 identified long lines, an ambiguous variable name, a bare exception, and formatting issues.

### 3. What improvements were made?

The program was updated to use parameterized SQL queries, JSON serialization, safer default arguments, specific exception handling, descriptive names, docstrings, and consistent formatting.

### 4. How were the fixes verified?

The updated program was executed, and all three static-analysis tools were rerun. Pylint improved from 4.57/10 to 10/10, Bandit reported no issues, and Flake8 returned exit code 0.

### 5. What did you learn?

Static-analysis tools can identify code-quality, security, and formatting problems before deployment. Using multiple tools provides complementary checks, while rerunning them after changes helps verify that the reported issues have been addressed.