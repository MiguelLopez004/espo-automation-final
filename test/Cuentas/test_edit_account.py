import pytest

from src.assertions.accounts_assertions import AssertionAccounts
from src.transport.endpoint_account import EndpointAccount
from src.resources.payloads.payloads_account import PayloadAccount
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.resources.authentifications.authentification import Auth
from data.accounts import create_account_data


@pytest.mark.regression
@pytest.mark.functional
def test_edit_account_all_data(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_edit_account_address_data(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_edit_account_field_unknow(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba", test="test",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_edit_account_empty_data(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry=" ",
                               billingAddressPostalCode=" ",
                               billingAddressState=" ",
                               billingAddressStreet=" ",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_edit_account_email_invalid(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="pruebacom",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_edit_account_phoneNumber_invalid(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+1555dsf5555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_edit_account_addressShipping_invalid(setup_edit_account):
    headers, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="null",
                               shippingAddressCountry="null",
                               shippingAddressPostalCode="null",
                               shippingAddressState="null",
                               shippingAddressStreet="null", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.smoke
@pytest.mark.functional
def test_edit_account_with_invalid_user(setup_edit_account, get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    headers_valid, account = setup_edit_account
    data = create_account_data(name="prueba nueva", billingAddressCity="prueba",
                               billingAddressCountry="prueba",
                               billingAddressPostalCode="prueba",
                               billingAddressState="prueba",
                               billingAddressStreet="prueba",
                               description="prueba", emailAddress="prueba@prueba.com",
                               industry="Architecture", phoneNumber="+15555555555",
                               shippingAddressCity="prueba",
                               shippingAddressCountry="prueba",
                               shippingAddressPostalCode="prueba",
                               shippingAddressState="prueba",
                               shippingAddressStreet="prueba", type="Customer",
                               website="prueba.com")
    response = EspocrmRequest().put(EndpointAccount.view(account['id']), headers, data)
    AssertionStatusCode().assert_status_code_401(response)
