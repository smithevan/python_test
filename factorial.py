x = 4

def factorial_function(x):
  x_prod = 1
  while x > 1:
    x_prod *= x
    x -= 1
  return x_prod

print(factorial_function(x))