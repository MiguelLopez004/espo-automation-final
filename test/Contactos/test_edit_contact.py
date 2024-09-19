import pytest

from src.assertions.contacts_assertions import AssertionContacts
from src.transport.endpoint_contact import EndpointContacts
from src.resources.payloads.payloads_contacts import PayloadContact
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.resources.authentifications.authentification import Auth


@pytest.mark.regression
@pytest.mark.functional
def test_edit_contact_all_data(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_edit_contact_address_data(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",)
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_edit_contact_field_unknow(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", test="test",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",)
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_edit_contact_empty_data(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",)
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_edit_contact_email_invalid(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_edit_contact_phoneNumber_invalid(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945sdfsd654564",
                                                         addressPostalCode="0000", addressStreet="none",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_edit_contact_address_invalid(setup_edit_contact):
    headers, contact = setup_edit_contact
    payload = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                         lastName="Towel",
                                                         name="Mike Towel", emailAddress="one@on.as",
                                                         phoneNumber="+17945654564",
                                                         addressPostalCode="0000", addressStreet="452345234$&/$%$%&/$%&($%&/··",
                                                         addressState="none", addressCity="none", addressCountry="none",
                                                         description="prueba")
    response = EspocrmRequest().put(EndpointContacts.view(contact['id']), headers, payload)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts().assert_edit_contact_schema_schema_file(response.json())
