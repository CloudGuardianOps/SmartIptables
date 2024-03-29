import os
from .rules import create_rule

def allow_port(port, direction):
    rule = create_rule(port, direction, "ACCEPT")
    os.system(rule)

def block_port(port, direction):
    rule = create_rule(port, direction, "DROP")
    os.system(rule)
