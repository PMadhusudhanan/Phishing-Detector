#!/bin/bash
set -e

# Install dependencies via apt if possible
sudo apt update
sudo apt install -y python3-colorama python3-tldextract python3-pip

# Install any missing pip packages globally (careful with --break-system-packages)
sudo pip3 install --break-system-packages some-other-package

# Copy your script to /usr/local/bin and make executable
sudo cp phishdetect.py /usr/local/bin/phishdetect
sudo chmod +x /usr/local/bin/phishdetect

echo "Installed phishdetect system-wide. Run with: phishdetect <url>"
