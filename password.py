class Password:
    """
    A class representing a single password entry in the password manager.
    """
    def __init__(self, website, username, password):
        """
        Initialize the password object with the specified website, username, and password.
        """
        self.website = website
        self.username = username
        self.password = password

    def __str__(self):
        """
        Convert the password object to a string representation.
        """
        return f"Website: {self.website}\nUsername: {self.username}\nPassword: {self.password}"
