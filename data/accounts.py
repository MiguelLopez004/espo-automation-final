from faker import Faker
import random
import json

fake = Faker()


def generate_account_data():
    account_data = {
        "assignedUserId": "6703f4f2dfe619515",
        "assignedUserName": "Admin",
        "billingAddressCity": fake.city(),
        "billingAddressCountry": fake.country(),
        "billingAddressPostalCode": fake.postcode(),
        "billingAddressState": fake.state(),
        "billingAddressStreet": fake.street_address(),
        "contactIsInactive": fake.boolean(),
        "description": fake.text(max_nb_chars=200),
        "emailAddress": fake.email(),
        "emailAddressData": [{
            "emailAddress": fake.email(),
            "primary": True,
            "type": random.choice(["Work", "Personal"]),
            "optOut": fake.boolean(),
            "invalid": fake.boolean()
        }],
        "emailAddressIsInvalid": fake.boolean(),
        "emailAddressIsOptedOut": fake.boolean(),
        "industry": random.choice(
            ["Agriculture", "Culture", "Defense", "Education", "Energy"]
        ),
        "name": fake.company(),
        "phoneNumber": fake.phone_number(),
        "phoneNumberData": [{
            "phoneNumber": fake.phone_number(),
            "primary": True,
            "type": random.choice(["Office", "Mobile", "Fax", "Other"]),
            "optOut": fake.boolean(),
            "invalid": fake.boolean()
        }],
        "phoneNumberIsInvalid": fake.boolean(),
        "phoneNumberIsOptedOut": fake.boolean(),
        "shippingAddressCity": fake.city(),
        "shippingAddressCountry": fake.country(),
        "shippingAddressPostalCode": fake.postcode(),
        "shippingAddressState": fake.state(),
        "shippingAddressStreet": fake.street_address(),
        "teamsIds": ["6703f6f3376e6dd38"],
        "teamsNames": {"6703f6f3376e6dd38": "Team QA"},
        "type": random.choice(["Investor", "Customer"]),
        "website": fake.domain_name()
    }

    account_data["phoneNumber"] = "+1" + fake.msisdn()[0:10]
    account_data["phoneNumberData"][0]["phoneNumber"] = "+1" + fake.msisdn()[0:10]

    return json.dumps(account_data)


def create_account_data(assignedUserId=None, assignedUserName=None, billingAddressCity=None,
                        billingAddressCountry=None, billingAddressPostalCode=None, billingAddressState=None,
                        billingAddressStreet=None, contactIsInactive=None, description=None, emailAddress=None,
                        industry=None, name=None, phoneNumber=None, teamsIds=None, teamsNames=None,
                        shippingAddressCity=None, shippingAddressCountry=None, shippingAddressPostalCode=None,
                        shippingAddressState=None, shippingAddressStreet=None, type=None, website=None):
    account_data = {
        "assignedUserId": assignedUserId,
        "assignedUserName": assignedUserName,
        "billingAddressCity": billingAddressCity,
        "billingAddressCountry": billingAddressCountry,
        "billingAddressPostalCode": billingAddressPostalCode,
        "billingAddressState": billingAddressState,
        "billingAddressStreet": billingAddressStreet,
        "contactIsInactive": contactIsInactive,
        "description": description,
        "emailAddress": emailAddress,
        "industry": industry,
        "name": name or fake.company(),
        "phoneNumber": phoneNumber,
        "teamsIds": teamsIds,
        "teamsNames": teamsNames,
        "shippingAddressCity": shippingAddressCity,
        "shippingAddressCountry": shippingAddressCountry,
        "shippingAddressPostalCode": shippingAddressPostalCode,
        "shippingAddressState": shippingAddressState,
        "shippingAddressStreet": shippingAddressStreet,
        "type": type,
        "website": website
    }

    account_data = {key: value for key, value in account_data.items() if value is not None}
    account_data = {key: (None if value == "null" else value) for key, value in account_data.items()}

    return json.dumps(account_data, indent=4)
