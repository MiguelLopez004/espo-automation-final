from src.transport.endpoint_contact import EndpointContacts
from src.transport.api_request import EspocrmRequest


class ContactCall:
    @classmethod
    def view(cls, headers, contact_id):
        response = EspocrmRequest().get(EndpointContacts.view(contact_id), headers)
        return response.json()

    @classmethod
    def create(cls, headers, payload):
        response = EspocrmRequest().post(EndpointContacts.contact(), headers, payload)
        return response.json()

    @classmethod
    def update(cls, headers, payload, contact_id):
        response = EspocrmRequest().put(EndpointContacts.view(contact_id), headers, payload)
        return response.json()

    @classmethod
    def delete(cls, headers, contact_id):
        response = EspocrmRequest().delete(EndpointContacts.view(contact_id), headers)
        return response.json()