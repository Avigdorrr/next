from string import punctuation

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg, index):
        self._arg = arg
        self._index = index

    def __str__(self):
        return f"Provided illegal character for username. the character is: {self._arg} at index: {self._index}"


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The provided username is too short and must have at least 3 characters. the length that provided is: {self._arg}"


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The provided username is too long and must have at most 16 characters. the length that provided is: {self._arg}"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return f"The provided password does not include one of the mandatory characters. the character that missing is: "


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Special)"


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The provided password is too short and must have at least 8 characters. the length that provided is: {self._arg}"


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"The provided password is too long and must have at most 40 characters. the length that provided is: {self._arg}"


def check_input(username, password):
    try:
        for char in username:
            if not char.isalnum() and char != "_":
                raise UsernameContainsIllegalCharacter(char, username.index(char))
        if 3 > len(username):
            raise UsernameTooShort(len(username))
        if 16 < len(username):
            raise UsernameTooLong(len(username))

        if 8 > len(password):
            raise PasswordTooShort(len(password))
        if 40 < len(password):
            raise PasswordTooLong(len(password))

        has_uppercase = False
        has_lowercase = False
        has_number = False
        has_special_char = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_number = True
            elif char in string.punctuation:
                has_special_char = True
        if not all([has_uppercase, has_lowercase, has_number, has_special_char]):
            if not has_uppercase:
                raise PasswordMissingUppercase
            if not has_lowercase:
                raise PasswordMissingLowercase
            if not has_number:
                raise PasswordMissingDigit
            if not has_special_char:
                raise PasswordMissingSpecial

    except Exception as e:
        print(e)
        return False

    else:
        print("OK")
        return True


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

    username =input("enter user name: ")
    password = input("enter password: ")
    while not check_input(username, password):
        print("lets try again :)")
        username = input("enter user name: ")
        password = input("enter password: ")


if __name__ == '__main__':
    main()