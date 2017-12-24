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

"""
All arguments:
--mitm: total runtime in seconds
-iface: Interface to use for network activity
-vIP: IP of the victim
-gIP: IP of the gate/ node that the victim
-gPN: Port number of the gate to connect to
"""


class MitmArgs:

    def __init__(self, parser):
        parser.add_argument('-iface', '--interface', dest="interface",
                            required=True, type=str,
                            help="interface to use for network activity")

        parser.add_argument('-vIP', '--victim-ip', help="IP of the victim",
                            dest="victim_ip", required=True, type=str, default="127.0.0.1")

        parser.add_argument('-gIP', '--gate-ip', dest="gate_ip", required=True, type=str,
                            default="127.0.0.1",
                            help="IP of the gate/ node that the victim is connecting to")

        parser.add_argument('-gPN', '--gate_port_number',
                            help="Port number of the gate to connect to", dest="gate_port_number",
                            required=False, type=int)
        self.args = parser.parse_args()
        self.interface = self.args.interface
        self.victim_ip = self.args.victim_ip
        self.gate_ip = self.args.gate_ip
        self.gate_port_number = self.args.gate_port_number
        # self.victim_port_number = self.args.victim_port_number

    def get_interface(self):
        return self.interface

    def get_victim_ip(self):
        return self.victim_ip

    def get_gate_ip(self):
        return self.gate_ip

    def get_gate_port_number(self):
        return self.gate_port_number

    def get_victim_port_number(self):
        return self.victim_port_number

    def get_runtime(self):
        return self.args.mitm
