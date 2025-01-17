# yukicoder_no.369

N = int(input())
yuki_answer = int(input())
correct_answer = sum(map(int, input().split()))
print(correct_answer - yuki_answer)

# list(map(int, input().split())) の解答が多かったが、なぜわざわざリスト化しているのか？