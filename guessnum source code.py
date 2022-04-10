import random, os
from colorama import Fore, Back, Style, init
init(convert=True)

balance = 0
question_num = 0
print(f'\nGuess Number Game\nKetik {Fore.GREEN}"bal"{Style.RESET_ALL} untuk melihat uangmu\nYour money now : {balance}\n')
while 1:
	question_num += 1

	# PENENTUAN BENAR ATAU SALAH
	benar = random.randint(1,10) # define angka benar
	#print("benar = ", benar)
	salah = random.randint(1,10) # define pilihan lain atau angka salah
	#print("salah = ", salah)
	while 1: 
		#kalo salahnya sama kaya bener, salahnya generate ulang
		if salah == benar: 
			salah = random.randint(1,10)
			#print("salah = ", salah)
		else:
			break

	# TAMPILAN PILIHAN UNTUK AUTHOR
	out_list = [benar, salah]
	pilihan1 = random.choice(out_list)
	#print("pilihan 1 = ", pilihan1)
	pilihan2 = random.choice(out_list)
	#print("pilihan 2 = ", pilihan2)
	while 1:
		if pilihan2 == pilihan1:
			pilihan2 = random.choice(out_list)
		else:
			break

	#print("Guess Number Game")
	print(f"Question {question_num}")
	print(f"{pilihan1} or {pilihan2}")

	user_answer = input("Answer : ")


	if str(user_answer) == "bal":
		os.system("cls")
		print(f"Your money : {balance}$")
		print("\n")
		# if balance > 0:
		# 	print(f"{Fore.CYAN}Your money = {Fore.GREEN}{balance}$ {Style.RESET_ALL}")
		# 	print("\n")
		# elif balance < 0:
		# 	print(f"{Fore.CYAN}Your money = {Fore.RED}{balance}$ {Style.RESET_ALL}")
		# 	print("\n")

	else:
		if int(user_answer) == benar:
			balanceTambahan=random.randint(1,10)
			balance = balance+balanceTambahan
			print(f"CORRECT! {Fore.GREEN}+{balanceTambahan}$ ", Style.RESET_ALL)
			print("\n")
		elif int(user_answer) == salah:
			balanceBerkurang=random.randint(10,20)
			balance = balance-balanceBerkurang
			print(f"Better luck next time! {Fore.RED}-{balanceBerkurang}$ ", Style.RESET_ALL)
			print("\n")
		
		else:
			print(f"{Fore.CYAN}Ga ada di pilihan", Style.RESET_ALL)
			print("\n")
