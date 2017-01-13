#!/bin/bash
rm ./data/*.csv
wget -r -nH -nd -np -P ./data/ -R index.html* $1
cat ./data/2* > mm.csv

