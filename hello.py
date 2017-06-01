from __future__ import print_function
# print (1)

# print hello     # esto es error

# print "Hello"
# print 'hello'
# a = "agustin"
# print "hello",a,"kaka"
# print "hello" + " " + a
#
# print "hello a"
# print 'hello a'
# print "\n"
# print '\n'

##

# print 1+1
# print 1.1+2
# print 1.1+2.2
#
#
# print 2<<3
# print 16>>2
# print 2**2
# print 5/4.0
# print 5.0//4

a=2
b=3
a**=b

c="kaka"
d="kaka"

print (a)


if (c is d):
    print ("yes")

print (3.14j*2j)
import random, math
print (random.randrange(1,10,1))

print(-math.pi)

print ("----------------------------")

for i in range(5):
    print (i)

for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)

print ("----------------------------")

fruits = {'fruta1':'banana2', 'as':'apple2', 'allls':'mango2', 'asd':'9888'}
for (key,value) in fruits.items():        # Second Example
   print ('Current fruit :', key)
   print ('Current value :'+ value)
   print (key+value)





for (i, item) in enumerate(fruits):
    print (i, item)


print ("----------------------------")
items = ['orange', 'pear', 'banana']
for (i, item) in enumerate(items):
    print (i, item)







# print(help({}))
