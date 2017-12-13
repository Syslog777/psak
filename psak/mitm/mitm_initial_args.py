#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(
    description="PSAK, the Pentester's Swiss Army Knife")

if len(sys.argv) <= 1:
    parser.print_help()
sys.exit(1)
