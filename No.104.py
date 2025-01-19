# yukicoder_no.104

route_memory = str(input())
national_highway = 1

for RL_checker in route_memory:
    if RL_checker == "L":
        national_highway = national_highway * 2
    else:
        national_highway = national_highway * 2 + 1

print(national_highway)