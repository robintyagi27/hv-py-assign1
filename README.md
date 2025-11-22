# 1 – Assignment: Password Strength Checker (Python)

This project is a simple Password Strength Checker written in Python.
It validates a password based on multiple security rules such as:

Length

Uppercase

Lowercase

Digits

Special characters

# Requirements

Python 3.x

No external libraries required (uses built-in re module)

 Screenshots
 Program Running (Example Output)
<img width="1130" height="370" src="https://github.com/user-attachments/assets/c139cc65-c4ea-4982-b51d-0ad7aef88494" />

# Project Structure

root/

│── password-python.py
│── README.md

# How It Works

The script checks the password against:

Minimum 8 characters
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character
Prints detailed feedback

# Example Output

Strong Password Example
--- Password Strength Checker ---
Enter a password to check (or 'quit' to exit): Test@123

<img width="741" height="118" src="https://github.com/user-attachments/assets/859161b4-b189-4221-9356-50c85bb99038" />

Password Strength: STRONG
Your password meets all the required criteria.

<img width="590" height="104" src="https://github.com/user-attachments/assets/bad14373-d344-4c15-9d95-d64a9c5893a3" />

Weak Password Example
Password Strength: WEAK
Your password does NOT meet the required criteria. Please address the following:
- Password must contain at least one uppercase letter.
- Password must contain at least one digit.

<img width="741" height="118" src="https://github.com/user-attachments/assets/a51ba79c-155b-4d45-81f1-c0e6f375468f" />

# How to Run

Install Python
https://www.python.org/

Save the script as:

password-python.py


# Run:

python password-python.py

# 2 – Assignment: CPU Health Monitor (Python + psutil)

This project monitors CPU usage and prints alerts when usage exceeds a threshold.

Uses the psutil library to collect accurate CPU metrics.

# Requirements

Python 3.x
psutil library

# Install:
pip install psutil

Screenshot
<img width="359" height="480" src="https://github.com/user-attachments/assets/dc944298-4dfc-4593-9c13-f223d39f7c94" />

# Project Structure

root/
│── cpu_monitor.py
│── README.md

# Features

Real-time CPU monitoring
Threshold alert (default: 80%)
Adjustable interval
Clean console output

Handles Ctrl+C exit

# Example Output

Monitoring CPU usage... (Alert threshold: 80%)
Press Ctrl+C to stop monitoring.

Current CPU usage: 12%
Current CPU usage: 18%
Alert! CPU usage exceeds threshold: 85%
Current CPU usage: 20%

<img width="901" height="297" src="https://github.com/user-attachments/assets/03587402-0659-4ede-be09-a59ede3573a2" /> <img width="359" height="480" src="https://github.com/user-attachments/assets/30294efc-088f-4101-bc30-96c960db5d76" />

# How to Run

Install:
pip install psutil


Save the script as:
cpu_monitor.py


Run:
python cpu_monitor.py

# 3 – Assignment: Automating Configuration Management

This Python + Flask project:

 Parses .ini config files
 Converts them into JSON
 Exposes a REST API at /config
 Includes error handling
 Outputs config_output.json

# Features

Parse INI configuration files
Converts to JSON
Serves data through Flask API
Error handling for missing/invalid files
Lightweight, fast, reliable

# Project Structure

auto-config-mgmt/
│── app.py
│── config.ini
│── config_output.json
│── requirements.txt
│── README.md

# Sample config.ini

[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080

# How It Works

When running app.py:
Reads config.ini
Parses all sections
Converts data to dictionary
Saves JSON → config_output.json

Starts Flask server

GET /config returns parsed JSON

# Run the Application

1. Install dependencies
pip install -r requirements.txt

2. Start the app
python app.py

3. Access API

Open:

http://localhost:5000/config

<img width="1117" height="240" src="https://github.com/user-attachments/assets/25c9b34e-d983-4ec9-84ac-191e881d5a65" />

# Sample API Response
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

# Generated JSON File
<img width="669" height="367" src="https://github.com/user-attachments/assets/dfeeeb74-7dd1-4c9c-9111-96be801f16cc" />
