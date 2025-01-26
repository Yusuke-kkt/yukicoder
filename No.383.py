# yukicoder_no.383

a, b = map(int, input().split())

if a > b:
    print("-" + str(a - b))
else:
    print(a - b)

# 別解
if a > b:
    print(f"-{a - b}")
else:
    print(a - b)

# 別解
if a == b:
    pass
elif a > b:
    print("-", end="")
else:
    print("+", end="")
print(abs(a-b))

# なんで正解が出力される？
# python は出力の末尾がデフォルトで改行 (\n) になっている
# end = "" により "\n" を "" に置換 (改行しなくなる)
# 最後の print(abs(a-b)) が print("-", end="") の末尾まで詰められた状態で出力される