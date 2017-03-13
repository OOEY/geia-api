#!flask/bin/python

from flask import Flask, jsonify

app = Flask(__name__)

ip = [
	{
		'id': 1,
		'name': 'some insurance provider',
		'address': ' some street',
		'number': 55555555555,
		'services': ['sex', 'face']
			
	},
	{
		'id': 2,
		'name': 'some insurance other  provider',
		'address': 'some street',
		'number': 2222225555,
		'services': ['sex', 'face']
			
	}
]


@app.route('/geia/api/v1.0/ip', methods=['GET'])
def get_ip():
	return jsonify({'providers': ip})


@app.route('/geia/api/v1.0/provider', methods=['GET'])
def get_provider():
	return "this is a providers name...i think"


if __name__ == '__main__':
	app.run(debug=True)




