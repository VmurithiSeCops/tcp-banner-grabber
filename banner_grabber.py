#!/usr/bin/env python3
"""
TCP Banner Grabber Utility
Author: Victor Murithi (VmurithiSecOps)
Description: Connects to a target IP and port via sockets to extract service banners.
"""

import sys
import socket

def grab_banner(ip, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0) # 3-second timeout to prevent hanging
        
        # Connect to target
        print(f"\n[*] Connecting to {ip}:{port}...")
        s.connect((ip, int(port)))
        
        # Try receiving data (banner)
        banner = s.recv(1024).decode().strip()
        
        if banner:
            print(f"[+] Banner successfully retrieved:\n    -> {banner}")
        else:
            print("[-] Connected, but no banner received (service silent).")
            
        s.close()
        
    except socket.timeout:
        print(f"[!] Connection timed out while reaching {ip}:{port}.")
    except ConnectionRefusedError:
        print(f"[!] Connection refused. Port {port} appears closed or filtered.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 banner_grabber.py <target_ip> <port>")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    target_port = sys.argv[2]
    
    grab_banner(target_ip, target_port)
