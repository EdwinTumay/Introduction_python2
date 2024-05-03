Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

for item in data:
    user = User(id=item['id'], name=item['name'])
    session.add(user)

session.commit()