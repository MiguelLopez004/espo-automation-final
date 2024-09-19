from src.transport.endpoint import Endpoint
from config.config import BASE_URI


class EndpointAccount:

    @classmethod
    def account(cls):
        return f"{BASE_URI}{Endpoint.BASE_ACCOUNT.value}"

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
             select="billingAddressCountry,type,website,name",
             maxSize=20, offset=0, orderBy="createdAt", order="desc"):
        return cls.build_url_list(Endpoint.BASE_ACCOUNT.value, select, maxSize, offset, orderBy, order)

    @staticmethod
    def build_url_account_view(base, account_id):
        return f"{BASE_URI}{base.format(account_id=account_id)}"

    @classmethod
    def view(cls, account_id):
        return cls.build_url_account_view(Endpoint.BASE_ACCOUNT_VIEW.value, account_id)
