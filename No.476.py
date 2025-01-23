# yukicoder_no.476

mai_answer = int(input())

numbers_lis = list(map(int, input().split()))

if mai_answer == (sum(numbers_lis) / len(numbers_lis)):
    print("YES")
else:
    print("NO")


# map(int, input().split()) を print → <map object at 0x000001663901A0D0>
# map object をリスト化する必要がある →　list(map(int, input().split()))

# 別解
import statistics
if mai_answer == statistics.mean(numbers_lis):
    print("YES")
else:
    print("NO")