import pytest
from src.resources.authentifications.authentification import Auth
from src.transport.api_request import EspocrmRequest
from src.transport.endpoint_contact import EndpointContacts
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.schema_assertions import AssertionSchemas
from src.assertions.contacts_assertions import AssertionContacts


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_list_contacts_with_data(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_contact_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_order_asc(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(order='asc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_order_invalid(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(order='ASCSA'), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_order_desc(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(order='desc'), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_without_select(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(select=None), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionContacts.assert_contact_list_without_select_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_select_unknown(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(select="unknown"), headers)
    AssertionSchemas().assert_field_list_no_empty(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_select_special(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(select="***"), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionSchemas().assert_field_list_no_empty(response.json())


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_invalid_authentication(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointContacts.list(), headers)
    AssertionStatusCode().assert_status_code_401(response)
    AssertionContacts().assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_maxsize_major_total(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(maxSize=200), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionContacts().assert_contact_list_schema_file(response.json())
    AssertionSchemas().assert_field_list_no_empty(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_maxsize_cero(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(maxSize=0), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionContacts().assert_contact_list_schema_file(response.json())
    AssertionContacts().assert_empty_field_list(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_contacts_maxsize_negative(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(maxSize=-1), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts.assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_contacts_maxsize_string(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(maxSize="as"), headers)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_offset_major_total(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(offset=200), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionContacts().assert_contact_list_schema_file(response.json())
    AssertionContacts().assert_empty_field_list(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_offset_cero(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(offset=0), headers)
    AssertionStatusCode.assert_status_code_200(response)
    AssertionContacts().assert_contact_list_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_contacts_offset_negative(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(offset=-1), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts.assert_response_empty(response.text)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_list_contacts_offset_string(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(offset="as"), headers)
    AssertionStatusCode().assert_status_code_400(response)


@pytest.mark.regression
@pytest.mark.functional
def test_list_contacts_ordeby_unknown(setup_teardown_list_contacts):
    headers, contact1, contact2 = setup_teardown_list_contacts
    response = EspocrmRequest().get(EndpointContacts.list(orderBy='unknown'), headers)
    AssertionStatusCode().assert_status_code_400(response)
    AssertionContacts.assert_response_empty(response.text)