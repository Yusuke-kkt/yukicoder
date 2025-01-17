# yukicoder_no.485

A = int(input())
B = int(input())

if (B /A).is_integer():
    print(B // A)
else:
    print("NO")

# .is_integer(): float型の数値の小数点以下が0かどうか判定する(= float型の数値が整数かどうか判定する)
# 例えば、"4" は整数だが、"4.0" のことは整数だと認識されない。
# 出力が整数になるようにコードを書かないといけない

# 別解
if (B % A) == 0:
    print(B // A)
else:
    print("NO")

# 関数を使わずに簡潔に記述されている