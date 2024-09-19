import pytest

from src.resources.authentifications.authentification import Auth
from src.resources.payloads.payloads_account import PayloadAccount
from src.resources.call_request.account import AccountCall


@pytest.fixture(scope="function")
def setup_teardown_list_account(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)

    payload_account_1 = PayloadAccount().build_payload_add_account(name="prueba")
    payload_account_2 = PayloadAccount().build_payload_add_account(name="prueba1")
    payload_account_3 = PayloadAccount().build_payload_add_account(name="prueba2")

    account1 = AccountCall().create(headers, payload_account_1)
    account2 = AccountCall().create(headers, payload_account_2)
    account3 = AccountCall().create(headers, payload_account_3)

    if isinstance(account1, list):
        account1 = account1[0]
    if isinstance(account2, list):
        account2 = account2[0]
    if isinstance(account3, list):
        account3 = account3[0]

    yield headers, account1, account2, account3

    AccountCall().delete(headers, account1['id'])
    AccountCall().delete(headers, account2['id'])
    AccountCall().delete(headers, account3['id'])


@pytest.fixture(scope="function")
def setup_add_account(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    created_accounts = []
    yield headers, created_accounts

    for account in created_accounts:
        AccountCall().delete(headers, account['id'])


@pytest.fixture(scope="function")
def setup_contact_delete_account(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva")
    account = AccountCall().create(headers, payload_account)
    yield headers, account


@pytest.fixture(scope="function")
def setup_edit_account(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva")
    account = AccountCall().create(headers, payload_account)
    yield headers, account
    AccountCall().delete(headers, account['id'])


@pytest.fixture(scope="function")
def setup_create_account(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva")
    account = AccountCall().create(headers, payload_account)
    yield headers, account


@pytest.fixture(scope="function")
def setup_account_view_account(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva")
    account = AccountCall().create(headers, payload_account)
    yield headers, account
    AccountCall().delete(headers, account['id'])