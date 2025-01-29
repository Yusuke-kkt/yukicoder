# yukicoder_no.292

nickname = str(input())

B_advice, C_advice = map(int, (input().split()))

if B_advice == C_advice:
    print(nickname[:B_advice] + nickname[B_advice + 1:]) 
elif B_advice < C_advice:
    print(nickname[:B_advice] + nickname[B_advice + 1:C_advice] + nickname[C_advice + 1:])
else:
    print(nickname[:C_advice] + nickname[C_advice + 1:B_advice] + nickname[B_advice + 1:])



# 別解
Nickname = list(nickname)

if B_advice > C_advice:
    Nickname.pop(B_advice)
    Nickname.pop(C_advice)
elif B_advice < C_advice:
    Nickname.pop(C_advice)
    Nickname.pop(B_advice)
else:
    Nickname.pop(B_advice)
    
print(''.join(Nickname))

# pop(): リストの最後の要素を抽出し、削除。インデックスを指定して抽出、削除も可能。
# .join: リストの要素を結合

# 別解とやってる操作は変わらないが、記述は別解の方が簡潔
# B_advice と C_advice だけを抽出して削除している感が出ている