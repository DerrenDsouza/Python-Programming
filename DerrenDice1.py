import random

while True:
	d=input("Press r to roll,q to quit:")

	if d=='r':
		print("You got:",random.randint(1,6))

	elif d=='q':
		print("Bye Bye Sir")
		exit()

print("end")
