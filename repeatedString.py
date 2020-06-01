def repeatedString(s, n):
    lss=n%len(s)
    tfs=int(n/len(s))
    cnt=s.count('a')
    sc=s.count('a',0,lss)
    tc=(tfs*cnt)+sc
    return tc
