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
    a=len(s1)%2
    b=len(s2)%2
    c=len(s3)%2

    if a or b or c ==1 :
        return "["+str(s1*a)+", "+str(s2*b)+", "+str(s3*c)+ "]"
    else: return "["+"]"

print(main("zdf","acsd", "ab"))


