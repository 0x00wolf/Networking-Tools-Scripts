import socket
import sys

# Select number of ports to scan
port_range = 1024

def scan_host(ip):
    print(f'[*] Starting TCP port scan on host {ip}')
    tcp_scan(ip)
    print(f'[+] TCP scan on host {ip} complete')

def network_scan(network):
    print('[*] Starting TCP port scan on network %s.0' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        scan_host(ip)
    print(f'[+] TCP scan on network {network}.0 complete')

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
    network = input("Network addr(X.X.X):\n>> ")
    network_scan(network)
    sys.exit() 

main()
