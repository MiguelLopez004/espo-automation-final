from src.transport.endpoint import Endpoint
from config.config import BASE_URI


class EndpointContacts:

    @classmethod
    def contact(cls):
        return f"{BASE_URI}{Endpoint.BASE_CONTACT.value}"

    @staticmethod
    def build_url_list(base, select=None, maxSize=None, offset=None, orderBy=None, order=None):
        params = []
        if select is not None:
            params.append(f"select={select}")
        if maxSize is not None:
            params.append(f"maxSize={maxSize}")
        if offset is not None:
            params.append(f"offset={offset}")
        if orderBy is not None:
            params.append(f"orderBy={orderBy}")
        if order is not None:
            params.append(f"order={order}")
        return f"{BASE_URI}{base}?{'&'.join(params)}"

    @classmethod
    def list(cls,
             select="phoneNumberIsOptedOut,phoneNumberIsInvalid,phoneNumber,phoneNumberData,emailAddressIsOptedOut,"
                    "emailAddressIsInvalid,emailAddress,emailAddressData,accountId,accountName,salutationName,"
                    "firstName,lastName,middleName,name",
             maxSize=20, offset=0, orderBy="createdAt", order="desc"):
        return cls.build_url_list(Endpoint.BASE_CONTACT.value, select, maxSize, offset, orderBy, order)

    @staticmethod
    def build_url_contact_view(base, contact_id):
        return f"{BASE_URI}{base.format(contact_id=contact_id)}"

    @classmethod
    def view(cls, contact_id):
        return cls.build_url_contact_view(Endpoint.BASE_CONTACT_VIEW.value, contact_id)
