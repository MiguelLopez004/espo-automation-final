from enum import Enum
from config.config import BASE_URI


class Endpoint(Enum):
    LOGIN = "/App/user"
    BASE_CONTACT = "/Contact"
    BASE_CONTACT_VIEW = "/Contact/{contact_id}"
    BASE_ACCOUNT = "/Account"
    BASE_ACCOUNT_VIEW = "/Account/{account_id}"


    @classmethod
    def login(cls):
        return f"{BASE_URI}{cls.LOGIN.value}"

