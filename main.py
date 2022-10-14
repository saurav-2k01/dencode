from flask import Flask, request
from d3ncod3 import De_ncode

app = Flask( __name__ )
@app.route("/")
def index():
    return "<h1>welcome<h1>"

@app.route("/encode")
def encode():
    string = request.args.get("string")
    layer = int(request.args.get("layer"))
    x = De_ncode(string, layer).encode_str()
    return x

@app.route("/decode")
def decode():
    string = request.args.get("string")
    layer = int(request.args.get("layer"))
    x = De_ncode(string, layer).decode_str()
    return x


if __name__ == "__main__":
    app.run(debug=True)
