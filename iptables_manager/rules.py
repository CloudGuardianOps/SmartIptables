def create_rule(port, direction, action):
    return f"iptables -A {direction.upper()} -p tcp --dport {port} -j {action.upper()}"
