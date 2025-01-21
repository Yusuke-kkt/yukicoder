# yukicoder_no.400

S = str(input())
mirror_S =""

for mirror in S:
    if mirror == "<":
        mirror_S += ">"
    else:
        mirror_S += "<"

print(mirror_S)

# mirror_S をリストにして .append() を使おうとした
# → print(mirror_S) ではリスト形式で出力されてしまう
# → 上記のように改善した