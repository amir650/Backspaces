def clean_string(s):
    result = []
    for c in s:
        if c == "#":
            if len(result) > 0 :
                result.pop()
        else:
            result.append(c)

    return "".join(result)