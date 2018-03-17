psak

￼

￼

￼

￼

￼

￼

Project Objectives
1. Make pentesting easier
2. Make pentesting simpler
3. Make pentesting make sense

Contribute

Write a TCP-RST Attack using scapy

Limitations • Development time is the greatest limitation in terms of psak

PSAK Framework

PSAK is simple to intergrate with, provided a intermediate understanding of software develpment and Python 3. Just fork the project, add you module and then submit a pull request.

Simply study the existing code and follow the style you sense.

￼￼￼￼￼

Installation Instructions

Copy and paste the following into your terminal as user root to install psak:

apt-get update apt-get upgrade apt-get install python3 apt-get install python3-pip apt-get install pip apt-get install pip3 pip3 install --upgrade pip pip install --upgrade google-api-python-client pip3 install setuptools pip3 install ipython pip3 install graphviz pip3 install cryptography pip3 install scapy-python3 pip3 install matplotlib pip3 install networkx pip3 install pyx pip3 install latex pip3 install docopt pip3 install netaddr pip3 install requests apt-get install tcpdump python3-crypto ipython3 apt-get install python3-tk #Basic penetration utils apt-get install airodump-ng apt-get install aireplay-ng apt-get install ip apt-get install arping

Finish up

pip3 install psak apt autoremove

Networking Research • Scapy-Attacks : scapy based attack research (Intergration in progress) • Ddos database : Ddos knowledge database ((Intergration in progress)) • James' Security Blog : A small comprehensive list of attacks and their implementation • Wifi ID's : Understanding the network terms SSID, BSSID, and ESSID • Deauthentication Attack : how to create and send wireless deauthentication packets using python and scapy

Network Attacks

If the feature has not been marked completed, you can contribute by writing an implementation of it by attack type

Basic Brute-Force Connectionless Attacks • UDP Flood • ICMP Flood • IGMP Flood

Complex Brute-Force Connectionless Attacks • Smurf Attacks • Fraggle Attacks • DNS Amplification

Basic Brute-Force Connection-Oriented Attacks • TCP-SYN Flood (Complete) • TCP-RST Attack • TCP-PSH+ACK Attack

Project payload list

A list of frameworks to use to design deliverable payloads for penetration testers.

• PowerSploit : PowerSploit is a collection of Microsoft PowerShell modules that can be used to aid penetration testers during all phases of an assessment. • Offensive-Security Exploit database : an official repository of The Exploit Database, a project sponsored by Offensive Security • DHCPig : initiates an advanced DHCP exhaustion attack