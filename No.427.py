# yukicoder_no.427

screen_height, screen_width = map(int, input().split())
if screen_height / screen_width == 3 / 4:
    print("YOKO")
else:
    print("TATE")

# == 3 / 4 を　== 0.75 にすると、ValueError: invalid literal for int() with base 10: '&'
# 小数が絡むと int はできない？

# 別解
if screen_height < screen_width:
    print("YOKO")
else:
    print("TATE")

#　問題分に忠実だと上の記述になるが、別解の方が簡潔に答えを出力できる