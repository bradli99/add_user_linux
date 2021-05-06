#!/usr/bin/python3

import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("user", type=str, help="user name to create in the system")
args = parser.parse_args()

if args.user:
	username = args.user

# check
file = '/etc/passwd'

users_list = []

lines = open(file).readlines()
for line in lines:
	user = line.split(':')[0]

	if user == username:
		print(f'[!] {username} already exist')
		exit()


print(f'[+] {username} is new in the system')
os.system(f'sudo useradd {username}')
print(f'[+] User {username} just got added')

print('[#] Done')
