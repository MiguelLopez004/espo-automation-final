import pytest
from src.resources.authentifications.authentification import Auth
from src.transport.endpoint_contact import EndpointContacts
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.contacts_assertions import AssertionContacts


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_view_contact_additional_headers(setup_contact_view_contact, get_headers):
    headers, contact = setup_contact_view_contact
    additional_headers = {'header_extra': 'value_extra'}
    headerse = Auth().get_valid_user_headers(get_headers, additional_headers)
    response = EspocrmRequest().get(EndpointContacts.view(contact['id']), headerse)
    AssertionStatusCode().assert_status_code_200(response)

@pytest.mark.regression
@pytest.mark.functional
def test_view_contact_incorrect_http_method(setup_contact_view_contact):
    headers, contact = setup_contact_view_contact
    response = EspocrmRequest().post(EndpointContacts.view(contact['id']), headers)
    AssertionStatusCode().assert_status_code_405(response)


@pytest.mark.regression
@pytest.mark.functional
@pytest.mark.smoke
def test_view_contact_correct(setup_contact_view_contact):
    headers, contact = setup_contact_view_contact
    response = EspocrmRequest().get(EndpointContacts.view(contact['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_contact_view_schema_file(response.json())


@pytest.mark.regression
@pytest.mark.functional
def test_view_contact_incorrect_authorization(setup_contact_view_contact,get_headers):
    headers, contact = setup_contact_view_contact
    headersInvalid = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointContacts.view(contact['id']), headersInvalid)
    AssertionStatusCode().assert_status_code_401(response)

@pytest.mark.regression
@pytest.mark.functional
def test_view_contact_id_not_exists(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(EndpointContacts.view(contact_id="id_no_existente"), headers)
    AssertionStatusCode().assert_status_code_404(response)