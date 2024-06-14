# import click
# from api.models import db, User
# """
# In this file, you can add as many commands as you want using the @app.cli.command decorator
# Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
# with youy database, for example: Import the price of bitcoin every night as 12am
# """
# def setup_commands(app):
#     """ 
#     This is an example command "insert-test-users" that you can run from the command line
#     by typing: $ flask insert-test-users 5
#     Note: 5 is the number of users to add
#     """
#     @app.cli.command("fill-db")
#     def fill_db():
#         """ Este comando rellenará la base de datos con datos de ejemplo. """
        
#         db.drop_all()
#         db.create_all()

#         try:
#             users = [
#                 User(email="diana@gmail.com", password="111111"),
#             ]
#             db.session.add_all(users)
#             db.session.commit()
            
#             people = [
#                 People(
#                     birth_year= "Grogu", 
#                     eye_color= "Black",
#                     hair_color= "White",
#                     url_img1="https://i.insider.com/5de6df0d695b583f4f17f695?width=700"
#                 ),

#                 People(
#                     birth_year= "C-3PO", 
#                     eye_color= "Black",
#                     hair_color= "White",
#                     url_img1="https://m.media-amazon.com/images/I/71LFpKcZjGL._AC_UF1000,1000_QL80_.jpg"
#                 ),

#                 People(
#                     birth_year= "Kylo Ren", 
#                     eye_color= "Black",
#                     hair_color= "Black",
#                     url_img1="https://m.media-amazon.com/images/I/71Ew2YMc26L._AC_UF894,1000_QL80_.jpg"
#                 ),
                

#                 People(
#                     birth_year= "Conde Dooku", 
#                     eye_color= "Brown",
#                     hair_color= "White",
#                     url_img1="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEBAQEBIVFRAVEA8QDxAVFRAQDw8PFRUWFhUVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFxAQFy0dHR0tLSstLS0tLS0tLS0tKy0tLS0tKy0tLS0tLS0tKy0rLS0rKy0tLS0tLS0tKy0tMDctK//AABEIAMIBAwMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAABAAIDBAUGBwj/xAA9EAABAwEEBwUHAgUEAwAAAAABAAIRAwQSITEFBhNBUWFxIoGRobEUMkJSwdHwI3IVM2Ki4SRTsvEHFkP/xAAZAQEBAQEBAQAAAAAAAAAAAAAAAQIDBAX/xAAiEQEBAQACAgMAAgMAAAAAAAAAARECIRIxA0FRMnETImH/2gAMAwEAAhEDEQA/APLLiWzVvYpbBdPFvVW4iGKzsUdgnimq1xO2asignCgVrxFbZo7Mq0KKcKRTxFUUkdkrWyKWzV8RW2SWyVrZpbM8EwVNilsl3ehtVaYE2iX1TBFNt7Z0h/W4RJ5SB1XTmxU2M7Vms1RobFzZUsQN3u5rNs9avjXj2zSuL0C06LsVqLqdBos1qxNISfZqpzuEOJLHHcQYywXG1aTmuLXNLXAlrmkQ5rhgQRuViKgYjslYARBWsNVhTT9mVZvoGor4wV9gUtkp7ySYIdkELgU8IFiYiIBqeAE7ZcvVHYcvVXKGEIEKQ0eXqkKXL1TKITCEhWNlyQLOiYIMOCHcp7vJLuUxVeEFZlJXEMNNK6tCvZSNyqPpFZ105cMRBoTg1C6kqwcAnAJgcnA9VUPAPBPaCmNKka5aCAPBGDwT21CnbQcFcTTAzkrWjqX6jSRkRH7sh5lRCoFp6DszqtSG4RDnHHIScI3wD4Kc7OPG1eMtuO6o0Tg04ZQOAj1Ulss4aI6FVLdaalOmDSp7Spk1k4d5CytGaatdoJp1bOxkElz75JAaYIDSJx3L4/dtr6E+oxdZalOjUp1KlNtRpcQ9jpF5pzIIMtcNxBwhO1x0eG1mVgS5lajTqh5i850Q+Y3yJ71yGmdNOtDwXMhreyccsQCfziu21gtTPZbDQxL2UAXzuDiS0eH0X0fgjx/LdrmDSCZsVYLuSaSvRkckYs6Is6KIlMgXs/LyUrKR4INqEZlF1qO5a6Q8QNya8z/1KiLid6TW81dEkoXXHekDzR2nMoJGWaMyjshvd5KF1Y7lGXu4psE7qTT8XkojZuajvHiltCpbAXWfmmGhzTtoUr/JTpUez5op08klOh6xpzUMOaatkcHsOIbILu471wFu0Q5hLXNIIwIIIIW9oHWqrQIuu7O9pxaeoXcUdJWLSDQ2u0MqxAdljyd9CvP3Hq2z33Hi1SxFQmzFem6wakVKUvpfqU85HvAcwuMtFkImQt8bEvGcpsYmwKcKRVyo2FFfXWY43jYiFJSBiO2CW1C10x2IpoikOCLawTxWHEeC10hNphb2qlMGq6nvcA4Nm7tLhksmd/3GSwxWbxCoad0tsgxtJxFQPBqObINMNxgEbzjKx8sl4WNcLnKV6zZnuu5SSZBywMqs20Uqbqhc4SSQ6o68Gm6JLb2QAxHWVo0aINJj2OvMc0Oa4GZaRIK43T7al1zwWtZJFIDaFzgMi+GwAYJjgvizj/tlfSnc6eb2+6K1cUyDTdUqXYxBEkiOS7HSNL9RwJBIDGk/taB9Fz2hrCatV1R7QKVOpNaIgQC4Adbsd63HVWzMySZMzMr63wTrXzvkvaLZhIUgiXtTC9q9HTCTYDiEDQb8wTA5vNEFvAqdA7BvFDZNRvt4HyRFZo+H0ToNuNQujh5qUWkbmjwCArjh5BURwPl80CBw9FM60D8A+qbt277x8AnQgu/mCVzl6KyLSz5T4hI2lny+anQq3eSEdFOazOB8UC9nNOhBjySh3EKSW8/FNMKYGQ7kijAQTBJTcr9mtRbkVzArH5ipqdbmVw2PRx549T1e1zqUYa432fKTl0O5dS+yWLSDZZDKpGOQM8xvXh9G1cytfR+lHMILXEHkViz8byXudV0+ntTqlEk3ZZucMR38FzFo0dG5egav69GBTtAvtynC9HPiti3au2a1sNSzuaHcN3eNyTnntLyzrk8afQHLxTNiF1em9W6tFxDmRwMYHoVzVraWgkjJdZziX497hUrHOZa0fM5zWDzxPdKlLLGz+ZaC48KTCWzu7bo/4rmq1R28klUqlQ70/wAn/HG8MbukNOU2kiyU7gggVXnaVsRu+Fu/ECea5i1PwJ7+7enVHYrV0To2lVpVHPeQ4G6Yi7SBntvnMQCYwmM1jlyvInFtama/Os7aVmtMus7DDKjcXsZjDS34mye6F2Wmda7C6neZWYQ6ciJIxGPA4+S8dbQpBomuSYGDaZeyDdwBLgQ4S6QcMBjjgxlmouMmsWgXL00+0JLQ6O1BiXRjJu5CQvP4S3cdZz5cfTttXKlGq2vRpVWbR72uuuNwGm0udDXEXSZInHC6FetGh30/fYW8z7vccjkfBcNY9G3YdTtFMEsDndvZvpi9ea7ODEA4kYmMCu1dperZA0CrfpFxpXZBcezg7KPdDCMx2BmHEn1fFy6xw5Xab7EOKIsQWxZ69ltdIODhZ7QOy8hv+mc7cXNHuA44jfuKxLY6tSqOp1BDhniCCNxad4OYK7aymFjCPsY/B/lVBbHJ3th3pq4s+xj8H+UvZBy8FALVyR9p5JomFiCI0e3HHyTGWw/L5KX2wn3WE9yapv8ACwd/krFDR1MCCJ54hBtSofgPeCpWbQ7lNAOjqfyjxcgdGM+Uf3fdWW0H8Qnig9NFH+FU97fBzgg7RdLhj1K0PZ3fkoezlBju0UOPqh/DG8fIrZ9nKjdZymoyf4c3j6oLS9nPFJVXn4KkBTAE8BeVpI16sUq6qgKRoRqXGpZ7WQui0PrDUpOBa4g9VxzFZp1CrjrOe9V7XojXGjXbs7S0Y4XokHqN3codPakU6zL9mcCDjdmQehXlFmtZGRXS6F1wq0HAB2EYtOIPcsZnpfH74sTTWrVSk665hETOC5m16OI3L6DsGnbJbmXKwaHZY8eTtyw9Y9QZBfQ7Qzj4h9039PKXrl08FrUMSVUfTk4hd1pXV9zCQWrmrbYS2cNyVnlwYjHep9UKjd6mNCAosRgVlysqs18GfwrUpWgkNaXEtA7AJJDRjgBkMys6tT3hGhVjBXjcZdFonSrqL5BOILTBiWnMTu4g7iAV0Fp0ia2zD4JuOFKoAG37uLmuAwBjtRxa/iuILpEeas2e2Ou3JghzajHfJUbk7ocjy6BdePPOkx1LQpAzkp7C3aMbUAAkSW/K7It7jI7lfZZgvR0irZ6jAMWSrtK0Ux/8p8E4WEclNT0azeT0CnSmttY3UfRTUrVwpkeAViho9jcgepkq4ywzkB4x9Fm2CGnVJEx5BSseflUwsD/l/uEIiwPPweJBU2KjDj8nTEFEVB8qebJdzpA8wQfJRVKjP9ojnEFQSumJueShM53D4xCabZTGdMnrdKq1NIUv9o9wH3VkRYfPynxVeoTw81WdpZg+B3gB9VG7S9L5Hz3Eeq1lNTEO/CPskqR0w35D/b9klcv4OHantKY1OC8rR4UgTWpy0HtKla5RNT2hFidhVLSFquu6NH1+6tsCxtMO/Ujm0eGP0Urc5WN7RelnMiCvQ9WtfHshrzebwO7ody8bbVhW7NbCMZUdNnLqvo7/AEdvbuFQjkH/AOVw+tOoL2AuYLzM5G7qFxWitPuYQQ4r0fVv/wAgzDK3aGV74h91nMTxvH+PbyXSOhXMJwwXP2ugQvpfSuhrHbKT6tNzWkNJJGAG/tDcvEtaNCmkXEYskw8TGGBzyxwReuUcO+RmoXNjEZcFcrCCqzhCjz8oDXZRktayaNL2io3tsycG4VaZ5j/sH0xxEicvBbFjsdqpFtam2DuN6nBacw5pMkdQtcf6ZdLqvVLC6z1M42tF26pTyJHSBhux4LpmFZ+jW+0UwyrSNK1NG3s7pwDzhIOTqT/cJExImCATepOkAxHEHAjkV6uPpNWmFWaLwqrFZpBSqvU3BTCoFVYnys4q22upG11RCIKmC6+0KrVrJriontSKrV6qp1Hc1aq0Qqz6YW4yqVCeJ8VXeJ3lWnwoHOC1KINmkpkldMcLQq3uR4KYKi0wnis7ivFrovAp4KpNtBhObaHTOC1qNGmFI1ZlS1OdvU9O2cc01Wg1c9aXXqs/ud44BaDbU4kzks6li6oeYb4D/KAPTL+McM1LUMAncFXaIEnM4lSqmNriT4dVYsGkyCMVjWt+Q7yo6VQghZt7Jzx6LZdZqjWlrXkAggwSJCZS1lxuP7TCe00nDHAkH4XeR3grj21TCtaJttOnaKNSs2/SbUa6o3OWjlv6LW46TnvTt6ugLDQcy01QKodDmWYm6wCJvPZjOBGE3fQaOs2p9htQpGgG2W1OuA06bP0SSMBVYIbTOMXhHEgrlv8A2ahVq1rRVY41Wvmxsb/LYQTDnN3kSIGWC29F6Qe4uv1XCJqWlzQP0wRAp3jvz7+i89t3XS8OF9OVr6rVKFW7eeyox9yo40mvdSfvJbe7IxmYOBBkjFTWHTlQOdTrV6bi0lt94bRriMHMeKjdnVbmIcZ5xgtbXTWShaGUXtvNe1hs9Rz4LqrGRsqhO8w4grzu3Vg83iCKk3X7w6MjPHd4FenyySzp4rO8rd0jbn2apSfRIAbUc9jWOLqBwhwaxxNwOBgtkgjjAjqbRrLSm8ATeax453mh2PMSvMFrWIm4J6dwAH0SfJfrpZHZu1mnECFPYdZhPaXHShJUvKtu9tWttNvuiVjVNcKt/wDpnJcy6Uwqbb9nT0Oya307hLgZjIcVTra6T7rYE5nErig9AuU3l+jrbVrhUMtAA5qlT1tr4i90nHFc66pKap3+jqhrtVwvMaeOaba9cHuwbTA5yuUJTTUV8uX6Np+sFT8yVY6ZqTie5Zhcmqbf0bLdP1OKSx0k7NXYSRvJStIUpSiCigakCnIgIHh0AlVrGcHH+o/RS2p0MJVegYpN4mT4laIkqY4c01wRJgJjnQCeRUVWqU5JwmfRRss8HtSG+auseBHn1Qe+enqpkTEns05Pw8fRVnUDjiMCRvGRhNvlpkYcjBBSbXwkg5uJMG7JM5pohdTLTIOO4gqwdLVbmykBuJMSC5x+I8T9lXqVQVXJWanlZ6dRR1TrVbM2u17Lzy8U6cy6ts714AjAPmA1pi9e6TzBMrpbJrMwWanSqUy51Mm41puUifhqEDJ4xEjOZ3LJpXrRaH1KkS5zqtSAGiSZyGAkn1WrJ9Iz1r2QdhvSfNZdcgvcRleMcIWxSENaOAHopCHpISlK00JTHBPlRucpQISQvJt9RScggXJpcgc4KIhOL0y8ogJISlKgMpJspKmLV5G8oQ5OlXVTtcnXlBeRDk1FgFGVXD06m6SBzV0DSz4a1vKe8pVcLjeAHko7cb1Zo/qHgMUqjpcStX2kGo5MtFSGk9PVNJxUVsPZA5rNWp7+8BLaqgysRhu9FKKgKmprU0XYxVeS/wDlt94DNx3ALffSBFzAQOzGDXco45LkdHaRNJ5ObScRkeoW7UryMD/XTM5jeFi9u3x8pirpiwNc3asEEGKjeBHLz71gPaRn3cCuj9qDyIGDw4Ox+JoP2PisCs4i9TPH0yRjnJ7RK9Z61yi+Pee4MHQCT6+aoJ7jkOHqc1ZccwC2DUmDxA9I+hWQwK/Sd2Ryc4ec/VWLE95C8o5SvJrSS8m3ky8heRKeSmym3kLyBxcmkoFyaXKB0oSmygSgdKEppKEqGnygmpImpZRCivI3lVSyleUYclKadJZU9jxeOUlVLytWQwHu5ALXH2IGOmq48A4/RFhzKioHCo7jA+v2UlPJaSE3NV7ae0BwHqrLFStDpefDwWeQjKSKSwgEKejaYicYy6cE2ExzVcJcaO1DQYdGIqUzvnp4LPq1S5xc7EnElMSUW3SRQSlESl2XUKxZTIeOEP8AofXyVRuY6hWtGP8A1BORlp6HBagklCQm1RdcWnMEhNvKNHygSmXkryGnShKbeQLlDTryV5MvJFyIJclKbKF5A6UrybKV5AZSTZSQPvJSmpSgfKUpiEoJJVkuij+5x+ypqza8Gsby81rj9oaMKY5mU/cE2vm1vRF5Ww9pWeeKuVTDT+ZqmscikkEEWqCUhNKdKY4qhpSCBRUAAShOSKIaCn0XQQU0ZFOptzSK0NKNxZUGT24/uGBVGVqUm7Szvb8TO23uxI8LyyZWuc739XTryV5NlCVgPvIShKEoHSlKbKKAyggkgKSCSApIJICgkkiChKSSB1MSQOJCs2gzUaOn3UVlHbHIE/nii53bJ4Arc9B0y4ngjOKazAdU5gVDLSez3quprUcu9QrFASBRQCgN5JBIqoSKARQFBySDlQ6OypKAwPcmOGAUlnGBVnsaGia11306fh8VRttG5UewZB2H7Ti3yIUlldB75U2lmTcf1Ye7LynwWr3x/oZySSS5NEkkkgSSSSBJJJIEkkkgCKSSApJJIEkkkgnsebv2qM+8Uklv6SpX7k5qSSv2ILXmOihCSSxQigEUlEFJJJFBu9FJJVCQckkgkqZJ9myKSS19qko5q1av5TutP6JJLc/jRllJFJcQAikkigikkiEkkkikmlJJEJJJJB//2Q=="
#                 ),

#                 People(
#                     birth_year= "BB-8", 
#                     eye_color= "Black",
#                     hair_color= "None",
#                     url_img1="https://m.media-amazon.com/images/I/61qVLItOMuL.jpg"
#                 )
#             ]

#             db.session.add_all(people)
#             db.session.commit()
            
#             favoritePeople = [
#                 FavoritePeople(user_id=users[0].id, vehicle_id=people[0].id ),
#                 FavoritePeople(user_id=users[0].id, vehicle_id=people[1].id ),
#                 FavoritePeople(user_id=users[0].id, vehicle_id=people[2].id ),
#                 FavoritePeople(user_id=users[0].id, vehicle_id=people[3].id ),
#                 FavoritePeople(user_id=users[0].id, vehicle_id=people[4].id ),
#                 FavoritePeople(user_id=users[0].id, vehicle_id=people[5].id )
#                 ]
#             db.session.add_all(favoritePeople)
#             db.session.commit()

#             print("La base de datos ha sido poblada con datos de ejemplo.")
            
#         except Exception as e:
#             db.session.rollback()
#             print(f"Error al llenar la base de datos: {e}")