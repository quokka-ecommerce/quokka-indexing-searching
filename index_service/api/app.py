import requests
import pysolr
from flask import Flask, jsonify, request

app = Flask(__name__)


SOLR_URL = "http://localhost:8983/solr/quokka-search/"
solr = pysolr.Solr(SOLR_URL, timeout=10)


@app.route('/quokka/products/get_all_products', methods=['GET'])
def get_all_products(limit=1000):
    raw_results = solr.search("*:*")
    return jsonify({'products': raw_results.docs})


@app.route('/quokka/products/search', methods=['GET'])
def search():
    query = request.args.get("query")
    raw_results = solr.search(query)
    return jsonify({'products': raw_results.docs})


@app.route('/quokka/products/get_filter_products', methods=['GET'])
def get_filter_products():
    filter_input = request.args
    query_dict = {}
    for k, v in filter_input.items():
        query_dict['fq'] = k + ":" + v
    raw_results = solr.search('*:*', **query_dict)
    return jsonify({'products': raw_results.docs})


if __name__ == "__main__":
    app.run(debug=True, port=8068)
