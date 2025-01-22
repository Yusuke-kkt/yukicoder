# yukicoder_no.418

cicada_strings = str(input() + "m")
min_strings = cicada_strings.replace("-", "")
print(cicada_strings)
print(min_strings)

import re
min_lis = re.findall("[m+][i+][n+]m", min_strings)
print(min_lis)
print(len(min_lis))

# 蝉の鳴き声 = "min" の出現回数を数える
# 最後が "n" で終わる文字列でなければならない(つまり "minn" や "mini" は "min" としてカウントしてはいけない)
# → "min" に続く文字が "m" でなければならない
# → "minm" の数を数えればいいのでは？
# "minm" を重複を許して数えるにはどうすればいいか





# 別解 (s が t の中に重複を許して何回登場するか)
# s = input() 
# t = input()
# cnt = 0
# for i in range(len(t)):
    # if s == t[i:i+len(s)]:
        # cnt += 1
# print(cnt)