import json


class PayloadAccount:

    @staticmethod
    def build_payload_add_account(
            contactIsInactive=False, name=None, website=None, emailAddressData=None,
            emailAddress=None, emailAddressIsOptedOut=None, emailAddressIsInvalid=None,
            phoneNumberData=None, phoneNumber=None, phoneNumberIsOptedOut=None,
            phoneNumberIsInvalid=None, billingAddressPostalCode=None, billingAddressStreet=None,
            billingAddressState=None, billingAddressCity=None, billingAddressCountry=None,
            shippingAddressPostalCode=None, shippingAddressStreet=None,
            shippingAddressState=None, shippingAddressCity=None, shippingAddressCountry=None,
            type=None, industry=None, description=None, assignedUserName=None,
            assignedUserId=None, teamsIds=None, teamsNames=None):
        payload = {
            "contactIsInactive": contactIsInactive,
            "name": name,
            "website": website,
            "emailAddressData": emailAddressData if emailAddressData is not None else [],
            "emailAddress": emailAddress,
            "emailAddressIsOptedOut": emailAddressIsOptedOut,
            "emailAddressIsInvalid": emailAddressIsInvalid,
            "phoneNumberData": phoneNumberData if phoneNumberData is not None else [],
            "phoneNumber": phoneNumber,
            "phoneNumberIsOptedOut": phoneNumberIsOptedOut,
            "phoneNumberIsInvalid": phoneNumberIsInvalid,
            "billingAddressPostalCode": billingAddressPostalCode,
            "billingAddressStreet": billingAddressStreet,
            "billingAddressState": billingAddressState,
            "billingAddressCity": billingAddressCity,
            "billingAddressCountry": billingAddressCountry,
            "shippingAddressPostalCode": shippingAddressPostalCode,
            "shippingAddressStreet": shippingAddressStreet,
            "shippingAddressState": shippingAddressState,
            "shippingAddressCity": shippingAddressCity,
            "shippingAddressCountry": shippingAddressCountry,
            "type": type,
            "industry": industry,
            "description": description,
            "assignedUserName": assignedUserName,
            "assignedUserId": assignedUserId,
            "teamsIds": teamsIds if teamsIds is not None else [],
            "teamsNames": teamsNames if teamsNames is not None else {}
        }
        return json.dumps(payload)
