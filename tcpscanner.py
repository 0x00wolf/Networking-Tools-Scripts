import socket
import sys

# Select number of ports to scan
port_range = 1024

def scan_host(ip):
    print(f'[*] Starting TCP port scan on host {ip}')
    tcp_scan(ip)
    print(f'[+] TCP scan on host {ip} complete')

def tcp_scan(ip):
    for port in range(port_range):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print(f'[+] {ip}:{port}/TCP Open')
                tcp.close()
        except Exception:
            pass
            

def main():
    socket.setdefaulttimeout(0.01)
    ip = input("IP ADDRESS: ")
    scan_host(ip)
    sys.exit()

main()
