#!/bin/bash

[ ! -f "data.json" ] && curl "https://data.lacity.org/api/geospatial/yru6-6re4?method=export&format=GeoJSON" -o data.json
python json_perf_meter/main.py json
for i in $(cat requirements.txt); do python json_perf_meter/main.py $i; done