# solution by anish0m



#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2:
        print("Weird")
    else:
        if n<6:
            print("Not Weird")
        elif n<=20:
            print("Weird")
        else:
            print("Not Weird")
