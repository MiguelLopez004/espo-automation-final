import json


class PayloadContact:

    @staticmethod
    def build_payload_add_contact(contact_data):
        payload = {
            "salutationName": contact_data.get("salutationName"),
            "firstName": contact_data.get("firstName"),
            "lastName": contact_data.get("lastName"),
            "name": contact_data.get("name"),
            "accountsIds": contact_data.get("accountsIds", []),
            "accountsNames": contact_data.get("accountsNames", {}),
            "accountsColumns": contact_data.get("accountsColumns", {}),
            "title": contact_data.get("title"),
            "accountIsInactive": contact_data.get("accountIsInactive"),
            "emailAddressData": contact_data.get("emailAddressData", []),
            "emailAddress": contact_data.get("emailAddress"),
            "emailAddressIsOptedOut": contact_data.get("emailAddressIsOptedOut"),
            "emailAddressIsInvalid": contact_data.get("emailAddressIsInvalid"),
            "phoneNumberData": contact_data.get("phoneNumberData", []),
            "phoneNumber": contact_data.get("phoneNumber"),
            "phoneNumberIsOptedOut": contact_data.get("phoneNumberIsOptedOut"),
            "phoneNumberIsInvalid": contact_data.get("phoneNumberIsInvalid"),
            "addressPostalCode": contact_data.get("addressPostalCode"),
            "addressStreet": contact_data.get("addressStreet"),
            "addressState": contact_data.get("addressState"),
            "addressCity": contact_data.get("addressCity"),
            "addressCountry": contact_data.get("addressCountry"),
            "description": contact_data.get("description"),
            "assignedUserName": contact_data.get("assignedUserName"),
            "assignedUserId": contact_data.get("assignedUserId"),
            "teamsIds": contact_data.get("teamsIds", []),
            "teamsNames": contact_data.get("teamsNames", {})
        }

        return json.dumps(payload, indent=4)
