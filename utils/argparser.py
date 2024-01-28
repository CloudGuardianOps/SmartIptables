import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Iptables Automation and Honeypot Script")
    parser.add_argument("--port", type=int, help="Port number for iptables rule or honeypot")
    parser.add_argument("--direction", choices=['INPUT', 'OUTPUT'], help="Direction of traffic: INPUT or OUTPUT", default="INPUT")
    parser.add_argument("--operation", choices=['allow', 'block', 'start_honeypot', 'stop_honeypot'], help="Operation: allow, block, start honeypot, or stop honeypot")
    return parser.parse_args()

def print_help():
    parser = argparse.ArgumentParser(description="Iptables Automation and Honeypot Script")
    parser.print_help()
