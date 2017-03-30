from __future__ import division
import math
import random
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
def mul_inv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
def encrypt(msg,a,b):
	asci=[]
	encrypt=''
	for i in msg:
		asci.append(ord(i)-65)
	for j in asci:
		encrypt+=chr((j*a+b)%26+65)
	return encrypt
def decrypt(en):
	decrypt=''
	for i in en:
		decrypt+=chr(((mul_inv(5,26)*(ord(i)-65-8))%26)+65)
	return decrypt
if __name__=='__main__':
	msg=input('Enter the message to be decrypted ')
	#print(msg.upper())
	en=encrypt(msg.upper(),5,8)
	print ('Inverse of 26')
	#a=mul_inv(5,26)
	print(decrypt(en).replace("T","  "))

