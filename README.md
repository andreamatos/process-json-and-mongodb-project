1. Introduction
   This Python script (`main.py`) is a simple program that reads data from a JSON file, processes it, and interacts with a MongoDB database. The program defines classes for representing bank accounts, a bank, and a MongoDB handler. It reads account data from a JSON file, identifies accounts in debt, inserts them into a MongoDB collection, and writes the result to a new JSON file.

2. Prerequisites

   2.1. Python Libraries
      - Ensure that the required Python libraries are installed. Install them using the following command:
        ```
        pip install pymongo
        ```

   2.2. MongoDB Docker Container
      - Ensure that Docker is installed on your system.

      - Run the following command to create a MongoDB Docker container:
        ```
        docker run -d -p 27017:27017 --name mymongo mongo
        ```

      - Replace `mymongo` with your desired container name.

      - This will start a MongoDB container with the default settings on port 27017.

3. Program Components

   3.1. Classes

      - **Account Class:**
        Represents an individual bank account.
        - `__init__(self, account_number, balance)`: Initializes an Account object.
        - `is_in_debt(self)`: Checks if the account is in debt.
        - `to_dict(self)`: Converts the account to a dictionary.
        - `__str__(self)`: Provides a human-readable string representation.

      - **Bank Class:**
        Represents a collection of bank accounts.
        - `__init__(self)`: Initializes a Bank object.
        - `add_account(self, account)`: Adds an Account object to the bank.
        - `accounts_in_debt(self)`: Returns a list of accounts in debt.

      - **MongoDBHandler Class:**
        Handles MongoDB interactions.
        - `__init__(self, uri, database_name, collection_name)`: Initializes the MongoDB connection.
        - `insert_accounts(self, accounts)`: Inserts accounts into a MongoDB collection.

   3.2. Functions

      - **read_accounts_from_json(json_file):**
        Reads account data from a JSON file and returns a list of Account objects.

      - **write_accounts_to_json(json_file, accounts):**
        Writes a list of Account objects to a JSON file.

4. Usage

   - Replace the placeholder values with your desired input JSON file (`input_accounts.json`), output JSON file (`output_debt_accounts.json`), MongoDB connection URI (`mongodb_uri`), database name (`database_name`), and collection name (`collection_name`).

   - Ensure that the MongoDB Docker container is running.

   - Run the script (`main.py`) to execute the program.

5. Example Usage

   ```python
   # Example usage:
   input_json_file = 'input_accounts.json'
   output_json_file = 'output_debt_accounts.json'
   mongodb_uri = "mongodb://localhost:27017/"
   database_name = "mydatabase"
   collection_name = "mycollection"

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


MongoDB Tool Configuration

Use your preferred MongoDB client tool to connect to the running container.

Configure the tool with the following parameters:

Host: localhost
Port: 27017
Database: mydatabase (or your specified database name)
Collection: mycollection (or your specified collection name)
Input JSON File Content (input_accounts.json)

[
  {"account_number": "1001", "balance": 500},
  {"account_number": "1002", "balance": -200},
  {"account_number": "1003", "balance": 1000},
  {"account_number": "1004", "balance": -500},
  {"account_number": "1005", "balance": 300}
]


Notes

Make sure to adapt the script and configuration according to your specific use case.
The MongoDB Docker container's data is not persisted by default. Consider using volumes for data persistence in a production environment.
Adjust the MongoDB connection URI in the script based on your MongoDB deployment (e.g., authentication, replica set).
The example assumes a simple MongoDB container setup. Adjust the MongoDB Docker command based on your requirements.
