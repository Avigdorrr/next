def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


class UnderAge(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"Provided age is under 18.\ncurrently the age is {self._arg}, need to wait {str(18 - self._arg)} years"

    def get_arg(self):
        return self._arg