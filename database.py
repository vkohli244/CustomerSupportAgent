from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings


Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(String, primary_key=True, index=True)
    customer_email = Column(String)
    products = Column(JSON)
    tracking_number = Column(String)
    shipping_status = Column(String)

def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"

    if not database_exists(url):
        create_database(url)
        print("Database created.")
    else:
        print("Database already exists.")

    engine = create_engine(url, pool_size=50, echo=False)
    return engine

# These are the objects that need to be defined at the module level
# so they can be imported by other files.
engine = get_engine(**settings)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This section of code will only run when the file is executed directly.
if __name__ == '__main__':
    # This call now only creates the tables when the file is run as a script.
    Base.metadata.create_all(bind=engine)
    print("Tables created.")
    print(engine.url)