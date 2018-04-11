#!/bin/sh
cd $TRAVIS_BUILD_DIR/virtualclinic
sbt ++$TRAVIS_SCALA_VERSION package