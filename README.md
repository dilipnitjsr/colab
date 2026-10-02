# Colab Research Starter

A compact, reproducible Google Colab / Python research starter.

The original repository contained only a "Hello World" notebook. It now provides a named notebook, a deterministic ML example, dependency management, tests, and CI.

## Open in Colab

Open:

`notebooks/research_quickstart.ipynb`

The notebook demonstrates:

- runtime/package version reporting;
- deterministic random seeds;
- synthetic data generation;
- train/test splitting;
- a simple scikit-learn regression model;
- MAE and R² evaluation;
- a short reproducibility checklist.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/quickstart.py
pytest
```

## Repository structure

```text
notebooks/
  research_quickstart.ipynb
examples/
  quickstart.py
tests/
  test_quickstart.py
requirements.txt
```

## Notebook security

Do not commit API keys, access tokens, passwords, private datasets, or service-account credentials in notebook cells or outputs. Use Colab Secrets or environment variables for credentials.

## Purpose

This repository is intentionally small. It can be used as a clean starting point for future Colab experiments while keeping executable logic reproducible outside the notebook.
