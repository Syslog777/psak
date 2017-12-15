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


class MitmArgs:

    def __init__(self, parser):
        self.parser = parser
        self.parser.add_argument('-iface', '--interface', required=True,
                                 help="Interface to use for network activity")
        self.parser.add_argument('-vIP', '--victim-ip', required=True,
                                 help="IP of the victim")
        self.parser.add_argument('-gIP', '--gate_ip', required=True,
                                 help="IP of the gate/ node that the victim"
                                      "is connecting to")
        self.parser.add_argument('-gPN', '--gate_port_number', required=True,
                                 help="Port number of the gate to connect to",
                                 type=int)
        self.args = self.parser.parse_args()

    def get_interface(self):
        if not self.parser.interface:
            return None
        return self.parser.interface

    def get_victim_ip(self):
        if not self.parser.victim_ip:
            return None
        return self.parser.victim_ip

    def get_gate_ip(self):
        if not self.parser.gate_ip:
            return None
        return self.parser.gate_ip

    def get_gate_port_number(self):
        if not self.parser.gate_port_number:
            return None
        return self.parser.gate_port_number

    def get_victim_port_number(self):
        if not self.parser.victim_port_number:
            return None
        return self.parser.victim_port_number
