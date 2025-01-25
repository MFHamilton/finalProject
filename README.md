Ransomware Simulation Script

⚠️ Disclaimer

This project is for educational purposes only. The code provided here is intended to demonstrate and study techniques used in cybersecurity, encryption, and ethical hacking. DO NOT use this code for malicious purposes or to harm others' systems. Unauthorized use of this code could result in legal consequences.

📋 Project Description

This script is a ransomware simulation written in Python. It demonstrates how file encryption, decryption, and system-level manipulation can be achieved programmatically. Additionally, it includes a graphical user interface (GUI) using tkinter to simulate the interaction between the attacker and the victim.

The script performs the following actions:

Encrypts specific file types in the current directory and its subdirectories.

Saves the encryption key in a file (key.key).

Displays a GUI with a ransom message demanding payment.

Offers the victim options to pay or refuse, which can trigger further actions such as file decryption or a simulated system crash.

🔑 Features

Encryption and Decryption:

Uses the cryptography library with Fernet for symmetric encryption.

Encrypts files with extensions: .txt, .pdf, .png, .jpeg, and .jpg.

Stores encrypted files in Base64 format.

Graphical User Interface:

Simulates a ransomware GUI with messages and user interactions.

Simulated Blue Screen of Death (BSOD):

Uses Windows APIs via ctypes to simulate a system crash in response to user actions.
