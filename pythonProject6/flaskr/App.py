from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='prueba', minutos=2, segundos=25, interprete='artista')
    u = Usuario(nombre='juan', contrasena='12345')
    a = Album(titulo='prueba', anio=1999, descripcion='text here', medio=Medio.CD)
    a.canciones.append(c)
    u.albunes.append(a)
    db.session.add(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albunes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
    print(Cancion.query.all())