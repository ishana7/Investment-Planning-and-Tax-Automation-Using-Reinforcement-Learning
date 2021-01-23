import boto3

def upload(source_file, bucket_name, object_key):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket_name).upload_file(source_file, object_key)
    except Exception as e:
        print(e)

'''

def print_file_list(bucket_name):

    bucket = s3.get_bucket(bucket_name)

    for key in bucket.list():
        print (key.name.encode('utf-8'))

def get_url_of_file(bucket_name, object_key):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket_name,
            'Key': object_key
        }
    )



def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', help='The path and name of the source file to upload.')
    parser.add_argument('bucket_name', help='The name of the destination bucket.')
    parser.add_argument('object_key', help='The key of the destination object.')
    args = parser.parse_args()

    upload(args.source_file, args.bucket_name, args.object_key)

    url = f"s3://{args.bucket_name}/{args.object_key}"

    print(url)

if __name__ == '__main__':
    main()

'''

