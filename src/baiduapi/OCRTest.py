from aip import AipOcr

from src.util import jsonUtil

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def getClient():
    APP_ID = '15765872'
    API_KEY = 'Bywy2lZjSttR1xPy48cwc5QQ'
    SECRET_KEY = 'Ca0GLFtO4Ebc4qV7hVHkzScxN0Si0r7Q'
    return AipOcr(APP_ID, API_KEY, SECRET_KEY)


"""
调用通用文字识别, 图片参数为本地图片
"""


def getImageWord(filePath="a.png"):
    client = getClient()
    image = get_file_content(filePath)
    result = client.basicGeneral(image)
    print(result)
    return result;


def getImageWordUrl(fileUrl="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1603076011&di=9177ce16b27b1cd73399dad7c28706db&src=http://img1.cache.netease.com/catchpic/4/42/427E51FB37B9579277B065F7CDC3E6F4.jpg"):
    client = getClient()
    result = client.basicGeneralUrl(fileUrl)
    print(result)
    return result;


if __name__ == '__main__':
    words = getImageWord()
    for word in words['words_result']:
        print(word['words'])
    # getImageWordUrl()
