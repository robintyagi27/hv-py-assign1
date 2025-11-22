
# 1-Assigment-Password Strength Checker (Python)

This project is a simple **Password Strength Checker** written in Python.  
It validates a password based on multiple security rules such as length, uppercase letters, lowercase letters, digits, and special characters.

---
---

##  Requirements

- Python 3.x  
- No external libraries required (uses built-in **re** module)

---

##  Screenshots

###  Program Running (Example Output) 

<img width="1130" height="370" alt="image" src="https://github.com/user-attachments/assets/c139cc65-c4ea-4982-b51d-0ad7aef88494" />


---

##  Project Structure

```
root/

├── password-python.py
├── README.md

```

---

##  How It Works

The script checks the password against the following criteria:

- ✔ Minimum **8 characters**  
- ✔ At least **one uppercase letter**  
- ✔ At least **one lowercase letter**  
- ✔ At least **one digit (0–9)**  
- ✔ At least **one special character**  
- ✔ Provides **feedback** if password is weak  

---

##  Example Output

**Strong Password Example:**

```
--- Password Strength Checker ---
Enter a password to check (or 'quit' to exit): Test@123
```
<img width="741" height="118" alt="image" src="https://github.com/user-attachments/assets/859161b4-b189-4221-9356-50c85bb99038" />

```

Password Strength: STRONG
Your password meets all the required criteria.
```
<img width="590" height="104" alt="image" src="https://github.com/user-attachments/assets/bad14373-d344-4c15-9d95-d64a9c5893a3" />


```

**Weak Password Example:**

```
Password Strength: WEAK
Your password does NOT meet the required criteria. Please address the following:
- Password must contain at least one uppercase letter.
- Password must contain at least one digit.
  
<img width="741" height="118" alt="image" src="https://github.com/user-attachments/assets/a51ba79c-155b-4d45-81f1-c0e6f375468f" />

```

---

##  How to Run This Program

### 1️ Install Python  
Download from https://www.python.org/

### 2️ Save the script as:
```
password-python.py
```

### 3️ Run the script

```
python password-python.py
```


## 2-Assgiment CPU Health Monitor (Python + psutil)

---
This project continuously monitors your **CPU usage** and generates an **alert** whenever CPU load exceeds a specified threshold.

The script uses the `psutil` library to get accurate CPU usage data and displays status every few seconds.

---


---

##  Requirements

- Python 3.x  
- psutil` library  
---


##  Screenshot (Example Output)

<img width="359" height="480" alt="image" src="https://github.com/user-attachments/assets/dc944298-4dfc-4593-9c13-f223d39f7c94" />
---

##  Project Structure

```
root/

├── cpu_monitor.py
├── README.md

```

---

##  Features

- Real-time CPU monitoring  
- Adjustable CPU threshold (default: **80%**)  
- Adjustable monitoring interval  
- Alerts displayed when CPU usage exceeds threshold  
- Graceful exit using **Ctrl + C**

---

##  Example Output

```
Monitoring CPU usage... (Alert threshold: 80%)
Press Ctrl+C to stop monitoring.
Current CPU usage: 12%
Current CPU usage: 18%
Alert! CPU usage exceeds threshold: 85%
Current CPU usage: 20%

<img width="901" height="297" alt="image" src="https://github.com/user-attachments/assets/03587402-0659-4ede-be09-a59ede3573a2" />

<img width="359" height="480" alt="image" src="https://github.com/user-attachments/assets/30294efc-088f-4101-bc30-96c960db5d76" />


```

---

##  How to Run the Script

### 1️ Install dependencies  
```
pip install psutil
```

### 2️ Save the script as:
```
cpu_monitor.py
```

### 3️ Run the script:
```
python cpu_monitor.py
```


# 3-Assigment- automating configuration management

---

##  Features

- Parse configuration in **INI format**
- Extract values based on section (e.g., `[Database]`, `[Server]`)
- Store final output as **JSON**
- Expose GET endpoint to retrieve stored configuration
- Handles missing files and read errors gracefully
- Lightweight Flask API

---

##  Project Structure

auto-config-mgmt/
│
├── app.py # Main application
├── config.ini # Input configuration file
├── config_output.json # Parsed output (auto-generated)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

##  Sample Input File (config.ini)

[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080


---

##  How It Works

1. When you run the application:  
   ```bash python app.py

The program reads config.ini

Extracts each section and its key-value pairs

Converts data into a Python dictionary

Saves the results as JSON into config_output.json

A Flask API is started on port 5000

The endpoint GET /config returns stored JSON

 Error Handling

If config.ini is missing → error printed

If file is unreadable → descriptive error

If JSON output missing → API returns 404 with message

 Running the Application
1. Install Dependencies
pip install -r requirements.txt

2. Run the App
python app.py

3. Access API

 Open your browser:

http://localhost:5000/config

<img width="1007" height="170" alt="image" src="https://github.com/user-attachments/assets/33e8660c-d192-427b-af67-389d722e7b07" />


 Sample API Response
{
    "Database": {
        "host": "localhost",
        "port": "3306",
        "username": "admin",
        "password": "secret"
    },
    "Server": {
        "address": "192.168.0.1",
        "port": "8080"
    }
}

 config_output.json (Generated Output)
{
    "Database": {
        "host": "localhost",
        "port": "3306",
        "username": "admin",
        "password": "secret"
    },
    "Server": {
        "address": "192.168.0.1",
        "port": "8080"
    }
}

 Screenshots (Add Yours Here)
 App Running

<img width="1117" height="240" alt="image" src="https://github.com/user-attachments/assets/25c9b34e-d983-4ec9-84ac-191e881d5a65" />


 API Output

<img width="1007" height="170" alt="image" src="https://github.com/user-attachments/assets/ecda4262-e24f-41c8-b36d-c644659929b4" />


 JSON File

<img width="669" height="367" alt="image" src="https://github.com/user-attachments/assets/dfeeeb74-7dd1-4c9c-9111-96be801f16cc" />







