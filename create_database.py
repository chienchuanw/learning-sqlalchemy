from connect_database import engine
from create_tables import meta


# Create all tables defined in the MetaData object in the database
meta.create_all(bind=engine)

# The bind=engine argument specifies that the engine object should be used to connect to the database and execute the necessary SQL commands to create the tables.
# If you omit the bind=engine argument in the meta.create_all() method, SQLAlchemy will not know which database connection to use to execute the SQL commands necessary to create the tables.
