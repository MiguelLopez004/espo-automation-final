import pytest
from src.transport.endpoint_account import EndpointAccount
from src.resources.payloads.payloads_account import PayloadAccount
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.accounts_assertions import AssertionAccounts
from src.resources.authentifications.authentification import Auth


@pytest.mark.regression
@pytest.mark.functional
def test_add_account(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity= "prueba",
                                                                 billingAddressCountry="prueba", billingAddressPostalCode="prueba",
                                                                 billingAddressState="prueba", billingAddressStreet="prueba",
                                                                 description="prueba", emailAddress="prueba@prueba.com",
                                                                 industry="Architecture", phoneNumber="+15555555555",
                                                                 shippingAddressCity="prueba", shippingAddressCountry="prueba",
                                                                 shippingAddressPostalCode="prueba", shippingAddressState="prueba",
                                                                 shippingAddressStreet="prueba", type="Customer", website="prueba.com")
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())
    created_account = response.json()
    created_accounts.append(created_account)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_account_duplicate_name(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity="prueba",
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
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())
    created_account = response.json()
    created_accounts.append(created_account)
    response1 = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_409(response1)
    created_account = response.json()
    created_accounts.append(created_account)



@pytest.mark.smoke
@pytest.mark.functional
def test_add_account_with_valid_user(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity="prueba",
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
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())
    created_account = response.json()
    created_accounts.append(created_account)


@pytest.mark.smoke
@pytest.mark.functional
def test_add_account_with_invalid_user(setup_add_account, get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity="prueba",
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
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_add_account_billingAddress_null(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva",
                                                                 description="prueba", emailAddress="prueba@prueba.com",
                                                                 industry="Architecture", phoneNumber="+15555555555",
                                                                 shippingAddressCity="prueba",
                                                                 shippingAddressCountry="prueba",
                                                                 shippingAddressPostalCode="prueba",
                                                                 shippingAddressState="prueba",
                                                                 shippingAddressStreet="prueba", type="Customer",
                                                                 website="prueba.com")
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())
    created_account = response.json()
    created_accounts.append(created_account)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_account_name_null(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(billingAddressCity="prueba",
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
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_400(response)
    created_account = response.json()
    created_accounts.append(created_account)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_account_phoneNumber_null(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity="prueba",
                                                                 billingAddressCountry="prueba",
                                                                 billingAddressPostalCode="prueba",
                                                                 billingAddressState="prueba",
                                                                 billingAddressStreet="prueba",
                                                                 description="prueba", emailAddress="prueba@prueba.com",
                                                                 industry="Architecture", phoneNumber="+1555sdfsd5555555",
                                                                 shippingAddressCity="prueba",
                                                                 shippingAddressCountry="prueba",
                                                                 shippingAddressPostalCode="prueba",
                                                                 shippingAddressState="prueba",
                                                                 shippingAddressStreet="prueba", type="Customer",
                                                                 website="prueba.com")
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_400(response)
    created_account = response.json()
    created_accounts.append(created_account)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_account_emailAddress_null(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity="prueba",
                                                                 billingAddressCountry="prueba",
                                                                 billingAddressPostalCode="prueba",
                                                                 billingAddressState="prueba",
                                                                 billingAddressStreet="prueba",
                                                                 description="prueba", emailAddress="prueba.com",
                                                                 industry="Architecture",
                                                                 phoneNumber="+15555555555",
                                                                 shippingAddressCity="prueba",
                                                                 shippingAddressCountry="prueba",
                                                                 shippingAddressPostalCode="prueba",
                                                                 shippingAddressState="prueba",
                                                                 shippingAddressStreet="prueba", type="Customer",
                                                                 website="prueba.com")
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_400(response)
    created_account = response.json()
    created_accounts.append(created_account)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_account_website_invalid(setup_add_account):
    headers, created_accounts = setup_add_account
    payload_account = PayloadAccount().build_payload_add_account(name="prueba nueva", billingAddressCity="prueba",
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
                                                                 website="prueba")
    response = EspocrmRequest().post(EndpointAccount.account(), headers, payload_account)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionAccounts().assert_account_view_schema_file(response.json())
    created_account = response.json()
    created_accounts.append(created_account)