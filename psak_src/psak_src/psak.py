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

"""
Notes:
1.) Each parser variable module argument is reusable.
2.) A module called multi-mod will be available to load multiple exploit_modules.
This will be required to run multiple exploit_modules because of the way psak is
designed
3.) psak must be at the top dir level as the modules it attempting to import.
If it is not, the python interpreter will look for the modules it is importing
on the PYTHONPATH. If the PYTHONPATH has a different module with the same name
on it, the interpreter will import that module, not the one you are attempting
to import

"""
usage = ("%(prog)s --module_name --help")
description = ("%(prog)s, the Pentester's Swiss Army Knife\n")
parser = argparse.ArgumentParser(description=description,
                                 usage=usage)


def add_args():
    parser.add_argument('--mitm',
                        help="Usage: %(prog)s --mitm runtime <options>\n"
                             "Attack type: connection-oriented",
                        required=False, nargs="?", type=int)
    parser.add_argument('--slowloris',
                        help="Usage: %(prog)s --slowloris host <options>\n"
                             "Attack type: connection-oriented",
                        required=False, nargs="?", type=str)
    parser.add_argument('--synack', help="Usage: %(prog)s --synack <options>\n"
                                         " Attack type: conncetion-oriented", nargs="?")
    parser.add_argument('--interface', help="Usage: %(prog)s --interface <options>", nargs="?")
    parser.add_argument('--ninfo', help="Usage: %(prog)s --ninfo <options>", nargs="?")


if len(sys.argv) <= 1:
    add_args()
    print("#### Basic Brute-Force Connectionless Attacks ####\n"
          "- UDP Flood\n"
          "- ICMP Flood\n"
          "- IGMP Flood\n"
          "#### Complex Brute-Force Connectionless Attacks ####\n"
          "- Smurf Attack\n"
          "- Fraggle Attack\n"
          "- DNS Amplification Attack\n"
          "#### Complex Brute-Force Connection-Oriented Attacks ####\n"
          "- DNS Flood\n"
          "- HTTP Flood\n"
          "- Slowloris\n"
          "#### Complex Stealth Recon Attacks ####\n"
          "- Man-in-the-middle attack\n")
    parser.print_help()
    sys.exit(1)

if sys.argv[1] == ('-h') or sys.argv[1] == ('--help'):
    add_args()
    parser.print_help()
    sys.exit(0)


def main():
    try:
        if sys.argv[1] == '--mitm':
            parser.add_argument('--mitm',
                                help="Usage: %(prog)s --mitm runtime -vIP 192.168.43.2"
                                     " -gIP 192.168.43.1 -iface wlan1",
                                required=False, nargs="?", type=int)
            try:
                from exploit_modules.mitm import Mitm
                # First try to import from local dev project
            except ImportError:
                # If that does not work, import from global psak lib
                from psak_src.exploit_modules.mitm import Mitm
            mitm = Mitm(parser)
            mitm.connect()

        if sys.argv[1] == '--slowloris':
            parser.add_argument('--slowloris',
                                help='Usage: %(prog)s --slowloris host',
                                required=False, nargs='?')
            try:
                from exploit_modules.slowloris import SlowLoris
            except ImportError:
                from psak_src.exploit_modules.slowloris import SlowLoris
            slowloris = SlowLoris(parser)
            slowloris.poisen()

        if sys.argv[1] == '--synack':
            parser.add_argument('--synack', help='Usage %(prog)s --synack ipaddress',
                                required=False, nargs="?")
            try:
                from exploit_modules.synack_flood import SynAckFlood
                synack = SynAckFlood(parser)
                synack.flood()
            except ImportError:
                from psak_src.exploit_modules.synack_flood import SynAckFlood
                synack = SynAckFlood(parser)
                synack.flood()

        if sys.argv[1] == '--interface':
            parser.add_argument("--interface", required=False, nargs="?",
                                help='Usage %(prog)s --interface interface')
            try:
                from exploit_modules.interface import Interface
            except ImportError:
                from psak_src.exploit_modules.interface import Interface
            interface = Interface(parser)
            interface.interface()

        if sys.argv[1] == '--ninfo':
            parser.add_argument("--ninfo", required=False, nargs="?",
                                help='Usage %(prog)s --list --macs\n'
                                     'Network info')
            try:
                from exploit_modules.internal_utils.ninfo import NInfo
                ninfo = NInfo(parser)
                ninfo.main()
            except ImportError:
                from psak_src.exploit_modules.internal_utils.ninfo import NInfo
                ninfo = NInfo(parser)
                ninfo.main()
        else:
            add_args()
            parser.print_help()
            sys.exit(1)

    except IOError as e:
        if e[0] == errno.EPERM:
            print(sys.stderr, ("\nYou need root permissions to do this,"
                               " exiting..."))
            sys.exit(1)


if __name__ == '__main__':
    main()
