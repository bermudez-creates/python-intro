greeting = "Hello world!"
print(greeting)

def fib(s):
  if s < 0:
    print('Non-ero value')

  elif s == 0:
    return 0
  
  elif s == 1 or s == 2:
    return 1
  
  else:
    return fib(s - 1) + fib(s - 2)


print(fib(6))
print(fib(30))