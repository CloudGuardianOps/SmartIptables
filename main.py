from iptables_manager import actions
from honeypot import server
from utils import argparser

def main():
    args = argparser.parse_args()

    if args.help:
        argparser.print_help()
    elif args.operation in ['allow', 'block']:
        if args.operation == 'allow':
            actions.allow_port(args.port, args.direction)
        elif args.operation == 'block':
            actions.block_port(args.port, args.direction)
    elif args.operation in ['start_honeypot', 'stop_honeypot']:
        if args.operation == 'start_honeypot':
            server.start_honeypot(args.port)
        elif args.operation == 'stop_honeypot':
            server.stop_honeypot()

if __name__ == "__main__":
    main()
