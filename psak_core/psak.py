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
import errno
import sys


class Psak:

    def __init__(self):
        """
        The Psak class only needs the name of the module.
        Therefore, the self.parser field will only have module
        names as valid args within this class. Additional args
        will be added to the parser object in whichever module is
        loaded.
        """
        self.usage = ("%(prog)s --module_name <module-args> \n"
                      "Ex. %(prog)s -mitm 180 -vIP 192.168.2.2 -gIP example.com "
                      "-iface wlan1")
        self.description = "PSAK, the Pentester's Swiss Army Knife"
        self.parser = argparse.ArgumentParser(description=self.description,
                                              usage=self.usage)
        self.parser.add_argument('--mitm',
                                 help=("Argments:"
                                       "--mitm: module to load and total "
                                       "runtime in seconds\n"
                                       "-iface: Interface to use for network"
                                       " activity\n"
                                       "-vIP: IP of the victim\n"
                                       "-gIP: IP of the gate/node that the"
                                       "\n victim"
                                       "-gPN: Port number of the gate to "
                                       "connect to\n"
                                       "Usage: PSAK.py --mitm runtime-in-seconds"
                                       " [victim-ip] [gate-ip] "
                                       "[optional-attack-type]"),
                                 required=False, type=int)
        self.parser.add_argument('--slowloris',
                                 help="Usage: %(prog)s slowloris -help",
                                 required=False)
        self.parser.add_argument('-V', '--verbose', action="store_true",
                                 help="Increases logging", required=False)

        if len(sys.argv) <= 1:
            self.parser.print_help()
            sys.exit(1)

    def psak_normal_shutdown(self):
        print("[*] Exiting...")
        sys.exit(0)

    def main(self):
        try:
            if sys.argv[1] == '--mitm':
                from modules.mitm_core.mitm_args import MitmArgs
                from modules.mitm_core.mitm import Mitm
                mitm_args = MitmArgs(self.parser)
                mitm = Mitm(mitm_args)
                mitm.connect(runtime=mitm_args.get_runtime())
        except IOError as e:
            if e[0] == errno.EPERM:
                print(sys.stderr, ("\nYou need root permissions to do this,"
                                   " exiting..."))
                sys.exit(1)


if __name__ == '__main__':
    psak = Psak()
    psak.main()
