#!/usr/bin/env python3
#Author: Jude Owusu
#AuthorID:103399176
#Date Created: 01/22/25

import sys

if len(sys.argv) < 2:
    sys.exit(1)

timer = int(sys.argv[1])

while timer >  0:
    print(timer)
    timer = timer - 1

print('blast off!')


