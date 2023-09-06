#!/bin/bash

echo "[+] Cloning the source"
git clone https://github.com/hixaa/eemsv2
cd eemsv2

echo "[+] Starting Debloat"

# Remove bloatware
sudo apt remove --purge dillo vlc chromium-browser geany thonny piclone qpdfview rpi-imager mousepad galculator gpicview rp-bookshelf debian-reference-common -y

# autoremove
sudo apt autoremove -y

# clean
sudo apt autoclean -y

echo "[+] Performing system upgrade"
# update
sudo apt update
sudo apt upgrade -y

echo "[+] Set nameserver to 8.8.8.8"
sudo cp resolv.conf.head /etc/

echo "[+] Installing anydesk"
# install anydesk
sudo apt install libminizip1 libegl1-mesa -y
sudo apt install libgles-dev libegl-dev -y
sudo ln -s /usr/lib/arm-linux-gnueabihf/libGLESv2.so /usr/lib/libbrcmGLESv2.so
sudo ln -s /usr/lib/arm-linux-gnueabihf/libEGL.so /usr/lib/libbrcmEGL.so
sudo ldconfig
sudo apt install ./tools/anydesk_6.1.1-1_armhf.deb

echo "[+] Enable VNC"
sudo systemctl enable vncserver-x11-serviced.service

echo "[+] Installing scripts"
sudo apt install vim -y
pip3 install urllib3
pip3 install requests
pip3 install chardet
sudo cp cleanup.sh /
sudo chmod +x /cleanup.sh
#sudo mv xaees/xaees.service /lib/systemd/system/
#sudo cp -r xaees/* /

#echo "[-] Yet to make a service onboot"
#sudo systemctl enable xaees
#sudo systemctl start xaees

#echo "[+] Enabled xaees for ON BOOT"

echo "[+] Done with the installation"
echo "[*] Please do a REBOOT"
