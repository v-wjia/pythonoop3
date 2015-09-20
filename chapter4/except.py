__author__ = 'Administrator'

import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.__encrypt_pw(password)
        self.is_logged_in = False

    def __encrypt_pw(self, password):
        hash_string = (self.username + self.password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self.__encrypt_pw(password)
        return  encrypted == self.password


class AuthException(Exception):
    def __int__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        try:
            perm_name = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exists")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotloggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

class NotloggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


Authorizor = Authorizor(Authenticator)


class PermissionError(Exception):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass







