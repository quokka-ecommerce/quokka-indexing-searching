
# map product to indexable product
import sys
sys.path.append("/home/zaicheng/Project/quokka-dao-python")
from product.common_object.product_detail import ProductDetail


class IndexProductMapper(object):

    def __init__(self):
        self._mapper_dict = dict()

    def map_to_index_product(self, product):
        assert type(product) == ProductDetail
        ret = product.__dict__()
        ret.pop("attribute")
        ret.pop("review")

        for k, v in product.attributes:
            ret['attr_' + k] = v

        return ret
