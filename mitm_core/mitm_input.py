#!/usr/bin/env python3
"""
 Copyright (c) 2017, Syslog777

 All rights reserved.

 Redistribution and use in source and binary forms, with or without modification,
 are permitted provided that the following conditions are met:

     * Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.
     * Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.
     * Neither the name of Desktop nor the names of its contributors
       may be used to endorse or promote products derived from this software
       without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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
