Python Port Scanner
A fast, multi-threaded Python tool to scan open ports on a target IP address and within a specified port range. Developed as part of the Hack Secure Cybersecurity Internship (Red Teaming, April 2025 Batch).

🚩 Overview
This project is a command-line port scanner that allows users to:

Scan a target host for open TCP ports.

Select from common port ranges or specify a custom range.

Get real-time feedback on open ports.

Benefit from optimized multi-threading for faster scanning.

✨ Features
Input validation: Ensures only valid IP addresses and port ranges are accepted.

Port range options: Choose from well-known, registered, dynamic/private, all, or custom port ranges.

Prioritizes common ports: Scans the most frequently used ports first for quicker results.

Multi-threaded scanning: Utilizes threading for efficient and fast port scanning, even over large ranges.

User-friendly output: Displays open ports as they are found and summarizes results at the end.

🛠️ Installation
Clone the repository:

bash
git clone https://github.com/yourusername/python-port-scanner.git
cd python-port-scanner
(Optional) Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
No external dependencies required.
The script uses only Python’s standard library.

▶️ Usage
Run the script using Python 3:

bash
python HackSecure_PulasthiRanabahu_EHP.py
Follow the prompts:

Enter the target IP address (e.g., 192.168.1.1).

Select a port range option (well-known, registered, dynamic/private, all, or custom).

The scanner will display open ports as they are detected and provide a summary at the end.

📋 Example Output
text
============================================================
PYTHON PORT SCANNER
============================================================

Enter the target IP address to scan.
Examples: 192.168.1.1, 10.0.0.1, 127.0.0.1 (localhost)

Target IP address: 45.33.32.156

Select port range option:
1. Well-known ports (1-1023)
2. Registered ports (1024-49151)
3. Dynamic/Private ports (49152-65535)
4. All ports (1-65535)
5. Custom range

Enter option (1-5): 1

Scanning 45.33.32.156 for open ports from 1 to 1023...
Scan started at: 2025-04-24 01:11:04
------------------------------------------------------------
Port 22 is open
Port 80 is open

Scan completed at: 2025-04-24 01:11:04
------------------------------------------------------------
Found 2 open ports on 45.33.32.156:
Port 22 is open
Port 80 is open
📦 Project Structure
text
python-port-scanner/
├── HackSecure_PulasthiRanabahu_EHP.py
├── README.md
📚 Internship Context
This project fulfills the "Basic Port Scanner" requirement for the Hack Secure Cybersecurity Internship (Red Teaming). The goal is to demonstrate practical skills in network reconnaissance and Python scripting.

🤝 Acknowledgements
Developed by R.A.M.P Ranabahu for the Hack Secure Internship, April 2025 Batch.

Thanks to the Hack Secure team for guidance and support.

Let’s make the digital world safer, one scan at a time!
