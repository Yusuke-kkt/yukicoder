# yukicoder_no.29

item_lis = []
power_up_cnt = 0

N = int(input())

for i in range(N):
    a, b, c = map(int, input().split())
    item_lis.append(a)
    item_lis.append(b)
    item_lis.append(c)

# 何をやってる？
# 例えば 1 2 3 と入力したとき、a, b, c に対応するのはどれ？
# sort()を使わなかった場合 [1, 2, 3, 1, 2, 3] になる
# [1, 1, 2, 2, 3, 3] になると思ってた (つまり、a = 1, b = 2, c = 3 だと思ってたが、違うっぽい？)

item_lis.sort()
print(item_lis)




# item_ lis = list(map(int, input().split) for i in range(N))
# → [<map object at 0x000001C453E4A0D0>, <map object at 0x000001C453EA5340>, <map object at 0x000001C453EA53D0>]