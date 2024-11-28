# yukicoder_no.32

# L = 100円硬貨, M = 25円硬貨, N = 1円硬貨

L = int(input())
M = int(input())
N = int(input())

M = M + N // 25
L = (L + M // 4) % 10
M = M % 4
N = N % 25
print(L + M + N)

# 上から順番に計算が処理されていくことを意識する
# もっと綺麗に書けそう