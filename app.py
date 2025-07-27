from flask import Flask, render_template, request, redirect
import json
import os
from threading import Thread
from firewall import start_firewall

app = Flask(__name__)
RULES_FILE = 'rules.json'
LOG_FILE = 'firewall_log.txt'

def load_rules():
    with open(RULES_FILE) as f:
        return json.load(f)

def save_rules(rules):
    with open(RULES_FILE, 'w') as f:
        json.dump(rules, f, indent=4)

def get_last_log_lines(n=3):
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as file:
        lines = file.readlines()
        return lines[-n:]

@app.route('/')
def index():
    rules = load_rules()
    logs = get_last_log_lines()
    return render_template('index.html', rules=rules, logs=logs)

@app.route('/add_ip', methods=['POST'])
def add_ip():
    ip = request.form['ip']
    rules = load_rules()
    if ip and ip not in rules['blocked_ips']:
        rules['blocked_ips'].append(ip)
        save_rules(rules)
    return redirect('/')

@app.route('/add_port', methods=['POST'])
def add_port():
    port = request.form['port']
    try:
        port = int(port)
        rules = load_rules()
        if port not in rules['blocked_ports']:
            rules['blocked_ports'].append(port)
            save_rules(rules)
    except:
        pass
    return redirect('/')

@app.route('/start')
def start():
    Thread(target=start_firewall, daemon=True).start()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
