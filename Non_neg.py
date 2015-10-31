def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen=len(str)
    substr=str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result
