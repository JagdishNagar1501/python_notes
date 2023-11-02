##  Python String  ##

#        Python accepts single ('), double (") and triple (''' or """) quotes to denote 
#        string literals  

# a = 'Hello World'
# b = "This is Sentance."
# c = """"This is paragraph. It is 
#        made up to multiple
#        line and sentance. """ 

#print(a)
#print(b)
#print(c)

#print(a + ' add ' + b)
#print(a ,'add', c)

# x = "python"
# y = "progr'am'"
# z = "progr'am"
# zz = 'progr"am"'

# print(x)
# print(y)
# print(z)
# print(zz)

# -- Format Function
# print('{} this is {}'.format(x,y))
# print('{1} this is {0}'.format(x,y))
# print(f'{x} this is {y}')
# print(f'{x} this is {y.upper()}')

# print(a[1])
# print(a[4:])
# print(a[:5])
# print(abvn [2:5])
# print(a[-1])
# print(a*2)

#  some function
# a = " jagdish nagar "
# print(a.strip())
# print(len(a))
# print(a.lower())
# print(a.count('l'))
# print(a.upper())

# Replace
#print(a.replace("H", "q"))
#print(a)

#x = a.replace("o","P")
#print(x)

# a = " hello world "
# print(a.split())
# print(a.find('hello'))

# in and not in
a = "hello world"
print('e' in a)

#To ask the user for input
print("Enter your name:")
x = input()
print("Hello, ", x)


y = input("Enter the value:-")
print(y)

# Help
print(help(str.upper))