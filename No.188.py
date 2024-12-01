# yukicoder_no.188

happy_day = 0

for month in range(1, 13):
    if month == 2:
        day_max = 28
    elif month == 4 or 6 or 9 or 11:
        day_max = 30
    else:
        day_max = 31
    for day in range(1, day_max + 1):
        if month == (day // 10) + (day % 10):
            happy_day += 1

print(happy_day)

# '=' と '==' の違いは？
# 'month' は '==' にしないと SyntaxError になる
# day_max' は '=' でも問題ない

