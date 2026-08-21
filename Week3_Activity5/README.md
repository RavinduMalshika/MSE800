## Database Schema Overview

4 Tables are required

| Table Name | Primary Key | Foreign Keys | Description |
| :--- | :--- | :--- | :--- |
| `customers` | `id` | None | Stores registered customer profiles. |
| `currencies` | `code` | None | Defines supported ISO currency codes and names. |
| `rates` | `id` | `from_code`, `to_code` | Logs historical and current exchange rates for currency pairs. |
| `transactions` | `id` | `customer_id`, `from_code`, `to_code` | Records executed money exchange trades. |

---

## Schema Justification

### 1. `customers` Table
* Essential for tracking system users, attaching transactions to specific individuals, and avoiding duplicate customer registrations.

### 2. `currencies` Table
* Serves as a lookup table for valid currency codes (e.g., `USD`, `EUR`, `GBP`). Using explicit foreign keys to this table guarantees that rates and transactions cannot be recorded for invalid or unsupported currencies.

### 3. `rates` Table
* Separates conversion rates from transaction records to allow rate updates over time. Instead of overwriting existing records, new conversion entries maintain a historical record of rate updates over time.

### 4. `transactions` Table
* Provides an immutable audit log for every currency exchange performed through the CLI. Storing the exact `amount_given` and `amount_received` alongside a timestamp ensures financial accuracy even if conversion rates change in the future.
