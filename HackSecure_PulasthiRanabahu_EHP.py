import socket
import sys
import ipaddress
from datetime import datetime
import concurrent.futures
import queue
import threading

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port_range(start_port, end_port):
    try:
        start_port = int(start_port)
        end_port = int(end_port)
        
        if 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port:
            return True, start_port, end_port
        else:
            return False, None, None
    except ValueError:
        return False, None, None

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)  # Further reduced timeout for faster scanning
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None

def worker(ip, port_queue, open_ports, print_lock):
    while not port_queue.empty():
        try:
            port = port_queue.get_nowait()
        except queue.Empty:
            break
        
        result = scan_port(ip, port)
        if result is not None:
            open_ports.append(result)
            with print_lock:
                print(f"Port {result} is open")
        
        port_queue.task_done()

def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip} for open ports from {start_port} to {end_port}...")
    print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    open_ports = []
    port_queue = queue.Queue()
    print_lock = threading.Lock()
    
    # Prioritize common ports first for faster results
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    # Add common ports first if they're in the range
    for port in common_ports:
        if start_port <= port <= end_port:
            port_queue.put(port)
    
    # Add remaining ports in the range
    for port in range(start_port, end_port + 1):
        if port not in common_ports:
            port_queue.put(port)
    
    # Determine optimal number of threads based on range size
    range_size = end_port - start_port + 1
    if range_size < 100:
        num_threads = range_size
    elif range_size < 1000:
        num_threads = 200
    else:
        num_threads = 500  # Use more threads for larger ranges
    
    # Create and start worker threads
    threads = []
    for _ in range(min(num_threads, range_size)):
        thread = threading.Thread(target=worker, args=(ip, port_queue, open_ports, print_lock))
        thread.daemon = True
        thread.start()
        threads.append(thread)
    
    # Wait for all ports to be processed
    port_queue.join()
    
    # Sort open ports for display
    open_ports.sort()
    return open_ports

def main():
    print("=" * 60)
    print("PYTHON PORT SCANNER")
    print("=" * 60)
    
    # Instructions for IP address input
    print("\nEnter the target IP address to scan.")
    print("Examples: 192.168.1.1, 10.0.0.1, 127.0.0.1 (localhost)")
    
    # Get IP address with validation
    while True:
        ip = input("\nTarget IP address: ")
        if validate_ip(ip):
            break
        else:
            print("Error: Invalid IP address format. Please try again.")
    
    # Instructions for port range with options
    print("\nSelect port range option:")
    print("1. Well-known ports (1-1023)")
    print("2. Registered ports (1024-49151)")
    print("3. Dynamic/Private ports (49152-65535)")
    print("4. All ports (1-65535)")
    print("5. Custom range")
    
    # Get port range option
    while True:
        try:
            option = int(input("\nEnter option (1-5): "))
            if option == 1:
                start_port, end_port = 1, 1023
                break
            elif option == 2:
                start_port, end_port = 1024, 49151
                break
            elif option == 3:
                start_port, end_port = 49152, 65535
                break
            elif option == 4:
                start_port, end_port = 1, 65535
                break
            elif option == 5:
                print("\nEnter custom port range (1-65535)")
                while True:
                    start_input = input("Starting port: ")
                    end_input = input("Ending port: ")
                    valid, start_port, end_port = validate_port_range(start_input, end_input)
                    if valid:
                        break
                    else:
                        print("Error: Invalid port range. Ports must be between 1-65535 and start_port <= end_port")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Scan ports
    open_ports = scan_ports(ip, start_port, end_port)
    
    # Display results summary
    print("\nScan completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 60)
    
    if open_ports:
        print(f"\nFound {len(open_ports)} open ports on {ip}:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print(f"\nNo open ports found on {ip} in the range {start_port}-{end_port}.")

if __name__ == "__main__":
    main()
