def removeDup(s):
    res = []

    for c in s:
        if res and res[-1] == c:
            print(res)
            res.pop()
        else:
            res.append(c)

    return ''.join(res)

removeDup("abbaca")

