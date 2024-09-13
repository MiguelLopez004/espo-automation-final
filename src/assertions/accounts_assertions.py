import pytest
from src.assertions.schema_assertions import AssertionSchemas


class AssertionAccounts:
    @staticmethod
    def assert_check_orden(response_json, order):
        list = [contact['name'] for contact in response_json['list']]
        if order == "asc":
            assert list == sorted(list), "The equipment list is not in asc order"
        elif order == "desc":
            assert list == sorted(list, reverse=True), "The equipment list is not in order"
        else:
            pytest.fail(f"Orden '{order}' invalido")

    @staticmethod
    def assert_response_empty(response_text):
        assert response_text == ''

    @staticmethod
    def assert_empty_field_list(response_json):
        field = "list"
        list_field = response_json.get(field)
        assert list_field is not None, f"'{field}' not found in the response."
        assert isinstance(list_field, list), f"The field '{field}' is not a list."
        assert len(list_field) == 0, f"The list '{field}' is not empty."

    @staticmethod
    def assert_check_order_asc(response_json):
        lists = [contact['name'] for contact in response_json['list']]
        assert lists == sorted(lists), "The contact list is not in ascending order"

    @staticmethod
    def assert_check_order_desc(response_json):
        lists = [contact['name'] for contact in response_json['list']]
        assert lists == sorted(lists, reverse=True), "The contact list is not in descending order"

    @staticmethod
    def assert_response_true(response):
        assert response.text == "true"

    @staticmethod
    def assert_response_false(response):
        assert response.text == "false"

    @staticmethod
    def assert_account_list_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "account_list_schema.json")

    @staticmethod
    def assert_account_list_without_select_schema_file(response):
        return AssertionSchemas().validate_json_schema(response, "account_list_without_select_schema.json")

    @staticmethod
    def assert_add_account_schema_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "add_account_schema.json")

    @staticmethod
    def assert_edit_account_schema_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "edit_account_schema.json")

    @staticmethod
    def assert_account_view_schema_file(payload):
        return AssertionSchemas().validate_json_schema(payload, "view_account_schema.json")