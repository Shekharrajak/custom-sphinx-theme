#!/usr/bin/env bash
echo $TRAVIS_COMMIT
cd docs && GITVER=$TRAVIS_COMMIT make html