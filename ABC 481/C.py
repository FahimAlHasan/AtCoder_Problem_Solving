#ABC481 - A
#verdict: AC

ID = 1
accounts = {}
for _ in range(int(input())):
    name = input()
    if name not in accounts:
        accounts[name] = ID
        ID += 1
    print(accounts[name])