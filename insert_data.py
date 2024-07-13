from sqlalchemy import insert
from create_tables import users_table
from connect_database import engine

# Create an insert statement for the users_table with specific values
statement = insert(users_table).values(name="Frank", full_name="Ocean")

# Establish a connection to the database using the engine
with engine.connect() as connect:
    # Execute the insert statement using the connection
    connect.execute(statement)

    # Execute the insert statement again with multiple sets of values
    connect.execute(
        statement,
        [
            {"name": "Joe", "full_name": "Joe Biden"},
            {"name": "Susan", "full_name": "Susan Boyle"},
        ],
    )

    # Commit the transaction to save the changes to the database
    connect.commit()


# "statement" refers to a SQL statement, which is a precise instruction that can be executed by the database. It does not mean "data" but rather the command or query that operates on the data in the database.
