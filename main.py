import socket
import argparse

parser = argparse.ArgumentParser(description='Simple TCP Port Scanner')
parser.add_argument('host', help='Target host (IP or domain)')
parser.add_argument('-p', '--ports', default='1-1024', help='Port range, e.g. 1-1024')
args = parser.parse_args()

host = args.host
port_range = args.ports
if '-' in port_range:
    start_port, end_port = [int(x) for x in port_range.split('-')]
else:
    start_port = end_port = int(port_range)

print(f"Scanning {host} ports {start_port}-{end_port} ...")

for port in range(start_port, end_port + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        try:
            s.connect((host, port))
        except (socket.timeout, ConnectionRefusedError):
            continue
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")
            continue
        print(f"[+] Port {port} is OPEN")
