# yukicoder_no.418

cicada_strings = str(input())
min_strings = cicada_strings.replace("-", "")

import re
min_lis = re.findall("min", min_strings)
print(len(min_lis))


# 別解 1
print(min_strings.count("min"))


# 別解 2
print(cicada_strings.count("m"))

# "-" を削除する手間がない。


# 別解 (s が t の中に重複を許して何回登場するか)
s = "min"
t = min_strings
cnt = 0
for i in range(len(t)):
    if s == t[i:i+len(s)]:
        cnt += 1
print(cnt)