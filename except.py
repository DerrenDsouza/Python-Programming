try:
	l={1,5,7,4,9}
	a=len(l)
	if a>3:
		raise NameError
	elif a<3:
		raise TypeError
except NameError:
	print("No error")
except TypeError:
	print("error occured")
finally:
	print("exection Completed")