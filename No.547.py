# yukicoder_no.547

N = int(input())
word_list_1 = list(str(input()) for i in range(N))
word_list_2 = list(str(input()) for j in range(N))

for word in range(N):
    if word_list_1[word] != word_list_2[word]:
        print(word + 1)

print(*set(word_list_1) - set(word_list_2))
print(*set(word_list_2) - set(word_list_1))


# "*" を入れることで｛｝などの括弧を外して出力できる
# set型
# set(A) - set(B) : 要素Aから要素Bを引いた差集合


# 別解
for i in range(N):
    if word_list_1[i] != word_list_2[i]:
        print(i+1)
        print(word_list_1[i])
        print(word_list_2[i])

# 要素のインデックス番号を取得するという考えに縛られない。