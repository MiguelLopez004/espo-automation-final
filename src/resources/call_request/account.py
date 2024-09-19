from src.transport.endpoint_account import EndpointAccount
from src.transport.api_request import EspocrmRequest


class AccountCall:
    @classmethod
    def view(cls, headers, account_id):
        response = EspocrmRequest().get(EndpointAccount.view(account_id), headers)
        return response.json()

    @classmethod
    def create(cls, headers, payload):
        response = EspocrmRequest().post(EndpointAccount.account(), headers, payload)
        return response.json()

    @classmethod
    def update(cls, headers, payload, account_id):
        response = EspocrmRequest().put(EndpointAccount.view(account_id), headers, payload)
        return response.json()

    @classmethod
    def delete(cls, headers, account_id):
        response = EspocrmRequest().delete(EndpointAccount.view(account_id), headers)
        return response.json()