#ABC458-C

s = input()

print(
    sum(
        min(len(s) - i + 1, i)
        for i, c in enumerate(s, 1)
        if c == 'C'
    )
)