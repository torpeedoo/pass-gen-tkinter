import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
specialChars = "!@#$%^&*()?<>"
def gen_pass(length, isUpper, isSpecial):
    passwd = []
    print(isUpper, isSpecial)
    if length>0:
        for char in range(length):
            special = random.randint(0,1)
            upper = random.randint(0, 1)
            if special and isSpecial == 1:
                passwd.append(random.choice(specialChars))  
            else:
                if upper and isUpper == 1:
                    passwd.append(random.choice(alphabet.upper()))
                else:
                    passwd.append(random.choice(alphabet))
        return "".join(passwd)
    else: return "Length must be more than 0"


