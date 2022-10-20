for i in d:
        res += (num//i) * d[i]
        num %= i
    return res 