from flask import Flask, request, response

@app.route('/', methods=['GET'])
def root():
    
    res = { 'success':'' }
