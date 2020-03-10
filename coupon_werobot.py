import werobot
import xmltodict
import requests
import json
import re
import time


robot = werobot.WeRoBot(token='wechat')

name_re_pattern = re.compile(r'(【.*?】)')

# def theCoupon(taobao_code):
#     """
#     :param taobao_code: 商品页面复制的淘口令
#     :return: 商品对应优惠券的淘口令
#
#     """
#
#     # get_item_id
#     get_id_url = 'http://gateway.kouss.com/tbpub/tpwdConvert'
#
#     get_id_data = {
#         "adzone_id": "1092###60",
#         "site_id": "6700###8",
#         "session": "70000100827678567a0###c82e10c85abf108fda6c36fdf5e1120f25d62631283423",
#         'password_content': taobao_code
#     }
#
#     try:
#         get_id_response = requests.post(url=get_id_url, data=get_id_data)
#         get_id_res_dict = json.loads(get_id_response.content.decode('utf-8'))
#         item_id = get_id_res_dict['data']['num_iid']
#
#     except KeyError as error_dict:
#         return get_id_res_dict['sub_msg']
#
#     # get_coupon
#     get_coupon_url = 'http://gateway.kouss.com/tbpub/privilegeGet'
#
#     get_coupon_data = {
#         "adzone_id": "1092###60",
#         "site_id": "6700###8",
#         "session": "70000100827678567a0###c82e10c85abf108fda6c36fdf5e1120f25d62631283423",
#         "item_id": item_id
#     }
#
#     try:
#         get_coupon_response = requests.post(url=get_coupon_url, data=get_coupon_data)
#         get_coupon_res_dict = json.loads(get_coupon_response.content.decode('utf-8'))
#
#         coupon_click_url = get_coupon_res_dict['result']['data']['coupon_click_url']
#         coupon_info = get_coupon_res_dict['result']['data']['coupon_info']
#
#     except KeyError as error_dict:
#         return get_coupon_res_dict['sub_msg']
#
#     # get_coupon_code
#     get_coupon_code_url = 'http://gateway.kouss.com/tbpub/tpwdCreate'
#
#     get_coupon_code_data = {
#         'user_id': "123",
#         'text': "长度大于5个字符",
#         'url': coupon_click_url,
#         #     'logo'="https://uland.taobao.com/"
#     }
#
#     try:
#         get_coupon_code_response = requests.post(url=get_coupon_code_url, data=get_coupon_code_data)
#         get_coupon_code_res_dict = json.loads(get_coupon_code_response.content.decode('utf-8'))
#         coupon_code = get_coupon_code_res_dict['data']['model']
#         return coupon_code
#
#     except KeyError as error_dict:
#         return get_coupon_code_res_dict['sub_msg']

@robot.handler
def theCoupon(message):
    taobao_code = message.content
    print(taobao_code)
    # coupon_code = theCoupon(taobao_code)
    #


    # get_item_id
    get_id_url = 'http://gateway.kouss.com/tbpub/tpwdConvert'

    get_id_data = {
        "adzone_id": "1092###60",
        "site_id": "6700###8",
        "session": "70000100827678567a0###c82e10c85abf108fda6c36fdf5e1120f25d62631283423",
        'password_content': taobao_code
    }

    try:
        get_id_response = requests.post(url=get_id_url, data=get_id_data)
        get_id_res_dict = json.loads(get_id_response.content.decode('utf-8'))
        item_id = get_id_res_dict['data']['num_iid']

    except KeyError as error_dict:
        return '1' + get_id_res_dict['sub_msg']

    # get_coupon
    get_coupon_url = 'http://gateway.kouss.com/tbpub/privilegeGet'

    get_coupon_data = {
        "adzone_id": "1092###60",
        "site_id": "6700###8",
        "session": "70000100827678567a0###c82e10c85abf108fda6c36fdf5e1120f25d62631283423",
        "item_id": item_id
    }

    try:
        get_coupon_response = requests.post(url=get_coupon_url, data=get_coupon_data)
        get_coupon_res_dict = json.loads(get_coupon_response.content.decode('utf-8'))

        coupon_click_url = get_coupon_res_dict['result']['data']['coupon_click_url']
        coupon_info = get_coupon_res_dict['result']['data']['coupon_info']

    except KeyError as error_dict:
        return '该商品无优惠券'

    # get_coupon_code
    get_coupon_code_url = 'http://gateway.kouss.com/tbpub/tpwdCreate'

    get_coupon_code_data = {
        'user_id': "123",
        'text': "长度大于5个字符",
        'url': coupon_click_url,
        #     'logo'="https://uland.taobao.com/"
    }

    try:
        time.sleep(1)
        get_coupon_code_response = requests.post(url=get_coupon_code_url, data=get_coupon_code_data)
        get_coupon_code_res_dict = json.loads(get_coupon_code_response.content.decode('utf-8'))
        coupon_code = get_coupon_code_res_dict['data']['model']
        name = re.findall(name_re_pattern, taobao_code)[0]

        reply_content = name + coupon_code + coupon_info
        return reply_content

    except KeyError as error_dict:
        return '该商品无优惠券'



robot.config['HOST'] = '0.0.0.0'

robot.config['PORT'] = 80

robot.run()