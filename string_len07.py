def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=s1
    b=s2
    c=s3
    if len(a)%2==1 :
        a=s1
    elif len(a)%2==0:
        a=s1[0:1:-1]
    if len(b)%2==1 :
        b=s2
    elif len(b)%2==0:
        b=s2[0:1:-1]
    if len(c)%2==1 :
        c=s3
    elif len(c)%2==0:
        c=s3[0:1:-1]
    '''a=s1[0:len(a+1):]
    b=s2[0:len(b+1):]
    c=s3[0:len(c+1):]'''

    if a or b or c ==1 :
        return "["+str(a)+", "+str(b)+", "+str(c)+ "]"
    else: return "["+"]"

print(main("df3","acsd", "ab"))


