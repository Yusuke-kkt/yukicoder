# yukicoder_no.63

L = int(input())
K = int(input())

eat_len = 0

if (L / 2) % K == 0:
    eat_len += ((L / 2) / K - 1) * K
else:
    eat_len += ((L / 2) // K) * K

print(eat_len)
