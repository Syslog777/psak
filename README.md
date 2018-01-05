# PSAK  

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://nodesource.com/products/nsolid)
[![PSAK](https://img.shields.io/badge/PSAK-Open--Source-000000.svg)](https://github.com/Syslog777/psak/) [![GitHub forks](https://img.shields.io/github/forks/Syslog777/psak.svg)](https://github.com/Syslog777/psak/network) [![Github issues](https://img.shields.io/github/issues/Syslog777/psak.svg)](https://github.com/Syslog777/psak/issues) [![Python 3.6](https://img.shields.io/badge/Python-3.6-00BFFF.svg)](https://www.python.org/downloads/release/python-363/) [![License](https://img.shields.io/github/license/Syslog777/psak.svg)](https://github.com/Syslog777/psak/blob/Release-0.5/LICENSE)


### Introduction
PSAK is a project that targets a very specific audience

PSAK must be developed with inexperience in mind while maintaining functional dynamics. In other words, it should be operable by a "script kiddie" with strong reading comprehension, while a seasoned pen-tester should not become frustrated with overly limited options. However, it is not meant to fully replace original tools such as "nmap" or "metasploit". Such a project is beyond the scope of the tasks at hand.

PSAK must be modular and easily expandable. This is because the founding developers cannot possibly integrate every single Linux-based 
security-oriented application into it. In addition, to remain relevant means to expand and grow. PSAK will not be a project to invest in as a developer or a user if it does not evolve in a positive manner. Some tools stagnate in their development, causing users to shy away from them and developers to ignore them. Clearly, the ability to evolve is crucial to PSAK's relevancy in the years to come.


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
apt-get install tcpdump python3-crypto ipython3
apt-get install python3-tk
pip3 install netaddr
pip3 install psak
apt autoremove
```

## PSAK Framework
PSAK is simple to intergrate with, provided a intermediate
understanding of software develpment and Python 3.

PSAK Package  | Description
------------- | -------------
psak_src | holds the psak project
exploit_modules | holds each psak exploit module package
setup.py | psak installation file 

### Adding modules to psak
1. All code must closely follow the Google Python style at 
guide https://google.github.io/styleguide/pyguide.html
2. Always add a __init__.py file to python packages or they will not be added to the 
project installation package list
3. Specify a class for your exploit. This allows for a more dynamic system and adheres to
the psak framework
4. Place your module package in psak_src.exploit_modules
5. Do not add ```if __name__ == '__main__':
    main()``` to your module. That is solely for the main module located in psak_src.psak.py
6. In psak_src.psak add the following in terms of sudo code to append to psak's arguments
```python3
 if sys.argv[1] == '--your-module'
    from exploit_modules.your_packages.your_core.your_module import YourClass
    yourObject = yourObject()
    yourObject.main_function()
```
7. Use parser.add_argument('--your-module', help='help message') to add
a quick help message for your module

# TODO Tool intergration list

> Some of the tools that PSAK will implement will come from broken repositories. Before each tool is added, a stable fork of each individual tool will be required.
The majority of revisions will involve simple code such as updating shebangs and octal notation (Python).
  - [DHCPTakeover][dhcpTake]: a python module that sets up a dhcp server using Scapy
  - [MitmAP][mitmAP]: a python program to create a fake AP and sniff data
  - [SSH-mitm][sshMitm] SSH man-in-the-middle tool 
  - [TLS Prober][tlsprober]: a toolfor identifying the implementation in use by SSL/TLS servers
  - [Tplmap][tplMap]: exploit Code Injection and Server-Side Template Injection vulnerabilities
  - [WAFW00F][waf]: identifies and fingerprints Web Application Firewall (WAF) products.
  - [Finmap][finmap]: find, prepare, audit, exploit and even google automatically for local and remote file inclusion bugs within webapps in python
 - [NoSQLMap][NoSql]: audit as well as automate injection attacks while exploiting default configuration weaknesses in NoSQL databases and web applications using NoSQL
 - [Webscreenshot][webscrnshot]: A simple script to screenshot a list of websites, based on the url-to-image phantomjs script.
 - [Slowloris][slowloris]: an HTTP Denial of Service attack that affects threaded servers (Completed)
 - [DHCP-Starvation][DHCP-starvation]: DHCP starvation attack 
 - [Scapy-Attacks][Scapy-Attacks]: scapy based attack research (Intergration in progress)
 - [Ddos database][ddosd]: Ddos knowledge database ((Intergration in progress))
- [James' Security Blog][jsb]: A comprehensive list of attacks and their implementation


# List of types of attacks to add
`
Sync flood/ARP attack/Stealth Finish/ ICMP Ping flood/ UDP flood/ UDP Scan/ TCP Scan/Ping of Death/ Smurf attack/ TCP land/ UDP land/ ICMP land/ IP spoof/ Sync with Data/ SRC Sync flood/ SRC Stealth Finish/ SRC ICMP flood/ SRC UDP flood/ Echo char gen/ Port scan/ SRC TCP connection overflow/ SRC UDP connection overflow/ TCPUDP connection overflow/ TCP connection overflow/ UDP connection overflow/ TCP UDP connection overflow/Ping sweep
`

# Project payload list
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

   