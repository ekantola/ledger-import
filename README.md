# SQL-Ledger transactions import script

Generate SQL-Ledger compatible SQL script from transactions of a bank account's log as a CSV file.


## CSV row format

reference,transdate,actor,description,amount,account_no

reference: text/number for the transaction's human-readable identifier
transdate: YYYY-MM-DD
actor: the person, organisation or other entity to be the reference for this transaction
description: textual description
amount: numeric amount
account_no: the ledger's contra account for this transaction

See the [sample CSV](sample-transactions.csv) for more details.


## Usage

```
./ledger-csv2sql.py < sample-transactions.csv > sample-transactions.sql
```

After this, you will have the transactions in `sample-transactions.sql` and can load the data into an SQL database. PostgreSQL has been tested to work. Example:

```
psql dbname < sample-transactions.sql
```

