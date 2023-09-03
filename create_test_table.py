"""
SCHEMA

item = {
    "clubId": {"S": document.get("clubId", "None")},
    "fullName": {"S": document.get("fullName", "None")},
    "nicknames": {"L": [{"S": nickname} for nickname in document.get("nickname", [])]},
    "age": {"N": document.get("age", "0")},
    "contacts": {
        "M": {
            "phoneNumber": {"S": document.get("phoneNumber", "None")},
            "email": {"S": document.get("personalEmail", "None")},
        }
    },
}
"""
import names
import random
import json

items = []

for i in range(1, 26):
    fullName = names.get_full_name()
    item = {
        "clubId": {"S": f"AWS-CC-2023-{i:04}"},
        "fullName": {"S": fullName},
        "nicknames": {"L": [{"S": name} for name in fullName.split(" ")]},
        "age": {"N": str(random.randint(18, 23))},
        "contacts": {
            "M": {
                "phoneNumber": {"S": f"09{random.randint(1, 999999999):04}"},
                "email": {"S": f"{fullName.replace(' ', '')}@gmail.com"},
            }
        },
    }
    items.append(item)

items = json.dumps(items, indent=2)

with open("data.json", "w") as file:
    file.write(items)
