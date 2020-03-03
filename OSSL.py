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
""".format(version)


main_menu = """

 =================================
| [1]	 ENCRYPT                  |
 =================================
| [2]    DECRYPT(FILE/KEY)        |
 =================================
| [3]	 GENERATE RSA KEY         |
 =================================
| [4] 	 GENERATE CSR             |
 =================================
| [5]	 GENERATE CERTIFICATE     |
 =================================
| [6]	 GET PUBLIC KEY	          |
 =================================
| [7] 	 VERIFY INFORMATION       |
 =================================
 
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
		y = open("{}".format(file_name),"r")
		y = y.read()
		z = open("DUMP/file.txt",'a')
		z.write(y)
		z.close()
	
	
	os.system("openssl enc -ciphers > DUMP/ciphers.txt")
	f = open("DUMP/ciphers.txt",'r')
	f = f.read().split("\n")
	lis=[]
	cnt=0
	for x in f:
		x = x.split()
		for v in x:
			lis.append(v)
	lis.remove(lis[0])
	lis.remove(lis[0])
	
	if not str(file_name).isdigit():
		input("PRESS ENTER TO VIEW AVAILABLE CIPHERS")
		print("\n\n=====================================================================================================")
		for x in lis:
			print("[{} ==> {}]\t".format(cnt,x) , end=" ")
			if cnt%3==0:
				print("\n=====================================================================================================")
			cnt+=1
		print("\n")

		cipher = int(input("[*] SELECT THE CIPHER YOU WISH TO USE ==> "))
		password = input("[*] ENTER THE PASSKEY TO USE : ==> ")
		print("[!] USING BASE64 ENCODING (DEFAULT)")
	
	if val==1:
		os.system("openssl enc {} -base64 -out ENCRYPTED_MSG.txt -k {} -in DUMP/file.txt".format(lis[cipher],password))
		input("\n[*] SUCCESSFULLY ENCRYPTED MESSAGE --> SAVED IN FILE: ENCRYPTED_MSG.txt")
		os.system("rm -rf DUMP")
		main()
		
	elif val==2:
		os.system("openssl enc -d  {} -base64 -out DECRYPTED_MSG.txt -k {} -in DUMP/file.txt".format(lis[cipher],password))
		input("\n[*] SUCCESSFULLY DECRYPTED MESSAGE --> SAVED IN FILE: DECRYPTED_MSG.txt")
		os.system("rm -rf DUMP")
		main()
	
	
	elif val==3:
		os.system("openssl rsa -in {} -out decrypted_{}".format(file_name,file_name))
		input("\n[*] SUCCESSFULLY DECRYPTED MESSAGE --> SAVED IN FILE: DECRYPTED_MSG.txt")
		os.system("rm -rf DUMP")
		main()
	
	elif val==4:
		if null=='y':
			input("PRESS ENTER TO VIEW AVAILABLE CIPHERS")
			print("\n\n=====================================================================================================")
			for x in lis:
				print("[{} ==> {}]\t".format(cnt,x) , end=" ")
				if cnt%3==0:
					print("\n=====================================================================================================")
				cnt+=1
			print("\n")
			cipher = int(input("[*] SELECT THE CIPHER YOU WISH TO USE ==> "))
			
			os.system("openssl genrsa -out RSA-KEY.key {}".format(lis[cipher]))
			input("\n[*] SUCCESSFULLY GENERATED RSA KEY --> SAVED IN FILE: RSA-KEY.key")
		
		elif null=='n':
			os.system("openssl genrsa -out RSA-KEY.key ")
			input("\n[*] SUCCESSFULLY GENERATED RSA KEY --> SAVED IN FILE: RSA-KEY.key")
			
		main()
	
	
	
def Encrypt():
	enc_sub_menu()
	val=1
	print("[!] ENTER FILE NAME IF THE FILE IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	file_name = input("ENTER YOUR FILE NAME : ==> ")
	if file_name=='0':
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
			
		os.system("openssl x509 -in {} -out MY-CERTIFICATE.crt -req -signkey {} -days {} ".format(csr_name , key_name , days))
		
		input("\n[*] SUCCESSFULLY GENERATED SELF SIGNED CERTIFICATE --> SAVED IN FILE: MY-CERTIFICATE.crt")
		
		
	elif choice=='n':
		os.system("mkdir cert")
		os.system("openssl req -new -out cert/MYCSR.csr -keyout cert/MYKEY.key")
		days = input("[*] ENTER VALID TIME PERIOD : [In DAYS] [DEFAULT : 365 DAYS] :  ")
		if days=='':
			days=365
			
		os.system("openssl x509 -in cert/{} -out MY-CERTIFICATE.crt -req -signkey cert/{} -days {} ".format("MYCSR.csr","MYKEY.key",days))
		os.system("rm -rf cert")
		
		input("\n[*] SUCCESSFULLY GENERATED SELF SIGNED CERTIFICATE --> SAVED IN FILE: MY-CERTIFICATE.crt")
		
	main()
	

	
	
def GenCsr():
	csr_sub_menu()
	choice = input("[*] DO YOU HAVE A RSA KEY ? (Y/N) : ").lower()
	if choice=='y':
		print("[!] ENTER KEY NAME IF THE KEY IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
		key_name = input("ENTER KEY NAME : ==> ")
		os.system("openssl req -new -key {} -out MY-CSR.csr".format(key_name))
		input("\n[*] SUCCESSFULLY GENERATED CSR  --> SAVED IN FILE: MY-CSR")
	
	elif choice=='n':
		print("[!] GENERATING NEW [PRIVATE KEY] AND CSR")
		os.system("openssl req -new -out MY-CSR.csr")
		input("\n[*] SUCCESSFULLY GENERATED CSR AND KEY --> SAVED IN FILE: MY-CSR and privkey.pem")
	
	main()
	
def GetPublic():
	cls()
	print(banner)
	print("[!] ENTER KEY NAME IF THE KEY IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	key_name = input("ENTER KEY NAME : ==> ")
	os.system("openssl rsa -in {} -pubout -out PUBLIC-KEY.key ".format(key_name))
	
	input("\n[*] SUCCESSFULLY GENERATED PUBLIC KEY --> SAVED IN FILE: PUBLIC-KEY.key")
	
	main()
	
		
	
	
def VerifyInfo():
	verify_sub_menu()
	choice = input("[*] ENTER YOUR CHOICE : ==> ")
	
	print("[!] ENTER FILE NAME IF THE FILE IS PRESENT IN WORKING DIRECTORY ELSE GIVE FULL PATH \n")
	
	if choice=='1':
		file = input("[*] ENTER CSR NAME : ")
		os.system("openssl req -text -noout -verify -in {}".format(file))
		input("\n[!]  PRESS ENTER TO CONTINUE ")
		VerifyInfo()
	
	elif choice=='2':
		file = input("[*] ENTER RSA KEY NAME : ")
		os.system("openssl rsa -in {} -check".format(file))
		input("\n[!]  PRESS ENTER TO CONTINUE ")
		VerifyInfo()
		
	elif choice=='3':
		file = input("[*] ENTER CERTIFICATE NAME : ")
		os.system("openssl x509 -in {} -text -noout".format(file))
		input("\n[!]  PRESS ENTER TO CONTINUE ")
		VerifyInfo()
		
		
	elif choice=='0':
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
		print("BYE....")
		
