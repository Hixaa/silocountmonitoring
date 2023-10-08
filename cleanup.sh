#!/bin/bash

echo "Performing Cleanup"
sudo find /components -type f -name "*.pyc" -exec rm -f {} \;
