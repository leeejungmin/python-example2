def rotate_word(strg, n):
    n = n % len(strg)
    return strg[n:] + strg[:n]
