#!/usr/bin/python3

import sys


def interrupt():
    print("\n[*] User requested shutdown")
    print("Exiting....")
    sys.exit(1)


def get_interface():
    try:
        interface = input("[*] Enter desired interface: ")
        return interface
    except KeyboardInterrupt:
        interrupt()


def get_victimIP():
    try:
        victimIP = input("[*] Enter victim IP: ")
        return victimIP
    except KeyboardInterrupt:
        interrupt()


def get_gateIP():
    try:
        gateIP = input("[*] Enter router IP: ")
        return gateIP
    except KeyboardInterrupt:
        interrupt()


def get_gate_port_number():
    try:
        portNum = input("[*] Enter gate port number: ")
        return portNum
    except KeyboardInterrupt:
        interrupt()
