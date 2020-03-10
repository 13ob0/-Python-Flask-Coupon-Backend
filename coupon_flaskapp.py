from flask import Flask
from flask import request
from flask import jsonify
# import xmltodict
# import requests
# import wechatpy
# from wechatpy import parse_message
# from wechatpy.replies import TextReply
import json
import re
# from wechatpy.utils import check_signature
# from wechatpy.exceptions import InvalidSignatureException
from getCoupon import getCoupon_fun


name_re_pattern = re.compile(r'(【.*?】)')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getCoupon():

    taobao_code = request.values.get('taobao_code')
    # taobao_code = json.loads(request.values.get('taobao_code'))
    print(taobao_code)
    name = re.findall(name_re_pattern, taobao_code)[0]
    # taobao_code = message['Content']
    coupon_code = getCoupon_fun(taobao_code)
    reply_content = name + '\n' + coupon_code

    data = {
        'coupon': reply_content
    }

    print(data)
    print(type(jsonify(data)))
    # return data
    return jsonify(data)


if __name__ == '__main__':
    app.run()
