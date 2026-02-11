#!/usr/bin/env python3

import sys

if len(sys.argv) !=3:
    print("none")
else :
    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)



#!/usr/bin/env python3
# import sys
# import re

# if len(sys.argv) != 3:
#     print("none")
# else:
#     keyword = sys.argv[1]
#     text = sys.argv[2]

#     matches = re.findall(re.escape(keyword), text)  # escape กัน keyword เป็น regex พิเศษ
#     count = len(matches)

#     if count == 0:
#         print("none")
#     else:
#         print(count)