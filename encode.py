class Encoder:
    def encode(self, password):
        new_password = ""
        for char in password:
            new_password += str(int(char) + 3)
        return new_password
