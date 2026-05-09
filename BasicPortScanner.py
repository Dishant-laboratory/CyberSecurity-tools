import socket

# set localhost automatically
host = "localhost"

# get port range from user
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# loop through ports
for port in range(start_port, end_port + 1):
    # create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # try to connect
    result = sock.connect_ex((host, port))
    
    # check if port responded
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    # close socket
    sock.close()