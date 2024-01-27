import sys
from iptables_manager import actions
from utils import validator, logger

def main():
    if len(sys.argv) != 4:
        logger.log("Usage: main.py <port> <direction> <action>")
        sys.exit(1)

    port, direction, action = sys.argv[1], sys.argv[2], sys.argv[3]

    if not validator.validate_port(port):
        logger.log(f"Invalid port: {port}")
        sys.exit(1)

    if direction not in ["in", "out"]:
        logger.log(f"Invalid direction: {direction}")
        sys.exit(1)

    if action not in ["allow", "block"]:
        logger.log(f"Invalid action: {action}")
        sys.exit(1)

    if action == "allow":
        actions.allow_port(port, direction)
    else:
        actions.block_port(port, direction)

    logger.log(f"Action {action} applied on port {port} for {direction} traffic.")

if __name__ == "__main__":
    main()
