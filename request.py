import requests

URL = "http://127.0.0.1:5000"

def getPredict(path):
    """
    Flask サーバにgetを投げる
    パラメータは画像のファイル名
    """
    print("request.py > start")
    URI = "/predict"
    query = {"path": path}

    r = requests.get(URL + URI, params=query)
    print("request.py > end")
    return r

if __name__ == '__main__':
    getPredict("/home/nvidia/Pictures/test.jpg")
