# psak  

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://nodesource.com/products/nsolid)
[![psak](https://img.shields.io/badge/PSAK-Open--Source-000000.svg)](https://github.com/Syslog777/psak/) [![GitHub forks](https://img.shields.io/github/forks/Syslog777/psak.svg)](https://github.com/Syslog777/psak/network) [![Github issues](https://img.shields.io/github/issues/Syslog777/psak.svg)](https://github.com/Syslog777/psak/issues) [![Python 3.6](https://img.shields.io/badge/Python-3.6-00BFFF.svg)](https://www.python.org/downloads/release/python-363/) [![License](https://img.shields.io/github/license/Syslog777/psak.svg)](https://github.com/Syslog777/psak/blob/Release-0.5/LICENSE)


### Project Objectives
1. Make pentesting easier
2. Make pentesting simpler
3. Make pentesting make sense
  
### Limitations
- Development time is the greatest limitation in terms of psak
 
 ### PSAK Framework
PSAK is simple to intergrate with, provided a intermediate
understanding of software develpment and Python 3. Just fork the
project, add you module and then submit a pull request.

> Simply study the existing code and follow the style you sense.

PSAK Package  | Description
------------- | -------------
psak_src | holds the psak project
exploit_modules | holds each psak exploit module package
setup.py | psak installation file 


 
### Installation Instructions
Copy and paste the following into your terminal as user root
to install psak:
```
apt-get update
apt-get upgrade
apt-get install python3
apt-get install python3-pip
apt-get install pip
apt-get install pip3
pip3 install --upgrade pip
pip3 install setuptools
pip3 install ipython
pip3 install graphviz
pip3 install cryptography
pip3 install scapy-python3
pip3 install matplotlib
pip3 install networkx
pip3 install pyx
pip3 install latex
pip3 install docopt
pip3 install netaddr
apt-get install tcpdump python3-crypto ipython3
apt-get install python3-tk
#Basic penetration utils
apt-get install airodump-ng
apt-get install aireplay-ng
apt-get install ip
apt-get install arping
# Finish up
pip3 install psak
apt autoremove
```

### Networking Research
  - [Scapy-Attacks][Scapy-Attacks]: scapy based attack research (Intergration in progress)
  - [Ddos database][ddosd]: Ddos knowledge database ((Intergration in progress))
  - [James' Security Blog][jsb]: A small comprehensive list of attacks and their implementation
  - [Wifi ID's][juniper]: Understanding the network terms SSID, BSSID, and ESSID 
  - [Deauthentication Attack][deauth]: how to create and send 
  wireless deauthentication packets using python and scapy

# Network Attacks
##### Basic Brute-Force Connectionless Attacks
- UDP Flood
- ICMP Flood
- IGMP Flood
##### Complex Brute-Force Connectionless Attacks
- Smurf Attacks
- Fraggle Attacks
- DNS Amplification
##### Basic Brute-Force Connection-Oriented Attacks
- TCP-SYN Flood
- TCP-RST Attack
- TCP-PSH+ACK Attack

#### External Sources  

##### Project payload list
> A list of frameworks to use to design deliverable payloads for penetration testers. 
- [PowerSploit][powersploit]: PowerSploit is a collection of Microsoft PowerShell modules that can be used to aid penetration testers during all phases of an assessment.
- [Offensive-Security Exploit database][exploit-database]: an official repository of The Exploit Database, a project sponsored by Offensive Security
- [DHCPig][dhcpig]: initiates an advanced DHCP exhaustion attack

   [ddosd]: <https://security.radware.com/ddos-knowledge-center/ddospedia/>
   [dhcpTake]: <https://github.com/david415/dhcptakeover>
   [powersploit]: <https://github.com/PowerShellMafia/PowerSploit>
   [waf]: <https://github.com/EnableSecurity/wafw00f>
   [tplMap]: <https://github.com/epinna/tplmap>
   [mitmAP]: <https://github.com/xdavidhu/mitmAP>
   [sshMitm]: <https://github.com/jtesta/ssh-mitm>
   [tlsprober]: <https://github.com/WestpointLtd/tls_prober>
   [finmap]: <https://github.com/kurobeats/fimap>
   [NoSql]: <https://github.com/codingo/NoSQLMap>
   [webscrnshot]: <https://github.com/maaaaz/webscreenshot>
   [exploit-database]: <https://github.com/offensive-security/exploit-database>
   [dhcpig]: <https://github.com/kamorin/DHCPig>
   [slowloris]: <https://github.com/gkbrk/slowloris>
   [DHCP-starvation]: <http://cabeggar.github.io/2016/02/21/DHCP-starvation-with-ScaPy/>
   [Scapy-Attacks]: <http://www.secdev.org/conf/scapy_csw05.pdf>
   [jsb]: <http://jamesdotcom.com/?p=264>
   [juniper]: <https://www.juniper.net/documentation/en_US/junos-space-apps/network-director2.0/topics/concept/wireless-ssid-bssid-essid.html>
   [deauth]: <http://www.bitforestinfo.com/2017/06/how-to-create-and-send-wireless-deauthentication-packets-using-python-and-scapy.html>
