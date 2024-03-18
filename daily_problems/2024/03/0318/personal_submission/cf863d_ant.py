n, q, m = map(int, input().split())
nums = list(map(int, input().split()))
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
important_indices = list(map(lambda x: int(x) - 1, input().split()))

for type, l, r in queries[::-1]:
    if type:
        for i in range(m):
            if l <= important_indices[i] <= r:
                important_indices[i] = l + r - important_indices[i]
    else:
        for i in range(m):
            if l < important_indices[i] <= r:
                important_indices[i] -= 1
            elif important_indices[i] == l:
                important_indices[i] = r

print(' '.join(map(str, (nums[p] for p in important_indices))))
