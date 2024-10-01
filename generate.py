#!/usr/bin/env python
# -*- coding: utf-8 -*-

from faker import Faker
from collections import OrderedDict
from dateutil.relativedelta import relativedelta
import csv
import datetime
import uuid

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
            ("us-east-1", 0.69),
            ("us-east-2", 0.21),
            ("us-west-2", 0.10)
        ]
    },
    "microsoft": {
        "name": "Microsoft Corporation",
        "market_share": 0.22,
        "billing_account_id": f'/providers/Microsoft.Billing/billingAccounts/{uuid.uuid4()}:{uuid.uuid4()}_2019-05-31/billingProfiles/BRUX-63NR-BG7-PGB',
        "accounts": {},
        "regions": [
            ("eastus", 0.43),
            ("westus", 0.42),
            ("centralus", 0.15)
        ]
    },
    "google": {
        "name": "Google LLC",
        "market_share": 0.15,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            ("us-central1", 0.78),
            ("us-east1", 0.13),
            ("us-west1", 0.09)
        ]
    },
    "ibm": {
        "name": "IBM Corporation",
        "market_share": 0.12,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            ("us-south", 0.55),
            ("us-east", 0.22),
            ("us-west", 0.23)
        ]
    },
    "oracle": {
        "name": "Oracle Corporation",
        "market_share": 0.09,
        "billing_account_id": fake.random_int(min=100000000000, max=999999999999),
        "accounts": {},
        "regions": [
            ("us-ashburn-1", 0.25),
            ("us-phoenix-1", 0.30),
            ("us-saopaulo-1", 0.40)
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
#    "AI and Machine Learning",
#    "Analytics",
#    "Business Applications",
    ("Compute", 0.43),
    ("Databases", 0.18),
#    "Developer Tools",
#    "Multicloud,"
    ("Identity", 0.01),
#    "Integration",
#    "Internet of Things",
    ("Management and Governance", 0.05),
#    "Media",
#    "Migration",
#    "Mobile",
    ("Security", 0.07),
    ("Storage", 0.11),
#    "Web",
    ("Other", 0.15)
]

service_categories = {
    "compute": {
        "name": "Compute",
        "market_share": 0.43,
        "services": {
            "aws": [
                "Amazon Elastic Compute Cloud"
            ],
            "microsoft": [
                "Azure Virtual Machines"
            ],
            "google": [
                "Compute Engine"
            ],
            "ibm": [
                "Virtual Servers"
            ],
            "oracle": [
                "Compute"
            ]
        }
    },
    "databases": {
        "name": "Databases",
        "market_share": 0.18,
        "services": {
            "aws": [
                "Amazon Relational Database Service"
            ],
            "microsoft": [
                "Azure SQL Database"
            ],
            "google": [
                "Cloud SQL"
            ],
            "ibm": [
                "Databases for MongoDB"
            ],
            "oracle": [
                "Autonomous Database"
            ]
        }
    },
    "identity": {
        "name": "Identity",
        "market_share": 0.01,
        "services": {
            "aws": [
                "Amazon Cognito"
            ],
            "microsoft": [
                "Azure Active Directory"
            ],
            "google": [
                "Identity Platform"
            ],
            "ibm": [
                "App ID"
            ],
            "oracle": [
                "Identity Cloud Service"
            ]
        }
    },
    "management_and_governance": {
        "name": "Management and Governance",
        "market_share": 0.05,
        "services": {
            "aws": [
                "Amazon CloudWatch"
            ],
            "microsoft": [
                "Azure Monitor"
            ],
            "google": [
                "Cloud Monitoring"
            ],
            "ibm": [
                "Cloud Pak for Multicloud Management"
            ],
            "oracle": [
                "Management Cloud"
            ]
        }
    },
    "security": {
        "name": "Security",
        "market_share": 0.07,
        "services": {
            "aws": [
                "Amazon GuardDuty"
            ],
            "microsoft": [
                "Azure Security Center"
            ],
            "google": [
                "Cloud Armor"
            ],
            "ibm": [
                "Cloud Pak for Security"
            ],
            "oracle": [
                "Cloud Guard"
            ]
        }
    },
    "storage": {
        "name": "Storage",
        "market_share": 0.11,
        "services": {
            "aws": [
                "Amazon Simple Storage Service"
            ],
            "microsoft": [
                "Azure Blob Storage"
            ],
            "google": [
                "Cloud Storage"
            ],
            "ibm": [
                "Cloud Object Storage"
            ],
            "oracle": [
                "Object Storage"
            ]
        }
    },
    "other": {
        "name": "Other",
        "market_share": 0.15,
        "services": {
            "aws": [
                "Amazon Simple Email Service"
            ],
            "microsoft": [
                "Azure DevOps"
            ],
            "google": [
                "Cloud Functions"
            ],
            "ibm": [
                "Watson Assistant"
            ],
            "oracle": [
                "API Gateway"
            ]
        }
    }
}

cloud_providers_ordered_dict = []
for key, provider in cloud_providers.items():
    cloud_providers_ordered_dict.append((key, provider["market_share"]))

service_categories_ordered_dict = []
for key, category in service_categories.items():
    service_categories_ordered_dict.append((key, category["market_share"]))

for i in range(5):
    team_name = fake.bs().replace(" ", "-").lower()
    cloud_providers["aws"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    
    team_name = fake.bs().replace(" ", "-").lower()
    # TODO: f'/subscriptions/{uuid.uuid4()}'
    cloud_providers["microsoft"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    
    team_name = fake.bs().replace(" ", "-").lower()
    cloud_providers["google"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    
    team_name = fake.bs().replace(" ", "-").lower()
    cloud_providers["ibm"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)
    
    team_name = fake.bs().replace(" ", "-").lower()
    cloud_providers["oracle"]["accounts"][team_name] = fake.random_int(min=100000000000, max=999999999999)

projects = [
    (fake.color_name(), 0.52),
    (fake.color_name(), 0.32),
    (fake.color_name(), 0.16),
]

date_start = datetime.date(2024, 1, 1)
date_end = datetime.date.today()

# Generate the data
data = []
for i in range(num_records):
    cost = fake.pyfloat(right_digits=2, min_value=0.01, max_value=1000.00)
    provider = fake.random_element(elements=OrderedDict(cloud_providers_ordered_dict))
    account = fake.random_element(elements=OrderedDict(cloud_providers[provider]["accounts"]))
    unit = fake.random_element(elements=units)
    quantity = fake.pyfloat(right_digits=4, min_value=0.0001, max_value=5000.0000)
    service_category = fake.random_element(elements=OrderedDict(service_categories_ordered_dict))

    if i < 10000:
        # Simulate a spike in usage
        date = datetime.date(2024, 3, 1)
    else:
        date = fake.date_between_dates(date_start, date_end)

    billing_period_start = datetime.date(date.year, date.month, 1) 
    billing_period_end = billing_period_start + relativedelta(months=1)

    record = {
        "BilledCost": cost,
        "BillingAccountId": cloud_providers[provider]["billing_account_id"],
        "BillingAccountName": "Main Billing Account", 
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
        "RegionId": fake.random_element(elements=OrderedDict(cloud_providers[provider]["regions"])),
        "RegionName": "",
        "ResourceId": "",
        "ResourceName": "",
        "ResourceType": "",
        "ServiceCategory": service_categories[service_category]["name"],
        # TODO: Add more services and make this random, weighted
        "ServiceName": service_categories[service_category]["services"][provider][0],
        "SkuId": fake.pystr(min_chars=10, max_chars=10),
        "SkuPriceId": fake.pystr(min_chars=10, max_chars=10) + "." + fake.pystr(min_chars=10, max_chars=10) + "." + fake.pystr(min_chars=10, max_chars=10),
        "SubAccountId": cloud_providers[provider]["accounts"][account],
        "SubAccountName": account,
        "Tags": {
            "user_billing_owner": "Finance",
            "user_billing_project": fake.random_element(elements=OrderedDict(projects)),
        }
    }
    data.append(record)

# Write the data as a CSV
with open("data.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
