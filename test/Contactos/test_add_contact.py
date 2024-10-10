import pytest
from src.transport.endpoint_contact import EndpointContacts
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.contacts_assertions import AssertionContacts
from src.resources.authentifications.authentification import Auth
from data.contacts import create_contact_data


@pytest.mark.regression
@pytest.mark.functional
def test_add_contact(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data()
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_duplicate_name(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data()
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)
    response1 = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_409(response1)
    created_contact = response.json()
    created_contacts.append(created_contact)



@pytest.mark.smoke
@pytest.mark.functional
def test_add_contact_with_valid_user(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data()
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.smoke
@pytest.mark.functional
def test_add_contact_with_invalid_user(setup_add_contact, get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    created_contact = setup_add_contact
    data = create_contact_data()
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_add_contact_address_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data(addressCity= None,
                        addressCountry= None,
                        addressPostalCode= None,
                        addressState= None,
                        addressStreet= None)
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_firstName_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data()
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_lastName_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data(lastName="null")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_phoneNumber_invalid(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data(phoneNumber="+1794565sss4564")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_emailAddress_invalid(setup_add_contact):
    headers, created_contacts = setup_add_contact
    data = create_contact_data(emailAddress="one@on")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, data)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)