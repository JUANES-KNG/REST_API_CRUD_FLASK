from flaskr import create_app
from .modelos import db, Album, Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    Album_Schema = AlbumSchema()
    a = Album(titulo='prueba', anio=1999, descripcion='text here', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    print([Album_Schema.dumps(album) for album in Album.query.all()])