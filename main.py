from iptables_manager import actions
from utils import argparser

def main():
    args = argparser.parse_args()

    if args.help:
        argparser.print_help()
    else:
        if args.operation == 'allow':
            actions.allow_port(args.port, args.direction)
        elif args.operation == 'block':
            actions.block_port(args.port, args.direction)

if __name__ == "__main__":
    main()
