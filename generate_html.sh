#!/usr/bin/env bash
# echo $TRAVIS_COMMIT
pin install numpy
cd docs && GITVER=31465473c4 make html