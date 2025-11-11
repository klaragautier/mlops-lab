# Environment and Dependency Management

## Overview

One of the first steps in **AI, Data Science, and MLOps** is to create an **isolated virtual environment** to manage your project’s dependencies.
You can create and manage environments using **pip** or **conda**.

In **MLOps best practices**, we use a **hybrid approach** such as:

* `(conda + poetry)`
* `(pip + poetry)`
* `(pip + uv)`
* `(conda + uv)`

This hybridization allows you to combine the robustness of environment isolation (via `conda` or `venv`) with modern dependency management and lockfile reproducibility (via `poetry` or `uv`).

---

## Tools Overview

### **1. Conda**

Conda is an open-source **package and environment management system**.
It helps install multiple versions of packages and their dependencies and switch easily between environments.
Originally created for Python, Conda can package and distribute **any software**, including C/C++, R, or CUDA-based libraries.

* Works on Linux, macOS, and Windows.
* Supports both `conda` and `conda-forge` channels for package sources.
* Ideal for **machine learning, data science, and reproducibility**.

Learn more:
[Getting Started with Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)
[Installing Miniconda/Anaconda](https://www.anaconda.com/docs/getting-started/miniconda/main)

---

### **2. Poetry**

Poetry is a tool for **Python dependency management and packaging**.
It allows you to:

* Declare project dependencies in `pyproject.toml`.
* Automatically resolve and lock dependencies in `poetry.lock`.
* Build and publish Python packages easily.

Poetry can manage its own virtual environments or use existing ones (like a conda env).

Learn more:
[Poetry Documentation](https://python-poetry.org/docs/)

---

### **3. uv**

`uv` is a **fast, modern Python package and environment manager**, written in **Rust**.
It provides:

* Lockfile-based reproducibility.
* Support for multi-project workspaces.
* High-speed dependency resolution.

`uv` can be used as a lightweight alternative to Poetry.

Learn more:
[uv Documentation](https://docs.astral.sh/uv/)

---

### **4. pip**

`pip` is the standard **Python package installer**.
It installs packages from [PyPI](https://pypi.org/) and works with `requirements.txt` for reproducibility.

Learn more:
[pip Documentation](https://pip.pypa.io/en/stable/getting-started/)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/TouyeAchille/mlops-lab.git
```

---

### 2. Change Directory

```bash
cd mlops-lab
```

---

### 3. Create a Conda Environment

```bash
conda env create -f conda.yml
```

---

### 4. Activate the Conda Environment

```bash
conda activate mlops_env
```

---

### 5. Add Additional Packages with Poetry

Add new dependencies to `pyproject.toml` and install them:

```bash
poetry add poetry-plugin-export pandas uvicorn gunicorn
```

---

### 6. Check Environment Health

Run a diagnostic on your conda environment:

```bash
conda doctor -n mlops_env
```

---

### 7. Verify Dependency Compatibility

Check for dependency conflicts:

```bash
pip check
```

---

### 8. View Poetry Environment Information

Display information about Poetry’s active environment:

```bash
poetry env info
```

---

### 9. Manage Dependencies During Development

* To **add new packages**:

  ```bash
  poetry add <package_name>
  ```

* To **update dependencies**:

  ```bash
  poetry update
  ```

* To **Installs the project dependencies**

```bash
  poetry install
  ```

---

## Summary

| Tool       | Role                                  | Strength                                        |
| ---------- | ------------------------------------- | ----------------------------------------------- |
| **conda**  | Environment and dependency manager    | Handles non-Python binaries (e.g., C/C++, CUDA) |
| **poetry** | Python dependency and packaging tool  | Lockfile reproducibility and version pinning    |
| **uv**     | Modern Rust-based environment manager | High performance and lockfile-based             |
| **pip**    | Python package installer              | Simple and lightweight                          |


