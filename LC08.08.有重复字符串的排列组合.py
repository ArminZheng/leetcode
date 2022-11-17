from typing import List


def permutation(S: str) -> List[str]:
    n = len(S)
    if not n:
        return [""]
    ans = []
    step = []
    source = sorted(list(S))

    def backtracking():
        if len(step) == n:
            ans.append("".join(step))
            return
        for i in range(n):
            if source[i] == None or i > 0 and source[i] == source[i-1]:
                continue
            tmp = source[i]
            source[i] = None
            step.append(tmp)
            backtracking()
            step.pop()
            source[i] = tmp
    backtracking()
    return ans


def permutation2(S: str) -> List[str]:
    n = len(S)
    res = []
    if not n:
        return [""]

    for i in range(n):  # q q e
        if S[i] in S[:i]:   # q q e in qe
            continue
        remain = S[:i] + S[i+1:]
        # if remain == [] ignore
        tmp = permutation2(remain)
        for x in tmp:  # s[:1] s[2:] 1 34567890 -> s[:8] s[9:]
            res.append(S[i] + x)
    return res


def permutation3(S: str) -> List[str]:
    n = len(S)
    if not n:
        return [""]
    
    ans = []
    path = []
    source = sorted(list(S))

    def backtracking(n, startindex):
        if len(path) == n:
            ans.append("".join(path))
            return
        for i in range(startindex, n):
            # push
            path.append(source[i])
            backtracking(n, i + 1)
            path.pop()
    backtracking(n, 0)
    return ans


# print(permutation("qqe"))
# print(permutation2("qqe"))
print(permutation3("qqe"))
