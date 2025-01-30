# yukicoder_no.211

K = int(input())
prime_num_dice = [2, 3, 5, 7, 11, 13]
composit_num_dice = [4, 6, 8, 9, 10, 12]
num_of_cases = []

for i in composit_num_dice:
    for j in prime_num_dice:
        num_of_cases.append(i * j)

print(num_of_cases.count(K) / 36)