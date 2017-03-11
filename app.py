#!flask/bin/python

from flask import Flask, jsonify

app = Flask(__name__)

ip = [
	{
		'id': 1,
		'name': 'some insurance provider',
		'address': '9818 flatlands ave',
		'number': 9175898478,
		'services': ['sex', 'face']
			
	},
	{
		'id': 2,
		'name': 'some insurance other  provider',
		'address': '9820 flatlands ave',
		'number': 9175848478,
		'services': ['sex', 'face']
			
	}
]


@app.route('/geia/api/v1.0/ip', methods=['GET'])
def get_ip():
	return jsonify({'providers': ip})



if __name__ == '__main__':
	app.run(debug=True)




