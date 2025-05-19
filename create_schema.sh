#!/usr/bin/env bash

# set -a makes automatically exports all subsequent variables
set -a

# source the env file containing the variables
source .env

# reset the -a option
set +a

# create the schema
mysql -u $DB_USER -h $DB_HOST -p"$DB_PASSWORD" $DB_NAME < schema.sql
