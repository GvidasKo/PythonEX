class Passwordtoshort(Exception):
    pass

class Passwordtolong(Exception):
    pass

class InvalidPassword(Exception):
    pass

# raise Passwordtolong("slaptazodis per ilgas")
tikras_pass = "slaptas"
def validate_password():
    input_pass = input("slaptazodis: ")
    if len(input_pass) < 3:
        raise Passwordtoshort("Password per trumpas")
    elif len(input_pass) > 30:
        raise Passwordtolong("Passwordas per ilgas")
    elif input_pass != tikras_pass:
        raise InvalidPassword("Netikras Passwardas")

try:
    validate_password()
except Passwordtoshort:
    print("Password per trumpas")
except Passwordtolong:
    print("Password per ilgas")
except InvalidPassword:
    print("Netikras Passwardas")