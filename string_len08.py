def main(s):
    """
    Given variable type string s. Return the character in the muddle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """

    if len(s)%2==1:
        return str(s[(len(s))//2])
    if len(s)%2==0:
        return str(s[(len(s))//2:(len(s)-1)//2])    

print(main("1278"))


