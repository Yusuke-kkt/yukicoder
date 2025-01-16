D = list(map(int, input().split()))
S = int(input())

if S == 1:
    print("SURVIVED")
elif 2 <= sum(D) and S == 0:
    print("DEAD")
else:
    print("SURVIVED")

# 別解
D1, D2, D3, S = map(int, input().split())

if S == 1:
    print("SURVIVED")
elif D1 + D2 + D3 < 2:
    print("SURVIVED")
else:
    print("DEAD")

# 別解の方が分かりやすい
# D と S を一行で簡潔に記述している (わざわざリスト化していない)
# sum() なんか使わなくていい (総和 = sum の思考回路が、sum を使いたいがための無駄なリスト化を生んだ)
# else が "DEAD"の方が並びが美しい