##################################
## This is Automation Project  ##
##################################

import netmiko

from getpass import getpass
from netmiko import ConnectHandler
from code1 import Router
from logg import logger

import fastapi
from fastapi import FastAPI

app=FastAPI()



@app.get("/")
def greet():
    return "HELLO WORLD this is my Automation Project "

# @app.post("/command")
# def command(address: str):
#     return Router(address)
 
# This if for L1   

@app.post("/L1user")
def command(address: str,L1command:str):

    router = Router(address)

    try:
        router.connection()

        output = router.command(L1command)

        return {
            "router": address,
            "output": output
        }

    except Exception as e:
        return {
            "router": address,
            "error": str(e)
        }

    finally:
        print("Congrats")
