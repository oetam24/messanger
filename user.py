class User:
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        self.messages = []
        self.controller = controller

    def send_message(self, nickname_to, text):
        pass

    def print_messages(self):
        for message in selg.messages
            print(f'*    {message.from_user} - {message.timestamp}')
            print(message.text)
            print()


