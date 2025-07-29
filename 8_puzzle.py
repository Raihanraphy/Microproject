from collections import deque

goal = '123456780'
moves = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}

def solve(start):
    q = deque([(start, start.index('0'))])
    seen = {start}
    while q:
        state, i = q.popleft()
        if state == goal:
            return "Solved!"
        for j in moves[i]:
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            new = ''.join(lst)
            if new not in seen:
                seen.add(new)
                q.append((new, j))
    return "Unsolvable"

# Example: scrambled puzzle where '0' is the blank
print(solve("123405678"))
