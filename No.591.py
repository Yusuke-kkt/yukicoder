# yukicoder_no.591

eyes = input()
mouth = input()
print("(" + eyes + mouth + eyes + ")" + "/")

# 別解
print(f"({eyes}{mouth}{eyes})/")
# f-strings: f"{}" 変数の値を文字列に挿入