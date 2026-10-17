#ABC-480A

row = [input() for _ in range(2)]

col = [row[0][0] + row[1][0], row[0][1] + row[1][1]]

if "AD" in row or "AD" in col:
    print("Yes")
elif "DA" in row or "DA" in col:
    print("Yes")
else:
    print("No")