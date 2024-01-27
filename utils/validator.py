def validate_port(port):
    try:
        port = int(port)
        return 0 <= port <= 65535
    except ValueError:
        return False
