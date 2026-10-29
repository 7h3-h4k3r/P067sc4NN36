<div>
  <img src="image/logo.png" alt="Logo" align="left" width="500" style="margin-right: 20px;" />
</div>


### 🔍 Python Port Scanner
  
**A fast and customizable port scanner built with Python.**  
Scan targets with precision and flexibility using intuitive command-line options.


### 📜 Features
- 🎯 **Target-Specific Scans**: Scan a single target effortlessly.
- 🚀 **Range-Based Scans**: Specify custom port ranges for scanning.
- ⚡ **Fast and Reliable**: Optimized for speed and accuracy.

---

## 🔧 Usage
### **installation process**
```bash
git clone https://github.com/7h3-h4k3r/P067sc4NN36.git 

```
- **Description**: download lib colorama using pip to install if you don't already have.

---
### Option 1: **Quick Target Scan**
```bash
python3 portscanner.py -Tp -s <target-ip>
```
- **Description**: Scan all open ports on the specified target.

---

### Option 2: **Custom Port Range Scan**
```bash
python3 portscanner.py -Tp <target-ip> -sP <starting-port-number> -Ep <ending-port-number>
```
- **Description**: Specify a range of ports to scan on the target.

---

## 🛠️ Requirements
- Python 3.x
- Network permissions to access the target system.

---

## 🌟 Example
### Scan All Ports on `192.168.1.1`:
```bash
python3 portscanner.py -Tp -s 192.168.1.1
```

### Scan Ports `20` to `80` on `192.168.1.1`:
```bash
python3 portscanner.py -Tp 192.168.1.1 -sP 20 -Ep 80
```

---

## 💻 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/7h3-h4k3r/P067sc4NN36.git
   ```
2. Navigate to the project directory:
   ```bash
   cd P067sc4NN36
   ```
3. Run the script with Python 3.
   ```
   python3 python3 portscanner.py -Tp -s <target ip>
   ```

---

## 🛡️ Note
Always ensure you have permission before scanning any network or system.

---

### ✨ Happy Scanning!