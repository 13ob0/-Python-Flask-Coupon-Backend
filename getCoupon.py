import requests
import json
import time
import re

name_re_pattern = re.compile(r'(【.*?】)')

def getCoupon_fun(taobao_code):
    """
    :param taobao_code: 商品页面复制的淘口令
    :return: 商品对应优惠券的淘口令

    """

    # get_item_id
    get_id_url = 'http://gateway.kouss.com/tbpub/tpwdConvert'

    get_id_data = {
        "adzone_id": "1092###60",
        "site_id": "6700###8",
        "session": "###",
        'password_content': taobao_code
    }

    try:
        get_id_response = requests.post(url=get_id_url, data=get_id_data)
        get_id_res_dict = json.loads(get_id_response.content.decode('utf-8'))
        item_id = get_id_res_dict['data']['num_iid']

    except KeyError as error_dict:
        try:
            return get_id_res_dict['sub_msg']

        except KeyError as error_dict:
            print('佣金券')

    time.sleep(1)

    # get_coupon
    get_coupon_url = 'http://gateway.kouss.com/tbpub/privilegeGet'

    get_coupon_data = {
        "adzone_id": "1092###60",
        "site_id": "6700###8",
        "session": "7000010141456277b007a9d55a14274bdaa65bc51ca4168b0860f6aefec32cddc7f8e5f2631283423",
        "item_id": item_id
    }

    try:
        get_coupon_response = requests.post(url=get_coupon_url, data=get_coupon_data)
        get_coupon_res_dict = json.loads(get_coupon_response.content.decode('utf-8'))
        print(get_coupon_res_dict)

        coupon_click_url = get_coupon_res_dict['result']['data']['coupon_click_url']
        item_url = get_coupon_res_dict['result']['data']['item_url']
        coupon_info = get_coupon_res_dict['result']['data']['coupon_info']

    except KeyError as error_dict:
        try:
            return get_coupon_res_dict['sub_msg']

        except KeyError as error_dict:
            coupon_click_url = item_url
            print('佣金券')

    time.sleep(1)

    # get_coupon_code
    get_coupon_code_url = 'http://gateway.kouss.com/tbpub/tpwdCreate'

    get_coupon_code_data = {
        'user_id': "123",
        'text': "财源滚滚哟～",
        'url': coupon_click_url,
        #     'logo'="https://uland.taobao.com/"
    }

    try:
        get_coupon_code_response = requests.post(url=get_coupon_code_url, data=get_coupon_code_data)
        get_coupon_code_res_dict = json.loads(get_coupon_code_response.content.decode('utf-8'))
        coupon_code = get_coupon_code_res_dict['data']['model']
        try:
            return coupon_code + coupon_info
        except UnboundLocalError:
            name = re.findall(name_re_pattern, taobao_code)[0]
            return name + coupon_code

    except KeyError:
        return get_coupon_code_res_dict['sub_msg']