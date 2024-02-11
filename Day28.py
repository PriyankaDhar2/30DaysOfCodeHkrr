#!/bin/python3

import math
import os
import random
import re
import sys

def filter_gmail_users(rows):
    gmail_users = [row[0] for row in rows if re.search(r"@gmail\.com$", row[1])]
    gmail_users.sort()
    return gmail_users

if __name__ == '__main__':
    N = int(input().strip())

    rows = [input().strip().split() for _ in range(N)]

    gmail_users = filter_gmail_users(rows)

    for user in gmail_users:
        print(user)
