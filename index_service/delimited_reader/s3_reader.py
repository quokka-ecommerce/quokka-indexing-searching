from boto.s3.connection import S3Connection

AWS_KEY = "AKIAIXJW5SPGVULNVMDQ"
SECRET_KEY = "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"
BUCKET = "quokka-ecommerce"


class S3Client(object):

    def __init__(self, bucket):
        self._connection = S3Connection(AWS_KEY, SECRET_KEY)
        self._bucket = self._connection.get_bucket(bucket)

    def read_file_from_s3(self, key):
        file_key = self._bucket.get_key(key)
        file_key.get_contents_to_filename("a.xlsx")


if __name__ == "__main__":
    s3 = S3Client(BUCKET)
    print s3.read_file_from_s3("catalog_input/search sample.xlsx")