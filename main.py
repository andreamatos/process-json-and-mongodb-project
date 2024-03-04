# main.py

import json
from pymongo import MongoClient

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def is_in_debt(self):
        return self.balance < 0

    def to_dict(self):
        return {'account_number': self.account_number, 'balance': self.balance}

    def __str__(self):
        return f"Account {self.account_number}: Balance = ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def accounts_in_debt(self):
        return [account for account in self.accounts if account.is_in_debt()]

class MongoDBHandler:
    def __init__(self, uri, database_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert_accounts(self, accounts):
        for account in accounts:
            self.collection.insert_one(account.to_dict())

def read_accounts_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return [Account(account['account_number'], account['balance']) for account in data]

def write_accounts_to_json(json_file, accounts):
    with open(json_file, 'w') as f:
        json.dump([account.to_dict() for account in accounts], f, indent=2)

# Example usage:
input_json_file = 'input_accounts.json'  # Replace with your input JSON file
output_json_file = 'output_debt_accounts.json'  # Replace with your desired output JSON file
mongodb_uri = "mongodb://localhost:27017/"  # Use the appropriate connection URI
database_name = "mydatabase"  # Replace with your desired database name
collection_name = "mycollection"  # Replace with your desired collection name

# Read accounts from JSON
accounts_data = read_accounts_from_json(input_json_file)

# Create Account objects and add them to the Bank
bank = Bank()
for account in accounts_data:
    bank.add_account(account)

# Find accounts in debt
debt_accounts = bank.accounts_in_debt()

# Insert accounts in debt into MongoDB
mongo_handler = MongoDBHandler(mongodb_uri, database_name, collection_name)
mongo_handler.insert_accounts(debt_accounts)

# Write accounts in debt to JSON
write_accounts_to_json(output_json_file, debt_accounts)

if debt_accounts:
    print("Accounts in debt:")
    for account in debt_accounts:
        print(account)
else:
    print("No accounts in debt.")
