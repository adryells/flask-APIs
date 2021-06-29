from flask import Flask, request, jsonify
import json

app=Flask(__name__)

lista = []

@app.route('/', methods=['GET'])
@app.route('/blog/', methods=['GET'])
@app.route('/blog/<int:postID>/', methods=['GET'])
def get_posts(postID=None):
	if postID:
		return f"blog: {postID}"
	else:
		return "Blog"

@app.route('/blog/post/', methods=['POST'])
def post_posts():
	lista.append(json.loads(request.data))
	return jsonify({"status":"Usuario cadastrado!"})

def alter_posts(postID=None):
	if postID:
		dados = json.loads(request.data)
		lista[postID] = dados
		return jsonify({"status":"Usuario alterado!"})

def del_posts(postID=None):
	if postID:
		lista.pop(postID)
		return jsonify({"status": "Post deletado"})

if __name__ == "__main__": 
	app.run(debug=True, port='3000')

