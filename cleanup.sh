#!/bin/bash

echo "Performing Cleanup"
sudo find /home/pi/scms/code/components -name "*.pyc" -exec rm -f {} \;