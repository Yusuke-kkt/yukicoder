# yukicoder_no.169

import math

K = int(input()) # Kは%の値
S = int(input())
print(math.floor((S / (100 - K)) * 100)) # 残りminutes / 残り%