#!/bin/bash
while true; do last_file=$(ls *.csv | sort -V | tail -n 1); echo $last_file; tail $last_file ; echo h > /dev/ttyUSB0; sleep 5; done