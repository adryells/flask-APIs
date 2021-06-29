from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Desenvolvedor(Resource):
	def get(self):
		return {"nome": "rafael"}

api.add_resource(Desenvolvedor, "/dev/")

if __name__ == "__main__":
	app.run()

	"""FLASK RESTFUL NAO EM VERSAO PARAPYTHON39 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHH BOSTAAAEERRRR"""