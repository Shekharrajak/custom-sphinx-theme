#!/usr/bin/env bash
export NUMPYVER:=$(shell python3 -c "import numpy; print(numpy.version.git_revision[:10])")

echo $NUMPYVER

cd docs && GITVER=$(NUMPYVER) make html