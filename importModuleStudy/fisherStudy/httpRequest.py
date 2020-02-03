
import requests,sys

class HttpRequest:

    @staticmethod
    def get(url,return_json=True):

        print(sys.path)

        # 第一种：返回restful 标准
        # 第二种：返回json
        response = requests.get(url)
#如果找不到对应的书，status_code返回的是404
#根据return_json值 返回json或者字符串
        if response.status_code != 200:
            return {} if return_json else ''
        return response.json() if return_json else response.text

#如下代码可以简化如上
        # if response.status_code == 200:
        #     if(return_json == True):
        #         response_data = response.json() #返回json格式
        #     else:
        #         response_data = response.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

