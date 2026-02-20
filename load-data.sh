#!/bin/bash
# This script runs automatically when the container first starts

mongoimport --db university --collection instructors --file /data/instructors.json --jsonArray
mongoimport --db university --collection courses --file /data/courses.json --jsonArray

echo "Database loaded successfully!"
