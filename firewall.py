from scapy.all import sniff, IP, TCP
import json
import logging

logging.basicConfig(filename='firewall_log.txt', level=logging.INFO, format='%(asctime)s %(message)s')

def load_rules():
    with open('rules.json') as f:
        return json.load(f)

def packet_callback(packet):
    rules = load_rules()
    try:
        if IP in packet:
            src_ip = packet[IP].src
            if src_ip in rules['blocked_ips']:
                logging.info(f"Blocked IP: {src_ip}")
                return

        if TCP in packet:
            dest_port = packet[TCP].dport
            if dest_port in rules['blocked_ports']:
                logging.info(f"Blocked Port: {dest_port}")
                return

    except Exception as e:
        logging.error(f"Error: {e}")

def start_firewall():
    sniff(prn=packet_callback, store=False)
