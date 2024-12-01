# yukicoder_no.143

K = int(input())
N = int(input())
F = int(input())

AgeList = list(map(int, input().split()))
TotalAge = sum(AgeList)

if K * N < TotalAge:
    print(-1)
else:
    print(K * N - TotalAge)
    
# map(): 指定した関数を複数の要素に適用
