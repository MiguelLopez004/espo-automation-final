import pytest
import random
import string
from src.resources.authentifications.authentification import Auth
from src.transport.endpoint_account import EndpointAccount
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.accounts_assertions import AssertionAccounts
from src.resources.call_request.account import AccountCall


@pytest.mark.smoke
@pytest.mark.functional
def test_delete_account_valid_contact(setup_create_account):
    headers, account = setup_create_account
    response = EspocrmRequest().delete(EndpointAccount.view(account['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_response_true(response)


@pytest.mark.functional
def test_delete_account_invalid_user(setup_create_account, get_headers):
    headers, account = setup_create_account
    headersAux = headers
    headers = Auth().get_unauthorized_users_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointAccount.view(account['id']), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AccountCall().delete(headersAux, account['id'])


@pytest.mark.functional
def test_delete_account_nonexistent_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    user_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    response = EspocrmRequest().delete(EndpointAccount.view(user_id_invalid), headers)
    AssertionStatusCode().assert_status_code_404(response)


@pytest.mark.smoke
@pytest.mark.functional
def test_delete_account_valid_with_auth_incorrect(setup_create_account, get_headers):
    headers, account = setup_create_account
    headersAux = headers
    headers = Auth().get_unauthorized_users_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointAccount.view(account['id']), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AccountCall().delete(headersAux, account['id'])