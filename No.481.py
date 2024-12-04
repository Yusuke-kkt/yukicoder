# yukicoder_no.481

A_list = list(map(int, input().split()))

for i in range(1, 11):
    if i not in A_list:
        print(i)

# 別解
print(55 - sum(A_list))