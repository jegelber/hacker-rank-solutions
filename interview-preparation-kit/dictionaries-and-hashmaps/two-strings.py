# Score: 25/25

# Strategy: check if one char in common, rather than large substring
# Put each char of word into a Counter
# Subtract the counter, if subtracting returns

def twoStrings(s1, s2):
    if (set(s1) & set(s2)):
        return "YES"
    else:
        return "NO"

print(twoStrings("be", "cate"))
