import pytest
from src.transport.endpoint_contact import EndpointContacts
from src.resources.payloads.payloads_contacts import PayloadContact
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.contacts_assertions import AssertionContacts
from src.resources.authentifications.authentification import Auth


@pytest.mark.regression
@pytest.mark.functional
def test_add_contact(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_duplicate_name(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)
    response1 = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_409(response1)
    created_contact = response.json()
    created_contacts.append(created_contact)



@pytest.mark.smoke
@pytest.mark.functional
def test_add_contact_with_valid_user(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.smoke
@pytest.mark.functional
def test_add_contact_with_invalid_user(setup_add_contact, get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    created_contact = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_401(response)


@pytest.mark.regression
@pytest.mark.functional
def test_add_contact_address_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_add_contact_schema_schema_file(response.json())
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_firstName_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_lastName_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_phoneNumber_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+1794565sss4564",
                                                         addressPostalCode="0000",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_add_contact_emailAddress_null(setup_add_contact):
    headers, created_contacts = setup_add_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000",
                                                         description="prueba")
    response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    created_contact = response.json()
    created_contacts.append(created_contact)
