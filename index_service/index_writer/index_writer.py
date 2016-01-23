import solr
from index_service.delimited_reader.delimited_reader import DelimitedReader
import sys
sys.path.append("/home/zaicheng/Project/quokka-dao-python")
from product.product_accessor import ProductClient
from index_product_mapper import IndexProductMapper
from SolrClient import SolrClient
import json

SOLR_URL = "http://localhost:8983/solr/"
DELIMITER = ","
QUOTECHAR = '"'

class IndexWriter(object):

    def __init__(self):
        self._solr_client = solr.Solr(SOLR_URL)
        self._delimiter_reader = DelimitedReader(DELIMITER, QUOTECHAR)
        self._product_db_client = ProductClient()
        self._index_product_mapper = IndexProductMapper()
        self._client = SolrClient(SOLR_URL)

    def _persist_products(self, products):
        self._product_db_client.insert_product_detail_in_batch(products)

    def _index_products(self, products):
        print products[0]
        msg = json.dumps(products[0])
        # self._client.index_json("quokka-search", msg)
        self._solr_client.add_many(products)
        self._solr_client.commit()

    def persit_and_index_product(self, csv_file_name, chunk_size=100):
        chunked_products = []
        chunked_index_products = []
        count = 0
        for product in self._delimiter_reader.read_file_into_stream(csv_file_name):
            if count == chunk_size:
                self._persist_products(chunked_products)
                self._index_products(chunked_index_products)
                count += 1
                chunked_products = []
            chunked_products.append(product)
            chunked_index_products.append(self._index_product_mapper.map_to_index_product(product))
            count += 1
        self._persist_products(chunked_products)
        self._index_products(chunked_index_products)

        products_from_db = self._product_db_client.fetch_all_product()
        self._index_products(products_from_db)


if __name__ == "__main__":
    writer = IndexWriter()
    writer.persit_and_index_product("/home/zaicheng/Project/quokka-indexing-searching/index_service/delimited_reader/search sample.csv")
