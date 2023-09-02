import socket
from colorama import init, Fore, Back, Style
import sys

init(autoreset=True)

try: 
    host = input("Host: ")
    port = input("Port: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host,int(port)))

    if result == 0:
        print("")
        print(f"Host Connection: {host}:{port} - " + Fore.GREEN + "OK".format(host, port))
    else:
        print("")
        print(f"Host Connection: {host}:{port} - " + Fore.RED + "ERR".format(host, port))

    sock.close()

    print("")
    print("https://github.com/Ethanol62")
    print("")
    input("Press Enter to exit...")

except Exception as e:
    print("")
    print("Invalid Host.")
    print("")
    print("https://github.com/Ethanol62")
    print("")
    input("Press Enter to exit...")