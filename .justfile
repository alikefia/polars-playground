# format and lint code (just and python)
fmt:
    #!/usr/bin/env bash
    just --unstable --fmt
    ruff format py
    ruff check --fix py

# install deps
deps:
    #!/usr/bin/env bash
    pip install -U pip
    pip install -U -r requirements.txt
    pip install -U -r requirements.dev.txt

# build polars
@build:
    (cd deps/polars/py-polars && maturin develop)

# run current script
@run:
    python py/i-${CURRENT}.py