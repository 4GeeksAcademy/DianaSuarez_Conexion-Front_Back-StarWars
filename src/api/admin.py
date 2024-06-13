import os
from flask_admin import Admin # type: ignore
from .models import db, User, People, FavoritePeople, Favorite
from flask_admin.contrib.sqla import ModelView # type: ignore

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class PeopleView(ModelView):
        column_list= ("usuario_id", "people_id")
        form_columns = ("usuario_id", "people_id")

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Favorite, db.session))
    admin.add_view(PeopleView(FavoritePeople, db.session))
    
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))