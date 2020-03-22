#!/usr/bin/python3
# DATE : 31 January 2020
# Written by : Aniket.N.Bhagwate ~{NullByte007}
# Base tool : OpenSSL

import os 

cls = lambda:os.system("clear")
os.system("rm -rf DUMP 2> error.txt 1>error.txt")
os.system("mkdir DUMP")
os.system("openssl version > version.txt")
f = open("version.txt",'r')
version = f.read()
os.system("rm -rf version.txt")


banner="""

\t\t\t\t\t<=============================================>
\t\t\t\t\t|   ___                    ____ ____  _       |
\t\t\t\t\t|  / _ \ _ __   ___ _ __  / ___/ ___|| |      |
\t\t\t\t\t| | | | | '_ \ / _ \ '_ \ \___ \___ \| |      |
\t\t\t\t\t| | |_| | |_) |  __/ | | | ___) |__) | |___   |
\t\t\t\t\t|  \___/| .__/ \___|_| |_||____/____/|_____|  |
\t\t\t\t\t|       |_|                                   |
\t\t\t\t\t<=============================================>
\t\t\t\t\t OpenSSL Version : {}  
\t\t\t\t\t Coded By : Nullbyte007 ~ Aniket Bhagwate    
""".format(version)


main_menu = """
 ===================================
| [1]	 ENCRYPT                    |
 ===================================
| [2]    DECRYPT(FILE/KEY)          |
 ===================================
| [3]	 GENERATE RSA KEY           |
 ===================================
| [4] 	 GENERATE CSR               |
 ===================================
| [5]	 GENERATE CERTIFICATE       |
 ===================================
| [6]	 GET PUBLIC KEY	            |
 ===================================
| [7] 	 VERIFY INFORMATION         |
 ===================================
| [8]	 GENERATE MESSAGE DIGEST    |
 ===================================
 
 ============================
| [0]    EXIT         	     |
 ============================
 
"""

enc_dec_menu = """

 ==================
| [#] SELECT FILE  |
 ==================
 
 ==================
| [0] BACK [ <== ] |
 ==================
"""


decrypt_sub="""

 ===================
| [1]	 FILE       |
 ===================
| [2]    RSA KEY    |
 ===================
 
 ==================
| [0] BACK [ <== ] |
 ==================
"""


csr_sub="""

 ============================
| 	GENERATE CSR         |
 ============================
 
 ==================
| [0] BACK [ <== ] |
 ==================

""" 	

verify_sub="""

 ======================
| [1]	 CSR           |
 ======================
| [2]    RSA KEY       |
 ======================
| [3] 	 CERTIFICATE   |
 ======================

 ==================
| [0] BACK [ <== ] |
 ==================

"""

def verify_sub_menu():
	cls()
	print(banner)
	print(verify_sub)
	
	
def csr_sub_menu():
	cls()
	print(banner)
	print(csr_sub)

def enc_sub_menu():
	cls()
	print(banner)
	print(enc_dec_menu)


def dec_sub_menu():
	cls()
	print(banner)
	print(decrypt_sub)

def menu_pr():
	cls()
	print(banner)
	print(main_menu)



def openssl(file_name,val,null):
	if not str(file_name).isdigit():
		try:
			y = open("{}".format(file_name),"r")
			y = y.read()
			z = open("DUMP/file",'a')
			z.write(y)
			z.close()
		except:
			input(" [!] FILE NOT FOUND !! ")
			main()
	
	
	
	os.system("openssl list -cipher-commands > DUMP/list.txt")
	f = open("DUMP/list.txt",'r')
	f = f.read().split()
	f.pop()
	nl = []
	lis =[]

	for x in f:
		nl.append(x.split("=>")[-1:][0])
	
	for x in nl:
		if x[0]==' ':
			x = x[1:]
			lis.append(x)
		else:
			lis.append(x)

	f = open("DUMP/list2.txt",'a')
	for x in lis:
		f.write(x+"\n")
	f.close()
	
	os.system("cat DUMP/list2.txt | sort -u > DUMP/list.txt")
	lis = open("DUMP/list.txt",'r')
	lis = lis.read().split("\n")
	lis.pop()
	
	def display_cipher():
		print("\n\n+---------------------------------------------------------------------------------------+")				
		try:
			row = "| [{i1:<2d}] {val1:<20s} | [{i2:<2d}] {val2:<20s} | [{i3:<2d}] {val3:<24s} |".format
			x=0
			y=1
			z=2
			for b in range(len(lis)+1):
				print(row(i1=x , val1=lis[x] , i2=y , val2=lis[y] , i3=z , val3=lis[z]))
				print("+---------------------------------------------------------------------------------------+")		
				x = x+3
				y = y+3
				z = z+3
		
		except:
			try:
				if lis[y]!='':
					row = "| [{i1:<3d}] {val1:<20s} | [{i2:<3d}] {val2:<20s}".format 
					print(row(i1=x , val1=lis[x] , i2=y , val2=lis[y]))
			except:
				pass

			



	if val==1:
		display_cipher()
		cipher = int(input("\n[*] SELECT THE CIPHER YOU WISH TO USE ==> "))
		print("\n[*] SELECTED CIPHER : \033[30;42m {} \033[m".format(lis[cipher]))
		password = input("\n[*] ENTER THE PASSKEY TO USE : ==> ")
		print("\n[!] USING BASE64 ENCODING (DEFAULT)")
		
		os.system("openssl enc -{} -base64 -out ENCRYPTED_MSG.txt -k {} -in DUMP/file 2> DUMP/error.txt ".format(lis[cipher],password))
		input("\n[*] SUCCESSFULLY ENCRYPTED MESSAGE --> SAVED IN FILE: ENCRYPTED_MSG.txt")
		os.system("rm -rf DUMP 2> DUMP/error.txt")
		main()
		
	elif val==2:
		display_cipher()
		cipher = int(input("\n[*] SELECT THE CIPHER YOU WISH TO USE ==> "))
		print("\n[*] SELECTED CIPHER : \033[30;42m {} \033[m".format(lis[cipher]))
		password = input("\n[*] ENTER THE PASSKEY TO USE : ==> ")
		print("\n[!] USING BASE64 ENCODING (DEFAULT)")
		
		
		os.system("openssl enc -d  -{} -base64 -out DECRYPTED_MSG.txt -k {} -in DUMP/file 2> DUMP/error.txt".format(lis[cipher],password))
		input("\n[*] SUCCESSFULLY DECRYPTED MESSAGE --> SAVED IN FILE: DECRYPTED_MSG.txt")
		os.system("rm -rf DUMP 2> DUMP/error.txt")
		main()
	
	
	elif val==3:
		os.system("openssl rsa -in {} -out decrypted_{} 2> DUMP/error.txt".format(file_name,file_name))
		input("\n[*] SUCCESSFULLY DECRYPTED MESSAGE --> SAVED IN FILE: DECRYPTED_MSG.txt")
		os.system("rm -rf DUMP 2> DUMP/error.txt")
		main()
	
	elif val==4:
		if null=='y':
			input("PRESS ENTER TO VIEW AVAILABLE CIPHERS")
			display_cipher()
					
			cipher = int(input("[*] SELECT THE CIPHER YOU WISH TO USE ==> "))
			
			os.system("openssl genrsa -out RSA-KEY.key -{} 2> DUMP/error.txt ".format(lis[cipher]))
			input("\n[*] SUCCESSFULLY GENERATED RSA KEY --> SAVED IN FILE: RSA-KEY.key")
		
		elif null=='n':
			os.system("openssl genrsa -out RSA-KEY.key 2> DUMP/error.txt")
			input("\n[*] SUCCESSFULLY GENERATED RSA KEY --> SAVED IN FILE: RSA-KEY.key")
			
		main()
	
	
	
def Encrypt():
	enc_sub_menu()
	val=1
	print("[!] ENTER FILE NAME IF THE FILE IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	file_name = input("ENTER YOUR FILE NAME : ==> ")
	if file_name=='0':
		input("[!] INVALID FILE NAME !!")
		main()
	openssl(file_name,val,0)
		
		
		
def Decrypt():
	dec_sub_menu()
	
	choice = input("[*] ENTER CHOICE : ==> ")
	if choice=='1':
		val=2
		print("[!] ENTER FILE NAME IF THE FILE IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
		file_name = input("ENTER YOUR FILE NAME : ==> ")
		if file_name=='0':
			main()
		openssl(file_name,val,0)
		
		
	elif choice=='2':
		val=3
		print("[!] ENTER KEY NAME IF THE KEY IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
		file_name = input("ENTER KEY NAME : ==> ")
		if file_name=='0':
			main()
		openssl(file_name,val,0)
		
	elif choice=='0':
		main()
		

def GenRsa():
	cls()
	print(banner)
	val=4
	cipher=''
	key_size = input("[*] ENTER YOUR KEY SIZE (Default: 2048)")
	if key_size=='':
		key_size = 2048
	choice = input("[*] DO YOU WANT TO USE ENCRYPTION ? (Y/N)").lower()
	if choice=='y':
		openssl(key_size,val,'y')
	elif choice=='n':
		openssl(key_size,val,'n')



def GenCert():
	cls()
	print(banner)
	choice = input("DO YOU HAVE CSR AND A PRIVATE KEY ? (Y/N)  : ").lower()
	if choice=='y':
		print("[!] ENTER CSR NAME IF THE CSR IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
		csr_name = input("ENTER CSR NAME : ==> ")
		
		print("[!] ENTER KEY NAME IF THE KEY IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
		key_name = input("ENTER KEY NAME : ==> ")
		
		days = input("[*] ENTER VALID TIME PERIOD : [In DAYS] [DEFAULT : 365 DAYS] :  ")
		if days=='':
			days=365
			
		os.system("openssl x509 -in {} -out MY-CERTIFICATE.crt -req -signkey {} -days {} 2> DUMP/error.txt".format(csr_name , key_name , days))
		
		input("\n[*] SUCCESSFULLY GENERATED SELF SIGNED CERTIFICATE --> SAVED IN FILE: MY-CERTIFICATE.crt")
		
		
	elif choice=='n':
		os.system("mkdir cert")
		os.system("openssl req -new -out cert/MYCSR.csr -keyout cert/MYKEY.key 2> DUMP/error.txt")
		days = input("[*] ENTER VALID TIME PERIOD : [In DAYS] [DEFAULT : 365 DAYS] :  ")
		if days=='':
			days=365
			
		os.system("openssl x509 -in cert/{} -out MY-CERTIFICATE.crt -req -signkey cert/{} -days {} 2> DUMP/error.txt".format("MYCSR.csr","MYKEY.key",days))
		os.system("rm -rf cert 2> DUMP/error.txt")
		
		input("\n[*] SUCCESSFULLY GENERATED SELF SIGNED CERTIFICATE --> SAVED IN FILE: MY-CERTIFICATE.crt")
		
	main()
	

	
	
def GenCsr():
	csr_sub_menu()
	choice = input("[*] DO YOU HAVE A RSA KEY ? (Y/N) : ").lower()
	if choice=='y':
		print("[!] ENTER KEY NAME IF THE KEY IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
		key_name = input("ENTER KEY NAME : ==> ")
		os.system("openssl req -new -key {} -out MY-CSR.csr 2> DUMP/error.txt".format(key_name))
		input("\n[*] SUCCESSFULLY GENERATED CSR  --> SAVED IN FILE: MY-CSR")
	
	elif choice=='n':
		print("[!] GENERATING NEW [PRIVATE KEY] AND CSR")
		os.system("openssl req -new -out MY-CSR.csr 2> DUMP/error.txt")
		input("\n[*] SUCCESSFULLY GENERATED CSR AND KEY --> SAVED IN FILE: MY-CSR and privkey.pem")
	
	main()
	
def GetPublic():
	cls()
	print(banner)
	print("[!] ENTER KEY NAME IF THE KEY IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	key_name = input("ENTER KEY NAME : ==> ")
	os.system("openssl rsa -in {} -pubout -out PUBLIC-KEY.key 2> DUMP/error.txt".format(key_name))
	
	input("\n[*] SUCCESSFULLY GENERATED PUBLIC KEY --> SAVED IN FILE: PUBLIC-KEY.key")
	
	main()
	
		
	
	
def VerifyInfo():
	verify_sub_menu()
	choice = input("[*] ENTER YOUR CHOICE : ==> ")
	
	print("[!] ENTER FILE NAME IF THE FILE IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	
	if choice=='1':
		file = input("[*] ENTER CSR NAME : ")
		os.system("openssl req -text -noout -verify -in {} 2> DUMP/error.txt".format(file))
		input("\n[!]  PRESS ENTER TO CONTINUE ")
		VerifyInfo()
	
	elif choice=='2':
		file = input("[*] ENTER RSA KEY NAME : ")
		os.system("openssl rsa -in {} -check 2> DUMP/error.txt".format(file))
		input("\n[!]  PRESS ENTER TO CONTINUE ")
		VerifyInfo()
		
	elif choice=='3':
		file = input("[*] ENTER CERTIFICATE NAME : ")
		os.system("openssl x509 -in {} -text -noout 2> DUMP/error.txt".format(file))
		input("\n[!]  PRESS ENTER TO CONTINUE ")
		VerifyInfo()
		
		
	elif choice=='0':
		main()

def GenDigest():
	enc_sub_menu()
	print("[!] ENTER FILE NAME IF THE FILE IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	file_name = input("ENTER YOUR FILE NAME : ==> ")
	if file_name=='0':
		input("[!] INVALID FILE NAME !!")
	else:
		
		os.system("openssl list -digest-algorithms > DUMP/list.txt")
		f = open("DUMP/list.txt",'r')
		f = f.read().split("\n")
		f.pop()
	
		nl = []
		dgst =[]
	
		for x in f:
			nl.append(x.split("=>")[-1:][0])
	
		for x in nl:
			if x[0]==' ':
				x = x[1:]
				dgst.append(x)
			else:
				dgst.append(x)
	
		f = open("DUMP/list2.txt",'a')
		for x in dgst:
			f.write(x+"\n")
		f.close()
		os.system("cat DUMP/list2.txt | sort -u > DUMP/list.txt")
		dgst = open("DUMP/list.txt",'r')
		dgst = dgst.read().split("\n")
		dgst.pop()
		
		try:
			row = "| [{i1:<2d}] {val1:<20s} | [{i2:<2d}] {val2:<20s} | [{i3:<2d}] {val3:<24s} |".format
			x=0
			y=1
			z=2
			print("+---------------------------------------------------------------------------------------+")		
			for b in range(len(dgst)+1):
				print(row(i1=x , val1=dgst[x] , i2=y , val2=dgst[y] , i3=z , val3=dgst[z]))
				print("+---------------------------------------------------------------------------------------+")
				x = x+3
				y = y+3
				z = z+3
		
		except:
			try:
				if dgst[y]!='':
					row = "| [{i1:<3d}] {val1:<20s} | [{i2:<3d}] {val2:<20s} | ".format 
					print(row(i1=x , val1=dgst[x] , i2=y , val2=dgst[y]))
					print("+---------------------------------------------------------------------------------------+")		
			
			except:
				row = "| [{i1:<3d}] {val1:<79s} |".format
				print(row(i1=x , val1=dgst[x]))
				print("+---------------------------------------------------------------------------------------+")		
			
		choice = int(input("\n\n[*] SELECT THE DIGEST YOU WISH TO USE ==> "))
				
		input("\n[*] SELECTED CIPHER : \033[30;42m {} \033[m \n\n <PRESS ENTER>".format(dgst[choice]))
		
		os.system("openssl {} {} > MSG_DIGEST".format(dgst[choice] , file_name))
		input("\n[*] SUCCESSFULLY GENERATED MESSAGE DIGEST --> SAVED IN FILE: MSG_DIGEST")
		main()
				
def main():

	menu_pr()
	choice = input("[*] SELECT YOUR CHOICE : ==> ")
	
	if choice=='1':
		Encrypt()
		
	elif choice=='2':
		Decrypt()
	
	elif choice=='3':
		GenRsa()
	
	elif choice=='4':
		GenCsr()
	
	elif choice=='5':
		GenCert()
	
	elif choice=='6':
		GetPublic()
	
	elif choice=='7':
		VerifyInfo()
		
	elif choice=='8':
		GenDigest()
	
	else:
		print("BYE...!")
		os.system("rm -rf DUMP")
		os.system("rm -rf error.txt")
		exit()
	
if __name__=='__main__':
	try:
		main()
	
	except:	
		cls()
		os.system("rm -rf DUMP")
		os.system("rm -rf error.txt")
		print("BYE....")
		
