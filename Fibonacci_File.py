# First and Second Number in an array
fib_seq = [0, 1]

#  Filling the Fibonacci Sequence
for i in range(2, 3):
   fib_seq = fib_seq + [(fib_seq[i-2] + fib_seq[i-1])]

print("Fibonacci Numbers are:\n", fib_seq)
