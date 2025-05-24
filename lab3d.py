#!/usr/bin/env python3

# Author ID: rgagabon@myseneca.ca

import subprocess

def free_space():
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    
    return result.stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())