from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db")

with engine.connect() as connect:
    result = connect.execute(text("select 'Hello'"))

    print(result.all())
