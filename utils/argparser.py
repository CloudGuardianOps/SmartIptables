import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Iptables Automation Script")
    parser.add_argument("--port", type=int, help="Port number to apply the rule")
    parser.add_argument("--direction", choices=['INPUT', 'OUTPUT'], help="Direction of traffic: INPUT or OUTPUT")
    parser.add_argument("--operation", choices=['allow', 'block'], help="Operation: allow or block")
    parser.add_argument("--help", action="store_true", help="Show this help message and exit")
    return parser.parse_args()

def print_help():
    parser = argparse.ArgumentParser(description="Iptables Automation Script")
    parser.print_help()
