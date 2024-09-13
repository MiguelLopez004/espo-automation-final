import requests


class EspocrmRequest:
    @staticmethod
    def get(url, headers):
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(url, headers, payloads=None):
        headers = headers.copy()
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url, headers=headers, data=payloads)
        return response

    @staticmethod
    def put(url, headers, payloads=None):
        headers = headers.copy()
        headers.update({'Content-Type': 'application/json'})
        response = requests.put(url, headers=headers, data=payloads)
        return response

    @staticmethod
    def delete(url, headers, payloads=None):
        headers = headers.copy()
        headers.update({'Content-Type': 'application/json'})
        response = requests.delete(url, headers=headers, data=payloads)
        return response


