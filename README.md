# PSAK  

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://nodesource.com/products/nsolid)
[![PSAK](https://img.shields.io/badge/PSAK-Open--Source-000000.svg)](https://github.com/Syslog777/psak/) [![GitHub forks](https://img.shields.io/github/forks/Syslog777/psak.svg)](https://github.com/Syslog777/psak/network) [![Github issues](https://img.shields.io/github/issues/Syslog777/psak.svg)](https://github.com/Syslog777/psak/issues) [![Python 3.6](https://img.shields.io/badge/Python-3.6-00BFFF.svg)](https://www.python.org/downloads/release/python-363/) [![License](https://img.shields.io/github/license/Syslog777/psak.svg)](https://github.com/Syslog777/psak/blob/Release-0.5/LICENSE)


### Introduction
PSAK is a project that targets a very specific audience

PSAK must be developed with inexperience in mind while maintaining functional dynamics. In other words, it should be operable by a "script kiddie" with strong reading comprehension, while a seasoned pen-tester should not become frustrated with overly limited options. However, it is not meant to fully replace original tools such as "nmap" or "metasploit". Such a project is beyond the scope of the tasks at hand.

PSAK must be modular and easily expandable. This is because the founding developers cannot possibly integrate every single Linux-based 
security-oriented application into it. In addition, to remain relevant means to expand and grow. PSAK will not be a project to invest in as a developer or a user if it does not evolve in a positive manner. Some tools stagnate in their development, causing users to shy away from them and developers to ignore them. Clearly, the ability to evolve is crucial to PSAK's relevancy in the years to come.


### Installation Instructions
Type the following into your terminal as user root:
```pip3 install psak```.
If you are a sudo user, then type the following instead:
```sudo pip3 install psak```.
Please note that installation success depends on many factors, including but not limited to:
- Python version
- Pip version
- Operating System

### PSAK Framework
PSAK is simple to integrate with, provided a intermediate
understanding of software development and Python 3.

PSAK Package  | Description
------------- | -------------
psak_project.psak_core  | holds all of psak's source code except for psak.py
psak_project.psak_exceptions  | holds psak's exception types while importing individual exception modules from the psak_core.modules package
psak_project.psak_core.modules  | holds all available integrated exploit modules
psak_project.psak_core.psak.py | psak python3 driver

Required package  |  Description
-------------|------------
psak_project.psak_core.modules.new_package.new_module_core | holds all of your main functional source code
psak_project.psak_core.modules.new_package.new_package_exceptions | holds your exceptions
psak_project.psak_core.modules.new_package.new_package_tests | holds all of your tests


Go to the wiki for additional project info --> https://github.com/Syslog777/psak/wiki
