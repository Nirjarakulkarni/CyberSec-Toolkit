def scan_ports(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = [80, 22, 443, 8080]  # Add ports you want to scan
    scan_ports(target, ports)
