# yukicoder_no.138

a, b, c = map(int, input().split("."))
e, f, g = map(int, input().split("."))

if a < e:
    print("NO")
elif e < a:
    print("YES")
else:
    if b < f:
        print("NO")
    elif f < b:
        print("YES")
    else:
        if c < g:
            print("NO")
        else:
            print("YES")




# 最初に思いついた方法 (不正解)
# a, b, c = map(str, input().split())
# fossil_ver = a + "." + b + "." + c
# fossil_number = fossil_ver.replace(".", "")

# A, B, C = map(str, input().split())
# judged_ver = A + "." + B + "." + C
# judged_number = judged_ver.replace(".", "")

# if fossil_number < judged_number:
#     print("NO")
# else:
#     print("YES")

# もしこの方法でやるなら、100の位 * 1000000 + 10の位 * 1000 * 1の位 してから、fossil_number と judged_number を比べる
# そうしないと、仮に fossil_ver が 1.10.3 で、judged_ver が 10.1.0 のとき、"YES" が出力されてしまう
# 下記解答例
# a, b, c = map(int, input().split('.'))
# e, f, g = map(int, input().split('.'))

# abc = a * 1000000 + b * 1000 + c
# efg = e * 1000000 + f * 1000 + g

# if abc >= efg:
#     print('YES')
# else:
#     print('NO')


# 別解
# a=list(input().split("."))
# b=list(input().split("."))
# for i in range(3):
#     if a[i]==b[i]:continue
#     if int(a[i])>int(b[i]):
#         print("YES")
#         exit()
#     else:
#         print("NO")
#         exit()
# print("YES")