import pytest

from src.resources.authentifications.authentification import Auth
from src.resources.payloads.payloads_contacts import PayloadContact
from src.resources.call_request.contact import ContactCall


@pytest.fixture(scope="module")
def setup_teardown_list_contacts(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)

    payload_contact_1 = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                                   lastName="Towel",
                                                                   name="Mike Towel")
    payload_contact_2 = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mikel",
                                                                   lastName="Merino",
                                                                   name="Mikel Merino")

    contact1 = ContactCall().create(headers, payload_contact_1)
    contact2 = ContactCall().create(headers, payload_contact_2)

    if isinstance(contact1, list):
        contact1 = contact1[0]
    if isinstance(contact2, list):
        contact2 = contact2[0]

    yield headers, contact1, contact2

    ContactCall().delete(headers, contact1['id'])
    ContactCall().delete(headers, contact2['id'])


@pytest.fixture(scope="function")
def setup_add_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    created_contacts = []
    yield headers, created_contacts

    for contact in created_contacts:
        ContactCall().delete(headers, contact['id'])


@pytest.fixture(scope="function")
def setup_contact_delete_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_contact = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                                 lastName="Towel",
                                                                 name="Mike Towel")
    contact = ContactCall().create(headers, payload_contact)
    yield headers, contact


@pytest.fixture(scope="function")
def setup_edit_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_contact = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                                 lastName="Towel",
                                                                 name="Mike Towel")
    contact = ContactCall().create(headers, payload_contact)
    yield headers, contact
    ContactCall().delete(headers, contact['id'])


@pytest.fixture(scope="function")
def setup_create_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_contact = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                                 lastName="Towel",
                                                                 name="Mike Towel")
    contact = ContactCall().create(headers, payload_contact)
    yield headers, contact


@pytest.fixture(scope="function")
def setup_contact_view_contact(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    payload_contact = PayloadContact().build_payload_add_contact(salutationName="Ms.", firstName="Mike",
                                                                 lastName="Towel",
                                                                 name="Mike Towel")
    contact = ContactCall().create(headers, payload_contact)
    yield headers, contact
    ContactCall().delete(headers, contact['id'])