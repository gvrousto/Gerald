import server_config, analyze
from flask import Flask, request, Response, json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

CLARIFAI_TOKEN = server_config.CLARIFAI_TOKEN

@app.route('/', methods=['GET'])
def root():
    print("Getting User Data")
    if request.args.get('user_tag'):
        body = analyze.scrape_account(request.args.get('user_tag'))
        res = { 'success': 'true', 'message': 'Scanning account', 'body': body  }
        return json.dumps(res)
    res = { 'success': 'true', 'message': 'Failed to retrieve account'}
    return json.dumps(res)


if __name__ == '__main__':
    app.run()
