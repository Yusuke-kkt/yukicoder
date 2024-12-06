# yukicoder_no.18

# N = [str(input().upper())] # BCD to AAA, ABC to ZZZ

N = list(map(str, input().split())) # ['A', 'B', 'C']

for ALP in N[0:]:
    # print(ord(ALP))        # 65 66 67
    # print(ord(ALP) - 1)    # 64 65 66
    # print(chr(ord(ALP)))   # A B C
    # if 65 <= ord(ALP) - 1:
        # print(chr(ord(ALP)))    # B C
    print(ord(ALP) - i + 1 for i in range(len(N)))

# ALP = [chr(i) for i in range(65, 91)]




# chr, 65 to 91
# ord, A to Z







# print(ALP.index("A"))






# n = str(input())
# N = n.upper()

# import string
# ALP_lis = list(string.ascii_uppercase)


# print(ALP_lis.index(S))



# 何が違う？
# N = [map(str, input().split()]
#     → <map object at 0x0000018BA173A0D0>
# N = list(map(str, input().split()))
#     →['A', 'B', 'C']