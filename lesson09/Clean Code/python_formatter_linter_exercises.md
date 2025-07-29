# Hands-On: Code Formatting and Linting in Python

These exercises will help you learn to automatically format Python code using tools like `black`, and identify problems using linters like `flake8` or `pylint`.

---

### Exercise 1: Format Code with `black`

**Goal**: Use `black` to autoformat an unformatted Python script.

1. Create a file named `messy.py` with the following content:

```python
def greet(name): print("Hello,"+name)
greet("world")
```

2. Run `black`:

```bash
black messy.py
```

✅ *Check*: The file should now be properly formatted with consistent indentation and spacing.

---

### Exercise 2: Format an Entire Directory

**Goal**: Use `black` to format all `.py` files in a project.

```bash
black .
```

✅ *Check*: All Python files in the current directory and subdirectories are formatted.

---

### Exercise 3: Install and Run `flake8`

**Goal**: Use `flake8` to identify potential issues in a Python file.

1. Install `flake8` (if not already):

```bash
pip install flake8
```

2. Create a file `bad_style.py`:

```python
import os,sys

def unused_function():
    pass

print(   "hi")
```

3. Run `flake8`:

```bash
flake8 bad_style.py
```

✅ *Check*: Output should list issues such as unused imports, extra spaces, and unused functions.

---

### Exercise 4: Lint with `pylint`

**Goal**: Use `pylint` to get more detailed feedback.

1. Install `pylint`:

```bash
pip install pylint
```

2. Run it on `bad_style.py`:

```bash
pylint bad_style.py
```

✅ *Check*: You'll receive a score and detailed output for code quality, style, and possible bugs.

---

### Exercise 5: Configure `flake8` with a Config File

**Goal**: Customize `flake8` using a configuration file.

1. Create a `.flake8` file:

```
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

2. Re-run:

```bash
flake8 bad_style.py
```

✅ *Check*: Some warnings will now be ignored or relaxed according to the config.

---

### Exercise 6: Format and Lint as a Pre-Commit Hook

**Goal**: Set up autoformatting and linting with `pre-commit`.

*Note*: you will need to be in a repository for this to work properly.  You can start a repo with `git init` or put this in an existing repository.

1. Install the tool:

```bash
pip install pre-commit
```

2. Create a `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
```

3. Install hooks:

```bash
pre-commit install
pre-commit run --all-files
```

✅ *Check*: Try committing and ensure that the files are formatted and checked before committing.

---

### Exercise 7: Add More Tools to Pre-Commit

**Goal**: Enhance your pre-commit workflow by adding additional code quality tools.

1. Update your `.pre-commit-config.yaml` to include more hooks, such as `isort` (for import sorting), `docformatter` (for docstring formatting), and other useful tools:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort
  - repo: https://github.com/PyCQA/docformatter
    rev: 1.7.5
    hooks:
      - id: docformatter
        args: ["--in-place", "--recursive", "."]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.7
    hooks:
      - id: bandit
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
  - repo: https://github.com/codespell-project/codespell
    rev: v2.2.6
    hooks:
      - id: codespell
```

2. Reinstall the hooks to update them:

```bash
pre-commit install
pre-commit run --all-files
```

✅ *Check*: Try committing again. Now, in addition to formatting and linting, your code will be checked for types, security issues, spelling, trailing whitespace, file