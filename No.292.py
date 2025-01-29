# yukicoder_no.292

nickname = str(input())

B_advice, C_advice = map(int, (input().split()))

if B_advice == C_advice:
    print(nickname[:B_advice] + nickname[B_advice + 1:]) 
elif B_advice < C_advice:
    print(nickname[:B_advice] + nickname[B_advice + 1:C_advice] + nickname[C_advice + 1:])
else:
    print(nickname[:C_advice] + nickname[C_advice + 1:B_advice] + nickname[B_advice + 1:])