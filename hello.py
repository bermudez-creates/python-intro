# common greeting 
name = input('Name?')
greeting = "Hello {} !"
# .format() how to use a previous set string to a new one
print(greeting.format(name))


# Comment on fibonnacci sequence in python 
def fib(s):
  if s < 0:
    print('Non-zero value')

  elif s == 0:
    return 0
  
  elif s == 1 or s == 2:
    return 1
  
  else:
    return fib(s - 1) + fib(s - 2)


# print(fib(6))
# print(fib(30))

# Variables
array = [1,2,3,4]
# array.insert(1, "Value1")
array.insert(0, 0)
print(array)