
# Lab 1 — Code Versioning with Git

##  Overview

**Code versioning** is the practice of tracking and managing changes to your source code over time using a Version Control System (VCS), most commonly **Git**.
It’s the backbone of **collaborative, reproducible, and auditable** workflows in MLOps and Data Science.

---

## Objectives

By the end of this lab, students will be able to:

* Understand and use **Git fundamentals** (commits, branches, merges, tags)
* Differentiate between **staged and unstaged** changes
* Use **diffs and logs** to explore code evolution
* Write **unit tests** and run them with `pytest`
* Apply **clean version control** practices with `.gitignore`
* Collaborate and manage repositories like a professional **MLOps engineer**

---

##  Prerequisites

Make sure you have the following installed and configured:

* Python (≥=3.11)
* Git
* Familiarity with Python basics (functions, DataFrames)
* Access to:

  * [Git Cheat Sheet](https://git-scm.com/cheat-sheet)
  * [Pandas Documentation](https://pandas.pydata.org/docs/reference/index.html)

---

## Getting Started

### Step 1 — Fork and Clone the Repository

```bash
git clone https://github.com/TouyeAchille/mlops-lab.git
cd mlops-lab
git status
```

This verifies that your working directory is under version control.

---

## Part I — Complete and Run the Preprocessing Script

### Step 2 — Navigate to the Preprocessing Directory

```bash
cd lab1/src/lab1/data_preprocessing
```

### Step 3 — Complete the Code

Open and complete the script:

```
data_preprocessing.py
```

Add the missing logic where indicated by `"your code here"`.

### Step 4 — Run the Script

```bash
python data_preprocessing.py --input_data_path ../../../../datastores/raw_csv_data/census.csv --output_data_path clean_census.csv
```

Observe the logs and verify that a cleaned dataset is generated.

---

## Part II — Version Your Code with Git

### Step 5 — Check the Status

```bash
git status
```

### Step 6 — Stage the File

```bash
git add data_preprocessing.py
git status
```

### Step 7 — Commit with a Descriptive Message

```bash
git commit -m "data preprocessing: remove duplicates and strip whitespace in DataFrame"
git status
```

> Tip: Commit messages should follow the format
> **`<scope>: <concise description>`**

---

## Part III — Explore Changes and History

### Step 8 — View Unstaged or Staged Changes

```bash
git diff
```

### Step 9 — Explore Commit History

```bash
git log --oneline
git log --oneline --stat
```

---

## Part IV — Push Your Work

### Step 10 — Push Changes to Remote

```bash
git push origin master
```

---

##  Key Configuration Files

| File           | Purpose                                                        |
| -------------- | -------------------------------------------------------------- |
| `.gitignore`   | Excludes unnecessary files (e.g. `__pycache__/`, `.env`, logs) |
| `~/.gitconfig` | Global Git configuration                                       |
| `.git/config`  | Local repository configuration                                 |

---

## Part V — Add and Run Unit Tests

### Step 11 — Navigate to the Test Directory

```bash
cd lab1/tests/unit_tests
```

### Step 12 — Complete the Test Scripts

Complete the following:

* `test_preprocessing.py`
* `conftest.py`

Each contains `"your code here"` placeholders for students to fill in.

### Step 13 — Run All Tests

```bash
pytest -vv lab1/src/tests/unit_tests/
```

 Fix any failing tests until all pass successfully.

---

## Part VI — Commit and Push Your Tests

### Step 14 — Stage and Commit

```bash
git add conftest.py test_preprocessing.py
git commit -m "add pytest configuration and preprocessing unit tests"
```

### Step 15 — Review and Push

```bash
git diff
git log --oneline --stat
git push origin master
```

---

##  Summary

At the end of this lab, you should have:

1. A **clean preprocessing script** with reproducible transformations
2. Properly **versioned code** in Git
3. **Passing unit tests** for validation
4. A workflow aligned with **MLOps best practices**

---


