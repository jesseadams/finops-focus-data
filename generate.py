#!/usr/bin/env python
# -*- coding: utf-8 -*-

from faker import Faker
from collections import OrderedDict
from dateutil.relativedelta import relativedelta
import csv
import datetime

fake = Faker()
Faker.seed(1337)

# Define the number of records to generate
num_records = 250000

charge_categories = [
    "Usage",
    "Purchase",
    "Tax",
    "Credit",
    "Adjustment"
]

cloud_providers = {
    "aws": {
        "name": "Amazon Web Services, Inc.",
        "market_share": 0.42,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            "us-east-1",
            "us-east-2",
            "us-west-2"
        ]
    },
    "microsoft": {
        "name": "Microsoft Corporation",
        "market_share": 0.22,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            "eastus",
            "westus",
            "centralus"
        ]
    },
    "google": {
        "name": "Google LLC",
        "market_share": 0.15,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            "us-central1",
            "us-east1",
            "us-west1"
        ]
    },
    "ibm": {
        "name": "IBM Corporation",
        "market_share": 0.12,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            "us-south",
            "us-east",
            "us-west"
        ]
    },
    "oracle": {
        "name": "Oracle Corporation",
        "market_share": 0.09,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            "us-ashburn-1",
            "us-phoenix-1",
            "us-saopaulo-1"
        ]
    }
}

units = [
    "Count",
    "Unit",
    "Request",
    "Token",
    "Connection",
    "Certificate",
    "Domain",
    "Core"
]

pricing_categories = [
    "Standard",
    "Dynamic",
    "Committed",
    "Other"
]

service_categories = [
    "AI and Machine Learning",
    "Analytics",
    "Business Applications",
    "Compute",
    "Databases",
    "Developer Tools",
#    "Multicloud,"
    "Identity",
    "Integration",
#    "Internet of Things",
    "Management and Governance",
#    "Media",
    "Migration",
    "Mobile",
    "Networking",
    "Security",
    "Storage",
    "Web",
    "Other"
]

cloud_providers_ordered_dict = []
for key, provider in cloud_providers.items():
    cloud_providers_ordered_dict.append((key, provider["market_share"]))

team_names = []
for i in range(5):
    team_name = fake.color_name()
    team_names.append(team_name)
    cloud_providers["aws"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    cloud_providers["microsoft"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    cloud_providers["google"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    cloud_providers["ibm"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    cloud_providers["oracle"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)

date_start = datetime.date(2024, 1, 1)
date_end = datetime.date.today()

# Generate the data
data = []
for i in range(num_records):
    cost = fake.pyfloat(right_digits=2, min_value=0.01, max_value=1000.00)
    provider = fake.random_element(elements=OrderedDict(cloud_providers_ordered_dict))
    account = fake.random_element(elements=OrderedDict(cloud_providers[provider]["accounts"]))

    date = fake.date_between_dates(date_start, date_end)
    billing_period_start = datetime.date(date.year, date.month, 1) 
    billing_period_end = billing_period_start + relativedelta(months=1)

    unit = fake.random_element(elements=units)
    quantity = fake.pyfloat(right_digits=4, min_value=0.0001, max_value=5000.0000)

    record = {
        "BilledCost": cost,
        "BillingAccountId": cloud_providers[provider]["billing_account_id"],
        "BillingAccountName": account,
        "BillingCurrency": "USD",
        "BillingPeriodEnd": billing_period_end,
        "BillingPeriodStart": billing_period_start,
        "ChargeCategory": fake.random_element(elements=charge_categories),
        "ChargeClass": "",
        "ChargeDescription": "Fake charge description",
        "ChargeFrequency": fake.random_element(elements=["One-Time", "Recurring", "Usage-Based"]),
        "ChargePeriodEnd": billing_period_end,
        "ChargePeriodStart": billing_period_start,
        "CommitmentDiscountCategory": "",   
        "CommitmentDiscountId": "",
        "CommitmentDiscountName": "",
        "CommitmentDiscountStatus": "",
        "CommitmentDiscountType": "",
        "ConsumedQuantity": quantity,
        "ConsumedUnit": unit,
        "ContractedCost": cost,
        "ContractedUnitPrice": cost,
        "EffectiveCost": cost,
        "InvoiceIssuerName": cloud_providers[provider]["name"],
        "ListCost": cost,
        "ListUnitPrice": cost,
        "PricingCategory": fake.random_element(elements=pricing_categories),
        "PricingQuantity": quantity,
        "PricingUnit": unit,
        "ProviderName": cloud_providers[provider]["name"],
        "PublisherName": cloud_providers[provider]["name"],
        "RegionId": fake.random_element(elements=cloud_providers[provider]["regions"]),
        "RegionName": "",
        "ResourceId": "",
        "ResourceName": "",
        "ResourceType": "",
        "ServiceCategory": fake.random_element(elements=service_categories),
        "ServiceName": fake.name(),
        "SkuId": fake.pystr(min_chars=10, max_chars=10),
        "SkuPriceId": fake.pystr(min_chars=10, max_chars=10) + "." + fake.pystr(min_chars=10, max_chars=10) + "." + fake.pystr(min_chars=10, max_chars=10),
        "SubAccountId": cloud_providers[provider]["accounts"][account],
        "SubAccountName": account,
        "Tags": "{}"
    }
    data.append(record)

# Print the generated data
#import json
#print(json.dumps(data, indent=4))

with open("data.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    #for record in data:
    #    writer.writerow(record)
