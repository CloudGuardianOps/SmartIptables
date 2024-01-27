import subprocess

def allow_port(port, direction):
    direction_flag = "-I INPUT" if direction == "in" else "-I OUTPUT"
    subprocess.run(f"sudo iptables {direction_flag} -p tcp --dport {port} -j ACCEPT", shell=True)

def block_port(port, direction):
    direction_flag = "-I INPUT" if direction == "in" else "-I OUTPUT"
    subprocess.run(f"sudo iptables {direction_flag} -p tcp --dport {port} -j DROP", shell=True)
