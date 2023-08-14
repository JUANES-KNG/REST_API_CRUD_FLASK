'''
* En primera instancia se crea el file que contiene el proyecto con su respectivo nombre en el escritorio.
* Luego se arrastra ese archivo al correspondiente editor.
* Se abre una terminal.
* Se crea un file llamado app.py donde esta sera la aplicacion de pyhton.
* se crea otro file llamado products.py donde van a ir los datos de simulaciond e nuestra rest api.
* se instala un framework de python (flask).
* Programas para permitir guardar datos POSTMAN, INSOMNIA (mas sencillo que postman) opera con las peticiones http dentro de una API y asi guardar datos.

'''

# Importamos el modulo y objetos
from flask import Flask, jsonify, request

# Lo ejecutamos
app = Flask(__name__)

# Importamos productos
from products import products

# Ruta de prueba con funcion ping y formato json (objeto)
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# ruta con metodo GET
@app.route('/products')
def getProducts():
    # return jsonify(products)
    return jsonify({'products': products}) # Lista dentro de uhna propiedad

# Ruta para pedir UN objeto en especifico por medio del nombre
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # recorrer cada producto y encontrar el solicitado
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    # Validacion
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Ruta para crear datos, peticion POST en formato Json
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

# Ruta para poder actualizar un dato
@app.route('/products/<string:product_name>', methods=['PUT']) # Metodo PUT para actualizar algun elemento de la lista
def editProduct(product_name):
    # Validacion
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# Ruta que nos permite eliminar elementos dentro de la lista
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    # Validacion
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })

# Inicializamos el server
if __name__ == '__main__':
    app.run(debug=True, port=4000)
