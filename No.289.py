# yukicoder_no.289

S = input()

total = 0

for i in S:
    if i.isdigit():
        total += int(i)
print(total)

# isdigit(): 文字列の中身が正の整数か判定する


# 別解
total = 0

for i in S:
    if i in "123456789":
        total += int(i)
print(total)

# if i in :特定の値が含まれているか判定
