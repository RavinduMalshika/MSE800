CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS currencies (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_code TEXT,
    to_code TEXT,
    rate REAL NOT NULL,
    FOREIGN KEY(from_code) REFERENCES currencies(code),
    FOREIGN KEY(to_code) REFERENCES currencies(code)
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    from_code TEXT,
    to_code TEXT,
    amount_given REAL,
    amount_received REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(from_code) REFERENCES currencies(code),
    FOREIGN KEY(to_code) REFERENCES currencies(code)
);
