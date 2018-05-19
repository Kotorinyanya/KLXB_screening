import requests
import json
import base64


def get_access_token(ak, sk):
    """
    Get access token.
    :param ak:
    :param sk:
    :return: token string
    """
    data = {
        'grant_type': 'client_credentials',
        'client_id': ak,
        'client_secret': sk
    }
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    req = requests.post(url, data=data)
    return json.loads(req.text)['access_token']


def screening_analysis(access_token, image, threshold):
    """
    Analysis screening image
    :param access_token:
    :param image: base64 image
    :param threshold:
    :return:
    """
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/scan_screening'
    url_para = 'access_token=' + access_token
    url = url + '?' + url_para
    image = bytes.decode(image)
    body = {"image": image, "threshold": threshold}
    body = json.dumps(body)
    body = json.loads(body)
    headers = {
        'Content-Type': 'application/json'
    }

    resp = requests.post(url, headers=headers, json=body)

    return resp.json()

def image_to_base64(image_path):
    with open(image_path, 'rb') as infile:
        image = base64.b64encode(infile.read())
    return image


def main():
    ak = 'REYaLwA1NtDBUEZdCppE6WXv'
    sk = 'SGHkZTBTTlN2aBXaLFym6jteOhIWxa8S'
    access_token = get_access_token(ak, sk)
    image_path = '1.jpg'
    print(access_token)
    b64_image = image_to_base64(image_path)
    print(screening_analysis(access_token, image=b64_image, threshold=0.3))

if __name__ == '__main__':
    main()
