#ABC-480B
#verdict: AC

candidates = []

def main():
    n, m = map(int, input().split())

    global candidates
    candidates = [input() for _ in range(n)]

    answer = [0 for _ in range(n)]
    for _ in range(m):
        index = who_gets_vote(input())
        if index:
            answer[index - 1] += 1
    
    print(*answer, sep='\n', end="")

def who_gets_vote(vote):
    def unmatched_positions(vote, candidate):
        return sum(a != b for a, b in zip(vote, candidate))
    
    cnt, index = 0, None
    for i, candidate in enumerate(candidates, 1):
        if vote == candidate:
            return i
        elif len(vote) == len(candidate):
            if unmatched_positions(vote, candidate) == 1:
                cnt += 1
                index = i
    
    if cnt == 1:
        return index
    else:
        return None

if __name__ == "__main__":
    main()