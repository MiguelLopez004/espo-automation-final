from src.utils.load_resources import load_credential_resource


class Auth:
    def __init__(self):
        self.users = self.load_file()

    @staticmethod
    def load_file():
        return load_credential_resource("users.json")

    def get_user(self, user_type):
        return self.users.get(user_type)

    def build_headers(self, get_headers, user_type, additional_headers=None):
        user = self.get_user(user_type)
        headers = get_headers(user["username"], user["password"])
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def get_valid_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "valid_user", additional_headers)

    def get_invalid_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "invalid_user", additional_headers)

    def get_disabled_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "disabled_user", additional_headers)

    def get_empty_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "empty_user", additional_headers)

    def get_unauthorized_users_user_headers(self, get_headers, additional_headers=None):
        return self.build_headers(get_headers, "unauthorized_users_user", additional_headers)