import json

class PayloadAccount:

    @staticmethod
    def build_payload_add_account(account_data):
        payload = {
            "contactIsInactive": account_data.get("contactIsInactive", False),
            "name": account_data.get("name"),
            "website": account_data.get("website"),
            "emailAddressData": account_data.get("emailAddressData", []),
            "emailAddress": account_data.get("emailAddress"),
            "emailAddressIsOptedOut": account_data.get("emailAddressIsOptedOut"),
            "emailAddressIsInvalid": account_data.get("emailAddressIsInvalid"),
            "phoneNumberData": account_data.get("phoneNumberData", []),
            "phoneNumber": account_data.get("phoneNumber"),
            "phoneNumberIsOptedOut": account_data.get("phoneNumberIsOptedOut"),
            "phoneNumberIsInvalid": account_data.get("phoneNumberIsInvalid"),
            "billingAddressPostalCode": account_data.get("billingAddressPostalCode"),
            "billingAddressStreet": account_data.get("billingAddressStreet"),
            "billingAddressState": account_data.get("billingAddressState"),
            "billingAddressCity": account_data.get("billingAddressCity"),
            "billingAddressCountry": account_data.get("billingAddressCountry"),
            "shippingAddressPostalCode": account_data.get("shippingAddressPostalCode"),
            "shippingAddressStreet": account_data.get("shippingAddressStreet"),
            "shippingAddressState": account_data.get("shippingAddressState"),
            "shippingAddressCity": account_data.get("shippingAddressCity"),
            "shippingAddressCountry": account_data.get("shippingAddressCountry"),
            "type": account_data.get("type"),
            "industry": account_data.get("industry"),
            "description": account_data.get("description"),
            "assignedUserName": account_data.get("assignedUserName"),
            "assignedUserId": account_data.get("assignedUserId"),
            "teamsIds": account_data.get("teamsIds", []),
            "teamsNames": account_data.get("teamsNames", {})
        }

        return json.dumps(payload, indent=4)
