T = int(input()) 
x = 1  

while x <= T:
  a, b = map(int, input().split())
  print(f"Case #{x}: {a} + {b} = {a + b}")
  x += 1
