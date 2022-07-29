def solution(a):
    s = 0
    have = set(a)
    target = set(list(range(1, 10)))

    omitted = (target - have)
    for _ in list(omitted):
        s += _
    print(omitted)
    return s

print(solution([1, 2, 3, 4, 5]))
