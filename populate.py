from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup_team import Team, Base, Player, User

engine = create_engine('sqlite:///teamplayer.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
team1 = Team(user_id=1, name="Jaguars")

session.add(team1)
session.commit()

player2 = Player(user_id=1, name="REggie bush", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     height=50, weight=50, team=team1)

session.add(player2)
session.commit()


player1 = Player(user_id=1, name="bill ", description="with garlic and parmesan",
                     height=25, weight=60, team=team1)

session.add(player1)
session.commit()

player2 = Player(user_id=1, name="john", description="john is a good player",
                     height=67, weight=8, team=team1)

session.add(player2)
session.commit()


# Menu for Super Stir Fry
team2 = Team(user_id=1, name="Lions")

session.add(team2)
session.commit()


player1 = Player(user_id=1, name="youaaaff", description="anffdsfdsf d sdf",
                     height=75, weight=9, team=team2)

session.add(player1)
session.commit()

player2 = Player(user_id=1, name="Peking Duck",
                     description=" he cook", height=50, weight=80, team=team2)

session.add(player2)
session.commit()

