import pytest
import base64
from config.config import X_Api_Key


@pytest.fixture(scope="session")
def get_headers():
    def _get_headers(username, password, additional_params=None):
        espo_authorization = encoded(username, password)
        headers = {
            'Espo-Authorization': espo_authorization,
            'X-Api-Key': X_Api_Key
        }
        if additional_params:
            headers.update(additional_params)
        return headers

    return _get_headers


def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode