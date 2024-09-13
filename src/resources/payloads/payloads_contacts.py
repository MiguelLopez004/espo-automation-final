import json


class PayloadContact:

    @staticmethod
    def build_payload_add_contact(salutationName, firstName, lastName, name,
                                  accountsIds=None, accountsNames=None, accountsColumns=None,
                                  title=None, accountIsInactive=None, emailAddressData=None, emailAddress=None,
                                  emailAddressIsOptedOut=None, emailAddressIsInvalid=None, phoneNumberData=None,
                                  phoneNumber=None, phoneNumberIsOptedOut=None, phoneNumberIsInvalid=None,
                                  addressPostalCode=None, addressStreet=None, addressState=None,
                                  addressCity=None, addressCountry=None, description=None,
                                  assignedUserName=None, assignedUserId=None, teamsIds=None, teamsNames=None):
        payload = {
            "salutationName": salutationName,
            "firstName": firstName,
            "lastName": lastName,
            "name": name,
            "accountsIds": accountsIds if accountsIds is not None else [],
            "accountsNames": accountsNames if accountsNames is not None else {},
            "accountsColumns": accountsColumns if accountsColumns is not None else {},
            "title": title,
            "accountIsInactive": accountIsInactive,
            "emailAddressData": emailAddressData if emailAddressData is not None else [],
            "emailAddress": emailAddress,
            "emailAddressIsOptedOut": emailAddressIsOptedOut,
            "emailAddressIsInvalid": emailAddressIsInvalid,
            "phoneNumberData": phoneNumberData if phoneNumberData is not None else [],
            "phoneNumber": phoneNumber,
            "phoneNumberIsOptedOut": phoneNumberIsOptedOut,
            "phoneNumberIsInvalid": phoneNumberIsInvalid,
            "addressPostalCode": addressPostalCode,
            "addressStreet": addressStreet,
            "addressState": addressState,
            "addressCity": addressCity,
            "addressCountry": addressCountry,
            "description": description,
            "assignedUserName": assignedUserName,
            "assignedUserId": assignedUserId,
            "teamsIds": teamsIds if teamsIds is not None else [],
            "teamsNames": teamsNames if teamsNames is not None else {}
        }
        return json.dumps(payload)
