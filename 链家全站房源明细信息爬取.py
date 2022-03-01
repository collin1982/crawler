import random
from time import sleep
import pymongo
# 导入pyquery解析页面
import requests
from concurrent.futures import ThreadPoolExecutor
import pymysql
from pyquery import PyQuery as pq
from selenium import webdriver
# 让selenium规避被检测风险
from selenium.webdriver import ChromeOptions, ActionChains
# 导入显示等待参数
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def load_from_mongodb():
    # 从Mongodb中取值（详情页网址）
    for item in db['广州市各街道二手房源基本信息表'].find({},
                                           {'_id': 0, '房源链接': 1}):
        try:
            get_details(item['房源链接'])
            print('===================================开始获取下一条明细===================================')
        except:

            print('===================================出现反爬虫===================================')


def load_from_mysql():
    a = 0
    cursor = DB.cursor()  # 使用cursor()方法获取操作游标
    sql = "select 房源链接 from " + 'house_guangzhou_list_etl'
    cursor.execute(sql)
    info = cursor.fetchall()
    DB.commit()
    for i in info:

            try:
                print('===================================开始获取下一条明细===================================')
                get_details(i['房源链接'])
                a += 1
                print('这是第' + str(a) + '条')
                if a % 1000 == 0:
                    print('一千条了，休息一下')
                    sleep(600)
            except:
                print('======================反爬=======================')

    cursor.close()


def get_details(link):
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55',
        'Referer': 'https://gz.lianjia.com/',
        'Cookie': 'lianjia_uuid=53bc55d6-3c2e-447c-a4d3-58b287d298a2; _smt_uid=61ef54bf.13101ec5; UM_distinctid=17e8ee30d3f80f-005e5b449bb04f-5e181856-fa000-17e8ee30d40729; _ga=GA1.2.1044822858.1643074755; _gid=GA1.2.1805430482.1645000981; login_ucid=2000000232617799; lianjia_token=2.0012bcdd7376c0c7d80311f44290fa4a7c; lianjia_token_secure=2.0012bcdd7376c0c7d80311f44290fa4a7c; security_ticket=L2dfSGY7zHVCarHhoFTbBJ7ibLkCPGVqlmXB6MKKDv1dH4wOrhO7WTxlqPorlQa0ZhfdxPFDa7nMDC/eg8rHBs2IUHGX0ZOv3QfnGa84DULR5XLRpmd1HCBCdBFX6b73AgCMxvDXPTwJe5SpVqGQ9a96f17qynHxH6FMPOn8UEU=; _jzqckmp=1; _jzqc=1; _jzqy=1.1644994475.1645208958.1.jzqsr=baidu.-; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1645089184,1645109897,1645155969,1645208964; lianjia_ssid=701393f2-a22a-4b1c-a611-c2a90afa7be1; select_city=440100; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217e8ee3106cc4-06aaf2dee11ce2-5e181856-1024000-17e8ee3106d111%22%2C%22%24device_id%22%3A%2217e8ee3106cc4-06aaf2dee11ce2-5e181856-1024000-17e8ee3106d111%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _jzqa=1.4387942491122683000.1643074752.1645208958.1645216126.23; _jzqx=1.1645012154.1645216126.6.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/pazhou/; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1645216638; _jzqb=1.3.10.1645216126.1'

    }
    # bro.get(link)
    # html = bro.page_source
    responce = requests.get(url=link, headers=headers).text
    doc = pq(responce)
    house_details = {
        # 房源固定信息
        '小区名称': doc.find('.communityName .info').text(),
        '价格': (doc.find('.price-container .total').text() + doc.find('.price-container .unit').
               text()).replace('万', '0000').replace('.', ''),
        '每平方单价': doc.find('.text .unitPrice span').text(),
        '所属行政区': doc.find('.areaName .info a').eq(0).text(),
        '所在街道': doc.find('.areaName .info a').eq(1).text(),
        '房子ID': doc.find('.houseRecord .info').text().replace('举报', ''),
        '建筑时间': doc.find('.houseInfo .area .subInfo').text().split('/')[0].replace('建', ''),

        # 房源固定信息
        '房屋户型': doc.find('.base .content li').eq(0).text().replace('房屋户型', ''),
        '所在楼层': doc.find('.base .content li').eq(1).text().replace('所在楼层', ''),
        '建筑面积': doc.find('.base .content li').eq(2).text().replace('建筑面积', ''),
        '户型结构': doc.find('.base .content li').eq(3).text().replace('户型结构', ''),
        '套内面积': doc.find('.base .content li').eq(4).text().replace('套内面积', ''),
        '建筑类型': doc.find('.base .content li').eq(5).text().replace('建筑类型', ''),
        '房屋朝向': doc.find('.base .content li').eq(6).text().replace('房屋朝向', ''),
        '建筑结构': doc.find('.base .content li').eq(7).text().replace('建筑结构', ''),
        '装修情况': doc.find('.base .content li').eq(8).text().replace('装修情况', ''),
        '梯户比例': doc.find('.base .content li').eq(9).text().replace('梯户比例', ''),
        '配备电梯': doc.find('.base .content li').eq(10).text().replace('配备电梯', ''),

        # 房源交易信息
        '挂牌时间': doc.find('.transaction .content li').eq(0).find('span').eq(-1).text(),
        '交易权属': doc.find('.transaction .content li').eq(1).find('span').eq(-1).text(),
        '上次交易': doc.find('.transaction .content li').eq(2).find('span').eq(-1).text(),
        '房屋用途': doc.find('.transaction .content li').eq(3).find('span').eq(-1).text(),
        '房屋年限': doc.find('.transaction .content li').eq(4).find('span').eq(-1).text(),
        '产权所属': doc.find('.transaction .content li').eq(5).find('span').eq(-1).text(),
        '抵押信息': doc.find('.transaction .content li').eq(6).find('span').eq(-1).text(),
        '房本备件': doc.find('.transaction .content li').eq(7).find('span').eq(-1).text(),

        # 小区信息
        '核心卖点': doc.find('.introContent .baseattribute').eq(0).find('div').eq(1).text().replace('\n', ':'),
        '小区介绍': doc.find('.introContent .baseattribute').eq(1).find('div').eq(1).text().replace('\n', ':'),
        '周边配套': doc.find('.introContent .baseattribute').eq(2).find('div').eq(1).text().replace('\n', ':'),
        '交通出行': doc.find('.introContent .baseattribute').eq(3).find('div').eq(1).text().replace('\n', ':'),

        # 经纪人信息
        '经纪人': doc.find('.ke-agent-sj-top .ke-agent-sj-fr .ke-agent-sj-name').text(),
        '经纪公司': doc.find('.ke-agent-sj-top .ke-agent-sj-fr .ke-agent-sj-tag').text(),
        '经纪电话': doc.find('.ke-agent-sj-container .ke-agent-sj-sdk-f-0 .ke-agent-sj-phone').text().replace(' ',
                                                                                                          ''),

        # 链接
        '房屋照片': doc.find('.img .imgContainer img').attr('src'),
        '房源连接': link
    }
    print(house_details)
    save_to_mongo(house_details)


# 设置请求头


# 写入到mongodb
def save_to_mongo(result):
    try:
        # 新版本pymongo弃用了.insert方法改用.insert_one
        if db[MONGO_TABLE].insert_one(result):
            print('存储到MongoDB数据库成功')
    except Exception:
        print('存储到MongoDB数据库失败' + result)


# 驱动函数
def main():
    load_from_mysql()


if __name__ == '__main__':
    # 初始化MongoDB
    MONGO_URL = 'localhost'
    MONGO_DB = 'house'
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]

    # 初始化MySQL
    DB = pymysql.connect(host='localhost', port=3307, user='root', password='000000', database='house',
                         charset='utf8mb4',
                         # 把查询的返回集以字典形式保存
                         cursorclass=pymysql.cursors.DictCursor)

    MONGO_TABLE = '广州市各街道二手房源明细信息表1'

    # 设置浏览器参数对象
    option = ChromeOptions()
    # 关闭chrome弹出得密码保存框和网页通知询问
    prefs = {"": "", "credentials_enable_service": False, "profile.password_manager_enabled": False,
             "profile.default_content_setting_values": {'notifications': 2}}
    option.add_experimental_option("prefs", prefs)
    # 关闭自动化测试提醒
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    # 屏蔽webdriver特征
    option.add_argument("--disable-blink-features")
    option.add_argument("--disable-blink-features-AutomationControlled")
    # TODO 使用无头
    option.add_argument('--headless')
    # 初始化引擎参数
    # bro = webdriver.Chrome(options=option)
    # 反淘宝js检测手段  解决滑块验证码
    # bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    # })

    # 配置显示等待参数传入引擎对象和最大等待时间
    # wait = WebDriverWait(bro, 60)
    main()
    print('===========================当前列表房源明细全部爬取完成===========================')
    sleep(5)
    # bro.quit()
