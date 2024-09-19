import pytest
from src.resources.authentifications.authentification import Auth
from src.transport.endpoint_account import EndpointAccount
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.accounts_assertions import AssertionAccounts


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_view_account_additional_headers(setup_account_view_account, get_headers):
    headers, account = setup_account_view_account
    additional_headers = {'header_extra': 'value_extra'}
    headerse = Auth().get_valid_user_headers(get_headers, additional_headers)
    response = EspocrmRequest().get(EndpointAccount.view(account['id']), headerse)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_view_account_incorrect_http_method(setup_account_view_account):
    headers, account = setup_account_view_account
    response = EspocrmRequest().post(EndpointAccount.view(account['id']), headers)
    AssertionStatusCode().assert_status_code_405(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_view_account_correct(setup_account_view_account):
    headers, account = setup_account_view_account
    response = EspocrmRequest().get(EndpointAccount.view(account['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_view_account_incorrect_authorization(setup_account_view_account, get_headers):
    headers, account = setup_account_view_account
    headersInvalid = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointAccount.view(account['id']), headersInvalid)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_view_account_id_not_exists(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointAccount.view(account_id="id_no_existente"), headers)
    AssertionStatusCode().assert_status_code_404(response)
