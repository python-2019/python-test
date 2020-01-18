import json

class jsonUtil(object):
    """
    json 工具类
    """
    @staticmethod
    def json_2_dict(json_str):
        """
        json字符串 转字典
        :param json_str: json字符串
        :return: 字典
        """
        return json.loads(json_str)

    @staticmethod
    def dict_2_json(dict):
        """
         字典 转 json字符串
        :param dict: 字典
        :return: son字符串
        """
        return json.dumps(dict)


if __name__ == '__main__':
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
    json_dict = jsonUtil.json_2_dict(jsonData)
    print(json_dict["a"])

    dict___json = jsonUtil.dict_2_json(json_dict)
    print(dict___json)
