#!/bin/bash

echo "Performing Cleanup"
sudo find /home/pi/silocountmonitoring/scms/components -type f -name "*.pyc" -exec rm -f {} \;
