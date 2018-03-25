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
from setuptools import find_packages
from setuptools import setup

"""
https://docs.python.org/3/distutils/setupscript.html#installing-package-data
EX.
setup.py
src/
    mypkg/
        __init__.py
        module.py
        data/
            tables.dat
            spoons.dat
            forks.dat
setup(...,
      packages=['mypkg'],
      package_dir={'mypkg': 'src/mypkg'},
      package_data={'mypkg': ['data/*.dat']},
      )
"""
"""
src=src
mypkg=psak_core

"""
setup(
    name='psak',
    version='0.6.0.1',
    packages=find_packages('psak_src'),  # include all packages under psak_src
    package_dir={'': 'psak_src'},  # tell distutils packages are under psak_src
    entry_points={"console_scripts": ["psak=psak_src.psak:main"]},
    include_package_data=True,  # include everything in source control,
    url='https://github.com/Syslog777/psak',
    license='BSD 3',
    author='Syslog777',
    author_email='thejavapi26@gmail.com',
    description='The Pentester\'s Swiss Army Knife ',
    keywords=["pentesting", "psak", "dos", "ddos", "ultimate", "hacking"]
)
print(find_packages())
