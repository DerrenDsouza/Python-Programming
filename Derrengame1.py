import random
l=["r","p","s"]
while True:
	u=input("Enter your Choice,Press n to Discontinue")
	if u=='n':
		print("Game Over")
		exit()
	c=random.choice(l)
	print("Computr choses",c)
	if u==c:
		print("Tie")
	elif u=="r" and c=="p":
		print("Computer wins")
	elif u=="r" and c=="s":
		print("You won")
	elif u=="s" and c=="r":
		print("Computer wins")
	elif u=="s" and c=="p":
		print("You won")
	elif u=="p" and c=="s":
		print("Computer wins")
	elif u=="p" and c=="r":
		print("You won")