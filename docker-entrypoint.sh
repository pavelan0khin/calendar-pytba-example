#!/bin/sh
set -e
set -x

export PYTHONUNBUFFERED=0


case "$1" in
    web)
        poetry run uvicorn src.main:app --host 0.0.0.0 --port 8001
    ;;
esac
