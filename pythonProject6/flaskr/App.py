from flaskr import create_app
from .modelos import db, Cancion
from flask_restful import Api
from .vistas import vista_canciones, vista_cancion

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)

api.add_resource(vista_canciones,'/canciones')
api.add_resource(vista_cancion,'/canciones/<int:id>')