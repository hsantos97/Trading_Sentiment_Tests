#!/bin/sh
docker build -t test .
docker run -it test ./init.sh