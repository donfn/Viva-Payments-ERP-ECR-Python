import socket
import os
import sys
import random
os.system('color 09')
os.system('@echo off')
os.system('cls')

pos_ip = '192.168.2.12'
pos_port = 8080

pos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pos.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
pos.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 60)
pos.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 4)
pos.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 15)

pos.connect((pos_ip, pos_port))
amount = str(input('Input the amound (ex. 20.50 for 20,50€): ')).replace(',','.')
packet = '|'+str(random.randint(1000,9999))+'|200|00|PAYMENT|'+amount+'|0000||||'
packet = '0'*(4-len(str(len(packet)))) + str(len(packet)) + packet
pos.send(packet.encode())

pos.recv(4096)
print('Present the card at the terminal. Close this program to cancel the transaction.')
response = pos.recv(4096).decode().split('|')
if response[4] == '00':
	os.system('color 02')
	print('APPROVED '+ response[11] + '€' + ' from ' + response[6] + ' ' + response[7] )
	print('The transaction can be reverted ONLY from the Web Dashboard')
else:
	os.system('color 04')
	print('DECLINED. View the POS screen for more info.')
input("Press ENTER to close...")
