class GreetingCard:

    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"the sender is: {self._sender}, and the recipient is: {self._recipient}")
