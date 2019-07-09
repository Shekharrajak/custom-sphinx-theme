#!/usr/bin/env bash
# echo $TRAVIS_COMMIT
pin install numpy
cd docs/src/custom-sphinx-theme && python setup.py install
cd ../../docs && GITVER=31465473c4 make html