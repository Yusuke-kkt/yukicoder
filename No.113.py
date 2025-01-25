# yukicoder_no.113

NEWS_strings = str(input())
X_cordinate = 0
Y_cordinate = 0

for i in NEWS_strings:
    if i == "N":
        Y_cordinate += 1
    elif i == "E":
        X_cordinate += 1
    elif i == "W":
        X_cordinate -= 1
    else:
        Y_cordinate -= 1

import math
print(math.sqrt(X_cordinate ** 2 + Y_cordinate ** 2))