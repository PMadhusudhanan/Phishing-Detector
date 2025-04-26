#!/bin/bash

echo "🔵 Installing Phishing Detector Tool..."

# Step 1: Install required python packages globally
echo "🔵 Installing Python packages (colorama, tldextract)..."
sudo pip install colorama tldextract

# Step 2: Make script executable
echo "🔵 Making phishdetect executable..."
chmod +x phishdetect.py

# Step 3: Move script to /usr/local/bin
echo "🔵 Moving to /usr/local/bin/ as 'phishdetect' command..."
sudo cp phishdetect.py /usr/local/bin/phishdetect

# Step 4: Success message
echo "✅ Installation complete! You can now use it like:"
echo ""
echo "   phishdetect https://example.com"
echo ""

exit 0
