import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter Value:"))

    if n % 2 != 0:  # odd
        print("Weird")
    elif 2 < n < 5 and n % 2 == 0:  # even
        print("Not Weird")
    elif n % 2 == 0 and 6 < n < 20:  # even
        print("Weird")
    elif n % 2 == 0 and n > 20:  # even
        print("Not Weird")

