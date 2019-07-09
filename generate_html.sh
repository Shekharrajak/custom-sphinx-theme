#!/usr/bin/env bash
# echo $TRAVIS_COMMIT
pip install numpy
pwd
cd docs/src/custom-sphinx-theme && python setup.py install
pwd
cd ../../docs && GITVER=31465473c4 make html