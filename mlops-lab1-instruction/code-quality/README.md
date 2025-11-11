# Code Quality

## Overview

Maintaining high code quality ensures **readability, maintainability, and consistency** across the project.
In this section, you’ll learn how to format, lint, and check your code manually and automatically using **Black**, **isort**, **Flake8**, and **Pre-commit**.

---

## Getting Started

### Step 1 – Navigate to the Project Directory

```bash
cd mlops-lab/lab1/src/lab1/data_preprocessing
```

---

##  Run Code Quality Checks Manually

### 1. Format Code with **Black**

```bash
black preprocessing.py
```

Observe the formatting changes in `preprocessing.py`.

---

### 2. Sort Imports with **isort**

```bash
isort preprocessing.py
```

Review the updated imports in `preprocessing.py` and fix if needed.

---

### 3. Lint Code with **Flake8**

```bash
flake8 preprocessing.py
```

Review linting errors or warnings and fix them accordingly.

---

## Run Code Quality Checks Using **Pre-commit**

The `.pre-commit-config.yaml` file defines repositories and hooks for automated checks.
To manually or automatically run these hooks, follow the steps below.

---

### Step 1 – Move to the Project Root

```bash
cd mlops-lab
```

---

### Step 2 – Configure `.pre-commit-config.yaml`

Ensure your `.pre-commit-config.yaml` file includes all necessary hooks (e.g., `black`, `isort`, `flake8`, `end-of-file-fixer`, etc.).
Edit or complete it where indicated by `# your code here`.

---

###  Step 3 – Run Pre-commit Hooks Manually

```bash
pre-commit run --all-files
```

or

```bash
pre-commit run -a
```

Observe the results and fix issues if any hooks fail.

Learn more about pre-commit hooks: [https://pre-commit.com](https://pre-commit.com)

---

## Automate Code Quality with Pre-commit Hooks

### Step 4 – Install the Git Hook Scripts

Run the following command to install pre-commit hooks.
This ensures checks are executed automatically on every `git commit`.

```bash
pre-commit install
```

---

### Step 5 – Auto-update Pre-commit Hooks

To update all hooks to their latest versions:

```bash
pre-commit autoupdate
```

---

### Pro Tip

When adding new hooks or updating existing ones, it’s a good practice to run them across the entire codebase:

```bash
pre-commit run --all-files
```

> Usually, pre-commit runs only on modified files during `git commit`. Running it manually on all files ensures consistency across the entire repository.

