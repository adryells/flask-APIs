from flask import Flask,jsonify,request
import json
app=Flask(__name__)

desenvolvedores = [
	{"nome": "Paulo", "habilidades":['python','django']},
	{"nome": "Hellyson", "habilidades":['python','flask']},
	{"nome": "Felipe", "habilidades":['javascript','css']},
	{"nome": "Ricardo", "habilidades":['python','javascript']},
	{"nome": "Benjamim", "habilidades":['python','html']},
]

@app.route('/dev/', methods = ['POST', 'GET'])
@app.route('/dev/<int:id>/', methods = ['GET','PUT','DELETE'])
def developer(id=None):
	if id != None:
		desenvolvedor = desenvolvedores[id]
		if request.method == 'GET':
			try:
				print(desenvolvedor)
				return jsonify(desenvolvedor)
			except IndexError:
				return jsonify({"status":"erro ao localizar dev"})
		elif request.method == 'PUT':
			dados = json.loads(request.data)
			desenvolvedor[id] = dados
			return jsonify(dados)
		elif request.method == 'DELETE':
			desenvolvedores.pop(id)
			return jsonify({"status":"excluido com sucesso"})
	elif request.method == 'GET':
		return jsonify({"devs":desenvolvedores})
	elif request.method == 'POST':
		desenvolvedores.append(json.loads(request.data))
		return jsonify({"status":"dev inserido com sucesso!"})





if __name__== '__main__':
	app.run()