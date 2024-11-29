# yukicoder_no.264

# ぐー = 0, ちょき = 1, ぱー = 2

you = int(input())
enemy = int(input())

if int(you) == int(enemy):
    print("Drew")
elif int(you) == 0 and int(enemy) == 1:
    print("Won")
elif int(you) == 1 and int(enemy) == 2:
    print("Won")
elif int(you) == 2 and int(enemy) == 0:
    print("Won")
else:
    print("Lost")

# 0, 1, 2, 以外を入力できないようにするには？