I created 1 class diagram for the projects scope.

Purpose: To show the structural design of the money exchange application.

Main Classes:
    - Database: Manages the SQLite database connection, and intialize the SQL schema script.
    - CurrencyManager: Handles operations related to currencies and exchange rate.
    - CustomerManager: Handles CRUD operations for customer records.
    - ExchangeService: Handles the execution of transactions and its calculations.

Relationships:
    - CurrencyManager -> Database: CurrencyManager requires a Database instance to execute SQL queries.
    - CustomerManager -> Database: CustomerManager requires a Database instance to execute SQL queries.
    - ExchangeService -> Database: ExchangeService requires a Database instance to execute SQL queries to get transaction logs.
    - ExchangeService -> CurrencyManager: ExchangeService relies on CurrencyManager to fetch exchange rates during a transaction.
