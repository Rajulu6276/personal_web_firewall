# personal_web_firewall

**Firewall Rule Management & Intrusion Prevention Web App**
**A Python-Flask-based web interface** for managing firewall rules and monitoring suspicious traffic. This application allows users to block IP addresses and ports, monitor live logs, and initiate a background firewall engine that simulates rule enforcement.

**📌 Features**
•	✅ Web-based GUI using Flask

•	✅ Add & manage blocked IP addresses

•	✅ Add & manage blocked ports

•	✅ View real-time firewall logs (last 3 entries on dashboard)

•	✅ Persistent rule storage using JSON

•	✅ Background firewall engine to simulate active blocking

•	✅ Secure and lightweight local server

•	✅ Automatic log updates

•	✅ Extensible design for real-world firewall integration

**🛠️ Tools & Technologies Used**
•	Python 3.x
•	Flask – lightweight web framework
•	Threading – to run firewall logic in the background
•	JSON – rule storage
•	HTML/CSS – front-end interface
•	firewall.py – core rule processor (custom module)
•	rules.json – stores all active blocked rules
•	firewall_log.txt – logs blocked access attempts
🚀 Installation
```bash
git clone https://github.com/Rajulu6276/firewall-web-app.git
cd firewall-web-app
pip install -r requirements.txt
python app.py
```
**🧪 How It Works**
**Web Interface**: Flask UI serves a dashboard to view and manage rules.

**Rules Management**: Users can add IP addresses or port numbers to block. These are saved to rules.json.


**Firewall Engine (Background Task)**: When "Start Firewall" is clicked, a background thread runs from firewall.py, simulating detection of traffic and enforcing blocks by logging attempts.


**Logging**: Detected attempts to blocked ports or IPs are logged in firewall_log.txt. Latest 3 logs appear on the web UI.


📄 Sample Log Output
Blocked Port: 443
Blocked IP: 8.8.8.8
Blocked Port: 80
📝 View complete logs in: firewall_log.txt
**🧾 Sample Rule File (rules.json)**
{
    "blocked_ips": [
        "192.168.1.100",
        "8.8.8.8"
    ],
    "blocked_ports": [
        80,
        443,
        21
    ]
}


**🔒 Security & Ethics Disclaimer**
This project is for educational and simulation purposes only. It does not enforce real firewall rules at the system/network level. For production environments, consider integrating with tools like iptables, ufw, or enterprise-grade firewalls.
🤝 Contributing
1.	Fork the repository
2.	Create a new feature branch
3.	Commit your changes
4.	Push to your fork
5.	Submit a Pull Request

**🙏 Acknowledgments**
•	Flask community for the lightweight yet powerful web framework
•	Open-source ecosystem for threading, JSON handling, and debugging tools
•	Inspired by real-world firewall rule sets and IDS/IPS logic
