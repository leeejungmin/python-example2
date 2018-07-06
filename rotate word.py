import string
def ro_letter(ll,n):
    if ll.isupper():
        start=ord("A")
    elif ll.islower():
        start=ord('a')
    else:
        return ll
    c=ord(ll)-start
    i=(c+n)%26+start
    return chr(i)
def ro_word(word,n):
    res=''
    for ll in word:
        res += ro_letter(ll,n)
    return res

if __name__ =='__main__':
    print(ro_word('cheer',7))
    print(ro_word('melon',-10))
    print(ro_word('sleep',9))
    
