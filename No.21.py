# yukicoder_no.21

N = int(input())
K = int(input())
numbers = list(int(input()) for i in range(N))

import math
print(math.ceil(max(numbers) - min(numbers)))


# 何が違う？
# numbers = list(map(int, input().split())) → できる
# numbers = [map(int, input().split())] → できない

# numbers = list(int(input()) for i in range(N))
 


