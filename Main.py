
SECURE = (('s','$'),('and','&'),('a','@'),('i','1'),('o','0'),('0','*'))
def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

if __name__ == '__main__':
    password = input("Enter your password : ")
    password = securePassword(password)
    print(f"Your secure password is : {password}")