class student:
	h=0

	def __init__(self):
		self.h=6

	def my_func(self,k):
		print("hi I am in class")
		self.h=k
		print(self.h)
o=student()
print(o.h)
o1=student()
print(o1.h)
o.my_func(2)
o1.my_func(4)
o3=student()
print(o3.h)