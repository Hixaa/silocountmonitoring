#!/bin/bash

echo "[+] Replacing config_scms.ini"
sudo cp -f https://raw.githubusercontent.com/Hixaa/silocountmonitoring/main/scms/config_scms.ini /

echo "[+] Replacing components folder"
sudo cp -f  https://raw.githubusercontent.com/Hixaa/silocountmonitoring/main/scms/components/ /
