#!/usr/bin/python3
from scapy.all import *


class MitmShark:
    def __init__(self, filter):
        self.filter = filter

    def arp_display(self, pkt):
        if pkt[ARP].op == 1:  # who-has (request)
            return 'Request: {} is asking about {}'.format(pkt[ARP].psrc, pkt[ARP].pdst)
        if pkt[ARP].op == 2:  # is-at (response)
            return '*Response: {} has address {}'.format(pkt[ARP].hwsrc, pkt[ARP].psrc)

    def mac_summary(self):
        return sniff(prn=lambda pkt: 'Packet from {} going to --> {}'.format(pkt.src, pkt.dst))

    def arp_summary(self):
        sniff(prn=lambda pkt: self.arp_display(pkt), filter=self.filter, store=0)

    def hexdump_summary(self):
        dump = sniff()
        return dump.hexdump()

    def full_summary(self):
        tshark()


ob = MitmShark("arp")
# ob.arp_summary()
ob.hexdump_summary()
