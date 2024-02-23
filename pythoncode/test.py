import requests
from dope.session import get_session


def upload_to_s3(bucket_name, object_name, data):
    session = get_session()
    s3 = session.aws_client("s3")
    s3.put_object(Bucket=bucket_name, Key=object_name, Body=data)

def get_api_data(api_url, method='GET'):
    response = requests.get(api_url, method)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()

if __name__ == "__main__":
    api_url = "https://data.ssb.no/api/v0/dataset/1052.csv?lang=no"
    bucket_name = "sb1u-test-dataplattform-f1-storage-integration"
    object_name = "ssb-test-fil"

    try:
        data = get_api_data(api_url)
        upload_to_s3(bucket_name, object_name, data)
        print(f"Lastet ned SSB API og flyttet til S3 bucket")
    except Exception as e:
        print(f"Feil: {e}")