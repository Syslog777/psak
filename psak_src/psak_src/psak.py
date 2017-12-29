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

usage = ("%(prog)s --module_name ")
description = "%(prog)s, the Pentester's Swiss Army Knife"
parser = argparse.ArgumentParser(description=description,
                                 usage=usage)


def add_args():
    parser.add_argument('--mitm',
                        help="Usage: %(prog)s --mitm runtime",
                        required=False, nargs="?")
    parser.add_argument('--slowloris',
                        help="Usage: %(prog)s --slowloris host",
                        required=False, nargs="?")
    parser.add_argument('--badpacket', help='Usage: %(prog)s --badpacket host',
                        nargs="?")


if len(sys.argv) <= 1:
    add_args()
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
                                required=False, nargs="?")
            from psak_src.exploit_modules.mitm_exploit.mitm_core.mitm import Mitm
            mitm = Mitm(parser)
            mitm.connect()
        if sys.argv[1] == '--slowloris':
            parser.add_argument('--slowloris',
                                help="Usage: %(prog)s --slowloris host",
                                required=False, nargs="?")
            from psak_src.exploit_modules.server_exploits.slowloris_exploit.slowloris import SlowLoris
            slowloris = SlowLoris(parser)
            slowloris.poisen()
        if sys.argv[1] == '--bad-packet':
            parser.add_argument('--bad-packet', help='Usage: %(prog)s --badpacket host',
                                nargs="?")
            from psak_src.exploit_modules.packet_attacks.bad_packet import BadPacket
            bad_packet = BadPacket(parser)
            bad_packet.send()
    except IOError as e:
        if e[0] == errno.EPERM:
            print(sys.stderr, ("\nYou need root permissions to do this,"
                               " exiting..."))
            sys.exit(1)


if __name__ == '__main__':
    main()
