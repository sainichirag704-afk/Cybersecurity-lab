import socket

# Function to scan ports
def scan_ports(target, ports):
    print(f"\nScanning target: {target}\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            else:
                print(f"❌ Port {port} is CLOSED")
            sock.close()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Couldn't connect to server.")
            break

if __name__ == "__main__":
    target = input("Enter the target IP or hostname: ")
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]  # Common ports
    scan_ports(target, ports_to_scan)
