import socket

target_host = "apache.org"
target_port = 80

def GetHttpCodeFromResponse(response):
    httpCode = response[9:12]
    # print(httpCode) # prints the 3 digit HTTP response code (200/404 etc.)
    return httpCode

# Using dirb small wordlist
wordlistFile = open("/usr/share/wordlists/dirb/small.txt",'r')
print("Looking for directories of: " + target_host)

# Iterate over each line (entry) in the wordlist
for wordlistEntry in wordlistFile:

    # Create a socket object
    client = socket.create_connection((target_host,target_port))
    request_header = "GET /" + wordlistEntry[:-1] + "/ HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n"

    # Send some data
    # TODO: Make non-blocking, multi-threaded
    
    client.send(request_header)

    # Receive response and display
    response = client.recv(1024) # 1024 byte buffer for response

    if (GetHttpCodeFromResponse(response) == '200'):
        print("[+] FOUND valid directory: /" + wordlistEntry[:-1])

wordlistFile.close()
