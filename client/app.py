from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message',methods=['GET',"POST"])
def post():
    data = request.get_json(force=True)
    #print(data)
    query = data['query']
    #print(query)
    if request.method == "POST":
    	url = "http://127.0.0.1:5002/jeremyzhang7413/chatbot/ask"
    	bot_question = {'input':query}
    	data = requests.post(url,json=bot_question)
    	print(data)
    	data_1 = data.json()
    	print(data_1)
    	info = {'reply':data_1['reply']} 
    	resp = jsonify(info)
    	#print(resp)
    	return resp

if __name__ == '__main__':
    app.run("0.0.0.0", port=5004, debug=True)


