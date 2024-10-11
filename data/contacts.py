from faker import Faker
import json
import random

fake = Faker()


def generate_contact_data():
    contact_data = {
        "accountId": "6705abbacb28e05d9",
        "accountIsInactive": fake.boolean(),
        "accountName": fake.company(),
        "accountsColumns": {
            "6705abbacb28e05d9": {
                "role": None,
                "isInactive": fake.boolean()
            }
        },
        "accountsIds": "6705abbacb28e05d9",
        "accountsNames": {
            "6705abbacb28e05d9": fake.company()
        },
        "addressCity": fake.city(),
        "addressCountry": fake.country(),
        "addressPostalCode": fake.postcode(),
        "addressState": fake.state(),
        "addressStreet": fake.street_address(),
        "assignedUserId": "6703f4f2dfe619515",
        "assignedUserName": "Admin",
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
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
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
        "salutationName": random.choice(
            ["Mr.", "Mrs.", "Ms.", "Dr."]),
        "teamsIds": ["6703f6f3376e6dd38"],
        "teamsNames": {"6703f6f3376e6dd38": "Team QA"},
    }

    contact_data["phoneNumber"] = "+1" + fake.msisdn()[0:10]
    contact_data["phoneNumberData"][0]["phoneNumber"] = "+1" + fake.msisdn()[0:10]

    return json.dumps(contact_data, indent=4)


def create_contact_data(addressCity=None, addressCountry=None, addressPostalCode=None,
                        addressState=None, addressStreet=None,
                        description=None, emailAddress=None, firstName=None, lastName=None, phoneNumber=None,
                        salutationName=None):
    contact_data = {
        "addressCity": addressCity,
        "addressCountry": addressCountry,
        "addressPostalCode": addressPostalCode,
        "addressState": addressState,
        "addressStreet": addressStreet,
        "description": description,
        "emailAddress": emailAddress,
        "firstName": firstName or fake.first_name(),
        "lastName": lastName or fake.last_name(),
        "salutationName": salutationName or random.choice(["Mr.", "Mrs.", "Ms.", "Dr."]),
        "phoneNumber": phoneNumber,
    }

    contact_data = {key: value for key, value in contact_data.items() if value is not None}
    contact_data = {key: (None if value == "null" else value) for key, value in contact_data.items()}

    return json.dumps(contact_data, indent=4)