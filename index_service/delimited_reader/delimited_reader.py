import csv
import sys
sys.path.append("/home/zaicheng/Project/quokka-dao-python")
from product.common_object.product_detail import ProductDetail
import json


class DelimitedReader(object):

    def __init__(self, delimiter, quotechar):
        self._default_delimiter = delimiter
        self._default_quotechar = quotechar

    @staticmethod
    def _clean_product_row(row):
        try:
            row.pop("")
        except Exception:
            pass

    def read_file_into_stream(self, csvFile):
        try:
            with open(csvFile, 'rb') as opened_file:
                reader = csv.DictReader(opened_file, delimiter = self._default_delimiter, quotechar = self._default_quotechar)
                for row in reader:
                    self._clean_product_row(row)
                    p = self.form_product_from_dict(row)
                    # json.dumps(p.__dict__()).decode('unicode-escape').encode('utf-8')
                    yield p
        except Exception as e:
            raise e

    def read_file_into_stream_with_delimiter(self, csvFile, delimiter, quotechar):
        try:
            with open(csvFile, 'rb') as opened_file:
                reader = csv.DictReader(opened_file, delimiter = delimiter, quotechar = quotechar)
                for row in reader:
                    self._clean_product_row(row)
                    p = self.form_product_from_dict(row)
                    yield p
        except Exception as e:
            print e
# (self, id, product_name, upc, category_l1, category_l2, category_l3, product_unit, brand, original_country,
#                  attributes, current_price, current_stock, image_link, product_description, vendor_id, sale_history_id,
#                  history_price, reviews)
    def form_product_from_dict(self, product_dict):
        return ProductDetail.build(product_dict)


if __name__ == "__main__":
    delimiter = DelimitedReader(",", '"')
    results = delimiter.read_file_into_stream("search sample.csv")
    for result in results:
        print result
