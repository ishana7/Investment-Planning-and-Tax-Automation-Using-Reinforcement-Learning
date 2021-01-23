import os
import subprocess as sp
from s3_upload import upload
import re

def run_pipeline(source_file, bucket_name, object_key):
    '''
    command_upload = f"python s3_upload.py {source_file} {bucket_name} {object_key}"
    call = sp.getoutput(command_upload)
    print(call)
    '''
    upload(source_file, bucket_name, object_key)
    url = f"s3://{bucket_name}/{object_key}"

    command_analysis = f"python textractor.py --documents {url} --tables"
    os.system(command_analysis)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', help='The path and name of the source file to upload.')
    parser.add_argument('bucket_name', help='The name of the destination bucket.')
    parser.add_argument('object_key', help='The key of the destination object.')
    #parser.add_argument('flags', help='Only one of the flags (--text, --forms and --tables) is required at the minimum. You can use combination of all three.')
    args = parser.parse_args()

    run_pipeline(args.source_file, args.bucket_name, args.object_key)

if __name__ == "__main__":
    main()


#Run : python pipeline.py form_16.pdf textract-console-us-east-1-6375b349-b720-4339-99ab-c4a951ea5a70 test.pdf