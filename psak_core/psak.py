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

import argparse
import sys


class Psak:

    def __init__(self):
        self.usage = 'python3 %prog <module_name> [module-options] \n' \
                     'Ex. python3 psak -mitm_core '
        self.description = "PSAK, the Pentester's Swiss Army Knife"
        self.parser = argparse.ArgumentParser(description=self.description,
                                              usage=self.usage)
        self.parser.add_argument('--mitm_core',
                                 help="Usage: python psak --mitm_core victim_ip gate_ip [optional_attack] ")
        self.args = self.parser.parse_args()
        if len(sys.argv) <= 1:
            self.parser.print_help()
        sys.exit(1)

    def psak_normal_shutdown(self):
        print("[*] Exiting...")
        sys.exit(0)

    def psak_error_shutdown(self):
        print("[*] Exiting, ")

    def module_loader(self):
        if self.args.mitm:

    def main(self):


if __name__ == '__main__':
    psak = Psak()
    psak.main()
