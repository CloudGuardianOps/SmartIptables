# main.py
from utils.argparser import parse_args
from iptables_manager import actions
from honeypot.server import Honeypot 

def main():
    args = parse_args()

    if args.operation == 'allow':
        actions.allow_port(args.port, args.direction)
    elif args.operation == 'block':
        actions.block_port(args.port, args.direction)
    elif args.operation == 'start_honeypot':
        honeypot = Honeypot(args.port) 
        honeypot.start() 
    elif args.operation == 'stop_honeypot':
        honeypot = Honeypot(args.port) 
        honeypot.stop()
        pass

if __name__ == "__main__":
    main()
