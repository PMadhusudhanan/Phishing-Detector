![Python](https://img.shields.io/badge/Python-3.x-blue)
![Made with ❤️](https://img.shields.io/badge/Made%20with-Love-red)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

# 🛡️ Phishing Detector Tool

A lightweight command-line tool to detect suspicious or phishing websites based on URL patterns, SSL status, and domain analysis.

---

## 📸 Demo

```
$ phishdetect https://example-login.com
```

Output:

```
[🔵] Checking URL: https://example-login.com
[🛡️] SSL Certificate: VALID
[⚠️] Suspicious Keywords Detected: login
[🔴] Warning: This website may be a phishing attempt!
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/PMadhusudhanan/Phishing-Detector.git
cd Phishing-Detector
chmod +x install.sh
./install.sh
```

✅ After installation, you can use it **anywhere** from the terminal as a **global tool**!

---

## 🚀 Usage

Simple one-line command:

```bash
phishdetect https://suspicious-site.com
```

No need to activate any virtual environment manually!

---

## 🛠️ Features

- 🔍 **URL Pattern Analysis** (detects suspicious words like "login", "secure", "update")
- 🔒 **SSL Certificate Validation**
- 🌐 **TLD (Top-Level Domain) Check** for suspicious domains
- 🎨 **Beautiful CLI Output** using colors
- ⚡ **Fast & Lightweight**, no heavy libraries

---

## 📦 Dependencies

- `colorama`
- `tldextract`
- `requests`

(Handled automatically by the install script.)

---

## 🧹 Uninstallation

If you want to remove the tool:

```bash
sudo rm /usr/local/bin/phishdetect
```

---

## 🤝 Contribution

Pull requests are welcome!  
If you have any improvements (like new detection techniques), feel free to contribute.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use it in your own tools and research!

---

# 💬 Contact

🔹 **GitHub**: [PMadhusudhanan](https://github.com/PMadhusudhanan)  
🔹 **LinkedIn**: https://www.linkedin.com/in/madhusudhanan-p-242538310?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

---

# 🚀 Star this repo if you find it helpful!

---

# 📢 Notes:
- Make sure you have **Python 3.8+** installed.
- For Kali Linux users: use `sudo pip install` if necessary.
