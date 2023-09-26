#!/bin/bash

echo "Performing Cleanup"
sudo find /home/pi/silocountmonitoring/scms/code/components -name "*.pyc" -exec rm -f {} \;
