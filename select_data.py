from create_tables import users_table
from connect_database import engine
from sqlalchemy import select

# Create a SELECT statement for the users_table
statement = select(users_table)

with engine.connect() as connect:
    result = connect.execute(statement)

    # Note: In newer versions of SQLAlchemy, 'result' is a 'Result' object which is an iterable
    # result set. You can use the 'fetchall()' method to fetch all rows or iterate through the result.

    for row in result:
        # Print each row from the result set
        print(row)
        print(f"{row.name} - {row.full_name}")
