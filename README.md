# -Python-Flask-Coupon-Backend

## 程序结构

* 基于Flask的后端服务器
* 基于原生语言的微信小程序

### 后端服务器

* run: Flask入口程序
* coupon_flaskapp: Flask主程序
* Coupon_werobot: 对接公众号的后端程序，根据淘口令查询优惠券并转换为优惠券口令
* getCoupon: 对接小程序的后端程序，根据淘口令查询优惠券并转换为优惠券口令