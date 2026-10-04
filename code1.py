import netmiko
import logging
import os
from getpass import getpass
from netmiko import ConnectHandler

class Router:
    def __init__(self,address):
        self.address=address
        pass
    
    
    def connection(self):
        sw1={
            "device_type":"cisco_ios",
            "ip":self.address,
            "username":"admin",
            "password":"Pass@123"
        }
        
        self.connection=ConnectHandler(**sw1)
        
    def prompt(self):
        prompt=self.connection.find_prompt()
        print (prompt)
    
        
    def command(self,command):
        
        output=self.connection.send_command(command)
        return output
        # print(output)


# with open("device.txt","r") as file:
#     for device in file:
# address = input("Enter the router IP address: ")
# router = Router(address)
# router.connection()
# router.prompt()
# output = router.command(input("Enter the command : "))
# print(output)
            