# yukicoder_no.5

# 箱の幅
L = int(input())
# ブロックの数
N = int(input())
# 各ブロックの幅
import random
block_widths = list([random.randint(1, L) for i in range(N)])
block_widths.sort()

max_blocks = 0
for i in block_widths:
    if block_widths <= L:
        max_blocks += 1
        L -= i
    else:
        break

print(max_blocks)

# 14行目の "<="" がエラーの原因
# おそらく, 9行目の "blocks_widths" が list なのに対し, 4行目の "L" が int のため.
# つまり, "block_widths" と "L" では型？が異なるため, "<=" を使えない？
# → list を int に変換する方法を探す？
