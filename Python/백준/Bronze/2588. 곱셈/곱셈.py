A = int(input())
B = list(map(int, input()))

print(A * B[2])
print(A * B[1])
print(A * B[0])
print((A * B[2]) + (A * B[1] * 10) + (A * B[0] * 100))


