import random
user=0
comp=0
ide=0
l=["r","p","s"]
d={'r':'Rock','p':'Paper','s':'Scissor'}
while True:
	u=input("Enter your Choice wheather rock=r, paper=p , scissor=s if not press n to Discontinue")
	if u=='n':
		print("Game Over")
		print("User score is:",user)
		print("Computer score is:",comp)
		print("Intermediate:",ide)
		exit()
	c=random.choice(l)
	print("Computr choses",d[c])
	print("User choses",d[u])
	if u==c:
		print("Tie")
		ide=ide+1
	elif u=="r" and c=="p":
		print("Computer wins")
		comp=comp+1
	elif u=="r" and c=="s":
		print("You won")
		user=user+1
	elif u=="s" and c=="r":
		print("Computer wins")
		comp=comp+1
	elif u=="s" and c=="p":
		print("You won")
		user=user+1
	elif u=="p" and c=="s":
		print("Computer wins")
		comp=comp+1
	elif u=="p" and c=="r":
		print("You won")
		user=user+1
