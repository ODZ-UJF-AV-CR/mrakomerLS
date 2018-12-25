#!/bin/bash
echo $1 $2
sudo date +'%Y%m%d %H:%M:%S' --set "$1 $2"