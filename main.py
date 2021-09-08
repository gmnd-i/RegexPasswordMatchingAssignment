import re

def pwdMatch(pwd):
    if re.fullmatch(".*?[A-Z].*[A-Z].*", pwd) and re.fullmatch(".*?[0-9].*[0-9].*", pwd) and re.fullmatch( ".{10,}", pwd):
        return True;
    else :
        return False;

#7 test cases
print (1, pwdMatch("a00aAaaaAa")); #matches
print (2, pwdMatch("aAa0aAa0")); #not match len = 8
print (3, pwdMatch("aAa0aAa0aa")); #match. same as above but len = 10
print (4, pwdMatch("aaaaaaaaaa")); #not match. len = 10 but no upper case or digits
print (5, pwdMatch("aaaAaaAaaaaa")); #not match. len = 12 but no digits
print (6, pwdMatch("aaaAaaAaaa1a")); #not match. len = 12 but only 1 digit
print (7, pwdMatch("1aaAaaAaaa1a")); #match. len = 12
