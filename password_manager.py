import database
import encryption
import password_generator

class PasswordManager:
    """
    A password manager class that handles password encryption and storage.
    """
    def __init__(self, username, password):
        """
        Initialize the password manager with the specified username and password.
        """
        self.username = username
        self.password = password
        self.db = database.Database()
        self.crypto = encryption.Encryption(self.password)

    def add_password(self, website, username, password=None):
        """
        Add a new password entry to the password manager.
        """
        if password is None:
            password = password_generator.generate_password()
        encrypted_password = self.crypto.encrypt(password)
        self.db.insert_password(website, username, encrypted_password)

    def get_password(self, website, username):
        """
        Retrieve the password for the specified website and username.
        """
        encrypted_password = self.db.get_password(website, username)
        if encrypted_password is None:
            return None
        return self.crypto.decrypt(encrypted_password)

    def update_password(self, website, username, password=None):
        """
        Update the password for the specified website and username.
        """
        if password is None:
            password = password_generator.generate_password()
        encrypted_password = self.crypto.encrypt(password)
        self.db.update_password(website, username, encrypted_password)

    def delete_password(self, website, username):
        """
        Delete the password entry for the specified website and username.
        """
        self.db.delete_password(website, username)
