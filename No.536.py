# yukicoder_no.536

ID = str(input())

if ID[-2:] == "ai":
    print(ID[0:-2], end = "")
    print(ID[-2:].upper())
else:
    print(ID + "-AI")

# [start:stop]: インデックスを渡して文字列の位置を指定


# 別解
ID = input()
if ID[-2:] == "ai":
    print(ID[:-2]+"AI")
else:
    print(ID+"-AI")

# 別解のほうが簡潔
# 文字列の末尾を大文字に変換するという思考にとらわれず、末尾の2文字までを出力し、そこに "AI" を加えている。