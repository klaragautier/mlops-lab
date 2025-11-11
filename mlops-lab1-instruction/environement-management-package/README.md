Parfait ⚙️ Voici la **version finale professionnelle** en **Markdown**, claire, homogène et prête à copier-coller dans ton README.md, ta doc MkDocs ou ton notebook d’introduction à MLOps 👇

---

# Environment and Dependency Management

## Overview

One of the first steps in **AI, Data Science, and MLOps** is to create an **isolated virtual environment** to manage your project’s dependencies.
You can create and manage environments using **pip** or **conda**.

In **MLOps best practices**, we often adopt a **hybrid approach** such as:

* `(conda + poetry)`
* `(pip + poetry)`
* `(pip + uv)`
* `(conda + uv)`

This hybridization combines the robustness of environment isolation (via `conda` or `venv`) with modern dependency management and lockfile reproducibility (via `poetry` or `uv`).

---

## Tool Overview

### 1. Conda

**Conda** is an open-source **package and environment management system**.
It allows you to install and switch between multiple versions of software packages and their dependencies.

* Works on Linux, macOS, and Windows
* Manages both Python and non-Python libraries (C/C++, R, CUDA)
* Ideal for **machine learning, data science, and reproducibility**

Learn more:

* [Getting Started with Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
* [Installing Miniconda/Anaconda](https://www.anaconda.com/docs/getting-started/miniconda/main)

---

### 2. Poetry

**Poetry** is a tool for **Python dependency management and packaging**.
It allows you to:

* Declare project dependencies in `pyproject.toml`
* Automatically resolve and lock dependencies in `poetry.lock`
* Build and publish Python packages easily

Poetry can either use its own virtual environments or integrate with existing ones like Conda.

Learn more:

* [Poetry Documentation](https://python-poetry.org/docs/)

---

### 3. uv

**uv** is a **fast, modern Python package and environment manager**, written in **Rust**.
It provides:

* Lockfile-based reproducibility
* Multi-project workspace support
* Extremely fast dependency resolution

`uv` can be used as a lightweight alternative to Poetry.

Learn more:

* [uv Documentation](https://docs.astral.sh/uv/)

---

### 4. pip

**pip** is the standard **Python package installer**.
It installs packages from [PyPI](https://pypi.org/) and manages dependencies via `requirements.txt`.

Learn more:

* [pip Documentation](https://pip.pypa.io/en/stable/getting-started/)

---

## Setup Instructions

### Step 1 — Create a Conda Environment

From the root directory of your project (e.g., `mlops-lab`):

```bash
conda env create -f conda.yml
```

This command will:

* Create a new virtual environment defined in `conda.yml`
* Install all dependencies and the specific Python version required for the lab

---

### Step 2 — Activate the Conda Environment

```bash
conda activate mlops_env
```

---

### Step 3 — Verify the Environment

List all existing Conda environments:

```bash
conda env list
```

---

### Step 4 — Add Additional Packages with Poetry

Add new dependencies to `pyproject.toml` and install them:

```bash
poetry add poetry-plugin-export pandas uvicorn gunicorn
```

Alternatively, you can add packages using other managers:

```bash
pip install <package_name>
conda install <package_name>
uv add <package_name>
```

However, in this **hybrid approach (conda + poetry)**, we primarily rely on Poetry to manage Python dependencies for consistency and reproducibility.

---

### Step 5 — Validate Poetry Configuration

Check the integrity of your `pyproject.toml` and `poetry.lock` files:

```bash
poetry check
```

---

### Step 6 — Check Environment Health

Run a diagnostic on your Conda environment:

```bash
conda doctor -n mlops_env
```

---

### Step 7 — Verify Dependency Compatibility

Check for any dependency conflicts within your environment:

```bash
pip check
```

---

### Step 8 — View Poetry Environment Info

Display detailed information about the Poetry environment:

```bash
poetry env info
```

---

### Step 9 — Manage Dependencies During Development

* Add new packages:

  ```bash
  poetry add <package_name>
  ```

* Update dependencies:

  ```bash
  poetry update
  ```

* Install all project dependencies defined in pyproject.toml:

  ```bash
  poetry install
  ```

---

## Conceptual Diagram

```text
┌──────────────┐
│   Conda Env  │── manages system libs (Python, CUDA, etc.)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Poetry     │── manages Python deps (pyproject.toml)
└──────────────┘
```

---

## Summary

| Tool       | Role                                  | Strength                                        |
| ---------- | ------------------------------------- | ----------------------------------------------- |
| **conda**  | Environment and dependency manager    | Handles non-Python binaries (e.g., C/C++, CUDA) |
| **poetry** | Python dependency and packaging tool  | Lockfile reproducibility and version pinning    |
| **uv**     | Modern Rust-based environment manager | High performance and lockfile-based             |
| **pip**    | Python package installer              | Simple and lightweight                          |

---
