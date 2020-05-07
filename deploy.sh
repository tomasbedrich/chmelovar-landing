#!/usr/bin/env sh

# this script is intended to run only manually on delta.tbedrich.cz

set -x
docker pull tomasbedrich/chmelovar-landing:latest
sudo chown -R ja:ja data/
docker-compose down
docker-compose -f docker-compose.production.yaml up -d
