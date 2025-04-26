![Python](https://img.shields.io/badge/Python-3.x-blue)
![Made with ❤️](https://img.shields.io/badge/Made%20with-Love-red)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# Phishing Detection Tool 🛡️

A lightweight Python CLI tool to detect potential phishing websites using URL analysis, SSL verification, and basic keyword detection.

---

## 🚀 Features

- ✅ Extracts domain and subdomain information
- ✅ Checks for suspicious keywords in URLs
- ✅ Validates SSL certificate status
- ✅ Easy to use from the command line
- ✅ Beginner-friendly and lightweight

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/PMadhusudhanan/Phishing-Detector.git
cd Phishing-Detector
```

2. **Install required packages**:

```bash
pip install -r requirements.txt
```

---

## ⚡ Usage

Run the tool by providing a URL:

```bash
python phishing_detector.py
```

Follow the prompts to input a website link.

Example:

```bash
Enter a URL: http://example-login.security-update.com

```
## 📸 Demo

![Phishing Detector Demo](demo.png)


---

## 🛠️ Built With

- Python 🐍
- Libraries: `tldextract`, `colorama`, `ssl`, `socket`

---

## 📄 Requirements

- Python 3.x
- Internet connection (for SSL checking)

---

## 🤔 How It Works

- Extracts the domain from the URL
- Searches for suspicious keywords like `login`, `secure`, `account`, `bank`
- Checks if SSL certificate is valid
- Warns if anything looks suspicious

---

## 📚 Future Improvements

- Add machine learning based URL classification
- Create a browser extension version
- Real-time monitoring of URLs

---

## 🙏 Acknowledgments

This project was created as part of a learning exercise in cybersecurity and phishing detection.

---

## 📬 Contact

- GitHub: [PMadhusudhanan](https://github.com/PMadhusudhanan)
- Email:  pmadhusudhanan2020@gmail.com
  





