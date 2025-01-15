# yukicoder_no.296

N = int(input())
H = int(input())
M = int(input())
T = int(input())

print((H * 60 + T * (N - 1) + M) // 60 % 24)
print((H * 60 + T * (N - 1) + M) % 60)

# いつまでも計算に頼らず、もっと関数とかを使うことに慣れていったほうがいいのでは？