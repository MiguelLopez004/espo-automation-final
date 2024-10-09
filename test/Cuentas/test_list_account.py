import pytest
from src.resources.authentifications.authentification import Auth
from src.transport.api_request import EspocrmRequest
from src.transport.endpoint_account import EndpointAccount
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.accounts_assertions import AssertionAccounts


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_list_accounts_with_data(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_order_asc(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_accounts_order_invalid(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(order='ASCSA'), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionAccounts().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_order_desc(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_without_select(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(select=None), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionAccounts.assert_account_list_without_select_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_select_unknown(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(select="unknown"), headers)
    AssertionSchemas().assert_field_list_no_empty(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_select_special(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(select="***"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_field_list_no_empty(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_invalid_authentication(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointAccount.list(), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionAccounts().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_maxsize_major_total(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(maxSize=200), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionAccounts().assert_account_list_schema_file(response.json())
    AssertionSchemas().assert_field_list_no_empty(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_maxsize_cero(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(maxSize=0), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionAccounts().assert_account_list_schema_file(response.json())
    AssertionAccounts().assert_empty_field_list(response.json())

@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_accounts_maxsize_negative(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(maxSize=-1), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionAccounts.assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_accounts_maxsize_string(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(maxSize="as"), headers)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_offset_major_total(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(offset=200), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionAccounts().assert_account_list_schema_file(response.json())
    AssertionAccounts().assert_empty_field_list(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_offset_cero(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(offset=0), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionAccounts().assert_account_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_accounts_offset_negative(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(offset=-1), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionAccounts.assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_accounts_offset_string(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(offset="as"), headers)
    AssertionStatusCode().assert_status_code_400(response)

@pytest.mark.regression
@pytest.mark.functional
def test_list_accounts_ordeby_unknown(setup_teardown_list_account):
    headers, account1, account2, account3 = setup_teardown_list_account
    response = EspocrmRequest().get(EndpointAccount.list(orderBy='unknown'), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionAccounts.assert_response_empty(response.text)