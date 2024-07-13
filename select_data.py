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


# Print the columns of the users_table
print(users_table.columns)

# Print the columns of the users_table using the 'c' attribute (an alias for 'columns')
# Which means 'c' is equal to 'columns'
print(users_table.c)

# Print the 'full_name' column object of the users_table
print(users_table.c.full_name)


# Use "WHERE" to filter
# Create a SELECT statement for the users_table with a WHERE clause to filter rows where the name column is "Joe"
statement = select(users_table).where(users_table.c.name == "Joe")

with engine.connect() as connect:
    result = connect.execute(statement)

    for row in result:
        print(row)
