# PSAK  

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://nodesource.com/products/nsolid)
[![GitHub forks](https://img.shields.io/github/forks/Syslog777/psak.svg)](https://github.com/Syslog777/psak/network) [![Python 3.6](https://img.shields.io/badge/Python-3.6-00BFFF.svg)](https://www.python.org/downloads/release/python-363/) [![License](https://img.shields.io/dub/l/vibe-d.svg)](https://github.com/Syslog777/psak/)



PSAK is a project that targets a very specific audience - Kali Linux users who are interested in pen-testing. While the target OS is Kali Linux, other Linux OS users are welcome to use our software. However, due to the myriad of bugs caused by "other" Linux operating systems, PSAK developers will only support Kali Linux distributions.

PSAK must be developed with inexperience in mind while maintaining functional dynamics. In other words, it should be operable by a "script kiddie" with strong reading comprehension, while a seasoned pen-tester should not become frustrated with overly limited options. However, it is not meant to fully replace original tools such as "nmap" or "metasploit". Such a project is beyond the scope of the tasks at hand.

PSAK must be modular and easily expandable. This is because the founding developers cannot possibly integrate every single Linux-based 
security-oriented application into it. In addition, to remain relevant means to expand and grow. PSAK will not be a project to invest in as a developer or a user if it does not evolve in a positive manner. Some tools stagnate in their development, causing users to shy away from them and developers to ignore them. Clearly, the ability to evolve is crucial to PSAK's relevancy in the years to come.



# Project intergration list

> Some of the tools that PSAK will implement will come from broken repositories. Before each tool is added, a stable fork of each individual tool will be required.
The majority of revisions will involve simple code such as updating shebangs and octal notation (Python).

  - [MitmAP][mitmAP]: a python program to create a fake AP and sniff data
  - [SSH-mitm][sshMitm] SSH man-in-the-middle tool 
  - [TLS Prober][tlsprober]: a toolfor identifying the implementation in use by SSL/TLS servers
  - [Tplmap][tplMap]: exploit Code Injection and Server-Side Template Injection vulnerabilities
  - [WAFW00F][waf]: identifies and fingerprints Web Application Firewall (WAF) products.
  - [Finmap][finmap]: find, prepare, audit, exploit and even google automatically for local and remote file inclusion bugs within webapps in python
 - [NoSQLMap][NoSql]: audit as well as automate injection attacks while exploiting default configuration weaknesses in NoSQL databases and web applications using NoSQL

   [waf]: <https://github.com/EnableSecurity/wafw00f>
   [tplMap]: <https://github.com/epinna/tplmap>
   [mitmAP]: <https://github.com/xdavidhu/mitmAP>
   [sshMitm]: <https://github.com/jtesta/ssh-mitm>
   [tlsprober]: <https://github.com/WestpointLtd/tls_prober>
   [finmap]: <https://github.com/kurobeats/fimap>
   [NoSql]: <https://github.com/codingo/NoSQLMap>
   
   
