#import library
from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
from werkzeug.wrappers import response

#inisiasi object flask
app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

#inisiasi object flask_cors
CORS(app)

#inisiasi variabel kosong bertipe dictionary
identitas = {} #variabel global, dictionary = json

#membuat class resource
class ContohResource(Resource) :
    # metode get dan post
    def get(self):
        # response = {"msg":"Halo dunia, ini app restful pertamaku"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg":"Data berhasil dimasukkan"}
        return response


#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)

