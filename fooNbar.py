# write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000
# for all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. 
#  do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".
from random import randint

def fooBar():
	x=randint(0, 1000)
	for i in range(100,100000):
		if x*x == i:
			print "Bar"
# if perfect square, print "Bar"
		elif i % x == 0 :
			print "Foo"
# if prime number, print "Foo"
		else:
			print "FooBar"
# if neither, print "FooBar"
fooBar()