"""Write function that will generate continous fibonacci numbers.
   You are forbidden from using for and while."""

# The generator will not be infinite, at some point it will hit recursion limit
def fibonacci(n1=0, n2=1):
    yield n1
    yield from fibonacci(n1=n2, n2=n1+n2)

# Demonstrate generating first 10 numbers
gen = fibonacci()
for i in range(10):
    print(next(gen))
