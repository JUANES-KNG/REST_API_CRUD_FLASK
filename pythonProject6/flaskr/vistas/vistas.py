from flask_restful import Resource
from ..modelos import db, Cancion, CancionSchema
from flask import request

cancion_schema = CancionSchema()

class vista_canciones(Resource):
    def get(self):
        return[cancion_schema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],\
                                minutos=request.json['minutos'],\
                                segundos=request.json['segundos'],\
                                interprete=request.json['interprete'])

        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)


class vista_cancion(Resource):
    def get(self, id):
        return cancion_schema.dump(Cancion.query.get_or_404(id))

    def put(self, id):
        cancion = Cancion.query.get_or_404(id)
        cancion.titulo = request.json.get('titulo',cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)

        db.session.commit()
        return cancion_schema.dump(cancion)

    def delete(self, id):
        cancion = Cancion.query.get_or_404(id)
        db.session.delete(cancion)

        db.session.commit()
        return 'operacion exitosa',204