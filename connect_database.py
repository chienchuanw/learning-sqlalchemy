from sqlalchemy import create_engine, text

# Use SQLite as database engine
# Create and  name the database to sample.db in the current location
# echo = True will print log in console
engine = create_engine("sqlite:///sample.db", echo=True)

# Establish a connection to the database
# Use 'with' to ensure the database connection is properly managed and closed automatically
with engine.connect() as connect:
    # Execute a simple SQL statement that selects the string "Hello"
    # Note: The string passed to 'text' needs to be a valid SQL statement. Otherwise, it will errors
    result = connect.execute(text("SELECT 'Hello'"))

    # Print all results of the query (in this case, it will be a single value: "Hello")
    print(result.all())
