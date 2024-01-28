from utils.argparser import parse_args
from iptables_manager import actions
from honeypot import server

def main():
    args = parse_args()

    if args.operation == 'allow':
        actions.allow_port(args.port, args.direction)
    elif args.operation == 'block':
        actions.block_port(args.port, args.direction)
    elif args.operation == 'start_honeypot':
        server.start_honeypot(args.port)
    elif args.operation == 'stop_honeypot':
        server.stop_honeypot()

if __name__ == "__main__":
    main()
