from flask import Flask, url_for, request, redirect, abort,jsonify


app = Flask(__name__, static_url_path='', static_folder='staticpages' )

products = [
    {"id":1,"Description":"HP", "Category":"JK", "Price":1000},
    {"id":3,"Description":"Ruth", "Category":"rK", "Price":40},
    {"id":4,"Description":"K", "Category":"jK", "Price":190},
    {"id":5,"Description":"Rory", "Category":"kK", "Price":10},
    {"id":6,"Description":"K", "Category":"lK", "Price":100},
    {"id":7,"Description":"Emma k", "Category":"pK", "Price":1700}
]
nextProductId=8

@app.route('/')
def index():
    return 'hello'

@app.route('/store')
def getAll():
    return jsonify(products)

@app.route('/store/<int:id>')
def findID(id):
    foundProducts = list(filter(lambda t : t["id"]== id, products))
    if len(foundProducts) == 0:
        return jsonify({}), 204
    return jsonify(foundProducts[0])

    return "find by ID"+str(id)

#curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\",\"Author\":\"Ruth\",\"Price\":15}" http://127.0.0.1:5000/books
@app.route('/store', methods = ['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
        
    product={
        "id": nextId, 
        "Tile": request.json["Title"],
        "Author":request.json["Author"],
        "Price": request.json["Price"],
    }
    products.append(product)
    nextProductId =+1
    return jsonify(product)

    
#curl -X PUT -d "{\"Title\":\"newtest\",\"Author\":\"newRuth\",\"Price\":4415}" -H "content-type:application/json" http://127.0.0.1:5000/books/4
@app.route('/store/<int:id>', methods = ['PUT'])
def update(id):
    foundProducts = list(filter(lambda t : t["id"]== id, products))
    if len(foundProducts) == 0:
        return jsonify({}), 404
    currentProducts = foundProducts[0]
    
    if "Title" in request.json:
        currentProducts['Title'] = request.json['Title']
        
    if "Author" in request.json:
        currentProducts['Author'] = request.json['Author']
        
    if "Price" in request.json:
        currentProducts['Price'] = request.json['Price']
        
    return jsonify(currentBooks)
#curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/store/<int:id>', methods = ['DELETE'])
def delete(id):
    foundProducts = list(filter(lambda t : t["id"]== id, products))
    if len(foundProducts) == 0:
        return jsonify({}), 404
    products.remove(foundProducts[0])

    return jsonify({"done":True})

if __name__ =="__main__":
    app.run(debug = True)