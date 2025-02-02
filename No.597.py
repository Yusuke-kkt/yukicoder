# yukicoder_no.597

N = int(input())
word_list = list(str(input()) for i in range(N))
joined_word = "".join(word_list)


# 別解
s = ""
for _ in range(int(input())):
	s += input()
print(s)