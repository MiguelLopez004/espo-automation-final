import pytest
import random
import string
from src.resources.authentifications.authentification import Auth
from src.transport.endpoint_contact import EndpointContacts
from src.transport.api_request import EspocrmRequest
from src.assertions.status_code_assertions import AssertionStatusCode
from src.assertions.contacts_assertions import AssertionContacts
from src.resources.call_request.contact import ContactCall


@pytest.mark.smoke
@pytest.mark.functional
def test_delete_contact_valid_contact(setup_create_contact):
    headers, contact = setup_create_contact
    response = EspocrmRequest().delete(EndpointContacts.view(contact['id']), headers)
    AssertionStatusCode().assert_status_code_200(response)
    AssertionContacts().assert_response_true(response)


@pytest.mark.functional
def test_delete_contact_invalid_user(setup_create_contact, get_headers):
    headers, contact = setup_create_contact
    headersAux = headers
    headers = Auth().get_unauthorized_users_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointContacts.view(contact['id']), headers)
    AssertionStatusCode().assert_status_code_401(response)
    ContactCall().delete(headersAux, contact['id'])


@pytest.mark.functional
def test_delete_contact_nonexistent_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    user_id_invalid = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    response = EspocrmRequest().delete(EndpointContacts.view(user_id_invalid), headers)
    AssertionStatusCode().assert_status_code_404(response)


@pytest.mark.smoke
@pytest.mark.functional
def test_delete_contact_valid_with_auth_incorrect(setup_create_contact, get_headers):
    headers, contact = setup_create_contact
    headersAux = headers
    headers = Auth().get_unauthorized_users_user_headers(get_headers)
    response = EspocrmRequest().delete(EndpointContacts.view(contact['id']), headers)
    AssertionStatusCode().assert_status_code_401(response)
    ContactCall().delete(headersAux, contact['id'])