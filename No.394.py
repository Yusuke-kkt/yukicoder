# yukicoder_no.394

score_lis = list(int(input()) for i in range(6))
score_lis.sort()
score_lis.pop()
score_lis.pop(0)

print(sum(score_lis) / 4)