#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    #sample company here
    apple = Company(name='Apple', founding_year=1971)
    google = Company(name='Google', founding_year=1975)  
    microsoft = Company(name='Microsoft', founding_year=1975)

    #sample devs here
    esther = Dev(name='Esther')
    bob = Dev(name='Bob')
    reign = Dev(name='Reign')

    session.add_all([apple, google, microsoft, esther, bob, reign])
    session.commit()
    
    #sample freebies here
    sticker = apple.give_freebie(esther, 'sticker', 10)
    mug = google.give_freebie(bob, 'mug', 5)
    t_shirt = microsoft.give_freebie(reign, 't-shirt', 3)

    session.add_all([sticker, mug, t_shirt])
    session.commit()

    print('Database seeded successfully!')
    session.close()


    

    
