import click
from api.models import db, User, People, FavoritePeople
"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("fill-db")
    def fill_db():
        """ Este comando rellenará la base de datos con datos de ejemplo. """
        
        db.drop_all()
        db.create_all()

        try:
            users = [
                User(email="diana@gmail.com", password="111111"),
            ]
            db.session.add_all(users)
            db.session.commit()
            
            people = [
                People (
                    birth_year= "Grogu", 
                    eye_color= "Black",
                    hair_color= "White"
                    url_img1=https://i.insider.com/5de6df0d695b583f4f17f695?width=700
                    ),

                People (
                    birth_year= "C-3PO", 
                    eye_color= "Black",
                    hair_color= "White",
                    url_img1=https://m.media-amazon.com/images/I/71LFpKcZjGL._AC_UF1000,1000_QL80_.jpg
                    ),

                People (
                    birth_year= "Kylo Ren", 
                    eye_color= "Black",
                    hair_color= "Black",
                    url_img1=https://m.media-amazon.com/images/I/71Ew2YMc26L._AC_UF894,1000_QL80_.jpg
                    ),
                

                People (
                    birth_year= "Conde Dooku", 
                    eye_color= "Brown",
                    hair_color= "White",
                    url_img1=
                    ),

                People (
                    birth_year= "BB-8", 
                    eye_color= "Black",
                    hair_color= "None",
                    url_img1=https://m.media-amazon.com/images/I/61qVLItOMuL.jpg
                    ),
            ]
            db.session.add_all(people)
            db.session.commit()
            
            favoriteVehicle = [
                FavoritePeople(user_id=users[0].id, vehicle_id=people[0].id ),
                FavoritePeople(user_id=users[0].id, vehicle_id=people[1].id ),
                FavoritePeople(user_id=users[0].id, vehicle_id=people[2].id ),
                FavoritePeople(user_id=users[0].id, vehicle_id=people[3].id ),
                FavoritePeople(user_id=users[0].id, vehicle_id=people[4].id ),
                FavoritePeople(user_id=users[0].id, vehicle_id=people[5].id )
                ]
            db.session.add_all(favoriteVehicle)
            db.session.commit()

            print("La base de datos ha sido poblada con datos de ejemplo.")
            
        except Exception as e:
            db.session.rollback()
            print(f"Error al llenar la base de datos: {e}")