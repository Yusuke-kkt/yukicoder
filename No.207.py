# yukicoder_no.207

A = int(input())
B = int(input())

if 1 <= A <= B <= 2000000000 and 0 <= B - A < 100:
    for i in range (A,B):
        if i % 3 == 0 or "3" in str(i):
            print(i)
