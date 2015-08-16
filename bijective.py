def is_bijective(s):
    """ Checks if the s box is bijective """
    for i in range(len(s)):
        if i not in s:
            print(i)
            return False
    return True
