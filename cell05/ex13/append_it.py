#!/usr/bin/env python3
import sys
import re

params_count = len(sys.argv) - 1

if params_count == 0:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if not re.search(r"ism$", sys.argv[i]):
            print(sys.argv[i] + "ism")
