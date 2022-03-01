import datetime
import sys
from time import sleep

import pymysql
import requests
# 导入pyquery解析页面
from pyquery import PyQuery as pq
from selenium import webdriver
# 让selenium规避被检测风险
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ChromeOptions
# 导入显示等待参数
from selenium.webdriver.common.by import By


def request(province_1, city_1, area_1, link_1):
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55',
        'Referer': 'https://lianjia.com/',
        # 'Cookie': 'lianjia_uuid=53bc55d6-3c2e-447c-a4d3-58b287d298a2; _smt_uid=61ef54bf.13101ec5; '
        #           'UM_distinctid=17e8ee30d3f80f-005e5b449bb04f-5e181856-fa000-17e8ee30d40729; '
        #           '_ga=GA1.2.1044822858.1643074755; _gid=GA1.2.1805430482.1645000981; login_ucid=2000000232617799; '
        #           'lianjia_token=2.0012bcdd7376c0c7d80311f44290fa4a7c; '
        #           'lianjia_token_secure=2.0012bcdd7376c0c7d80311f44290fa4a7c; '
        #           'security_ticket=L2dfSGY7zHVCarHhoFTbBJ7ibLkCPGVqlmXB6MKKDv1dH4wOrhO7WTxlqPorlQa0ZhfdxPFDa7nMDC'
        #           '/eg8rHBs2IUHGX0ZOv3QfnGa84DULR5XLRpmd1HCBCdBFX6b73AgCMxvDXPTwJe5SpVqGQ9a96f17qynHxH6FMPOn8UEU=; '
        #           '_jzqckmp=1; _jzqc=1; _jzqy=1.1644994475.1645208958.1.jzqsr=baidu.-; '
        #           'Hm_lvt_9152f8221cb6243a53c83b956842be8a=1645089184,1645109897,1645155969,1645208964; '
        #           'lianjia_ssid=701393f2-a22a-4b1c-a611-c2a90afa7be1; select_city=440100; '
        #           'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217e8ee3106cc4-06aaf2dee11ce2-5e181856-1024000'
        #           '-17e8ee3106d111%22%2C%22%24device_id%22%3A%2217e8ee3106cc4-06aaf2dee11ce2-5e181856-1024000'
        #           '-17e8ee3106d111%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5'
        #           '%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22'
        #           '%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6'
        #           '%89%93%E5%BC%80%22%7D%7D; _jzqa=1.4387942491122683000.1643074752.1645208958.1645216126.23; '
        #           '_jzqx=1.1645012154.1645216126.6.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/.jzqsr=gz%2Elianjia'
        #           '%2Ecom|jzqct=/ershoufang/pazhou/; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1645216638; '
        #           '_jzqb=1.3.10.1645216126.1 '

    }
    # 请求经过判断处理后的url
    try:
        response = requests.get(url=link_1, headers=headers, timeout=6)
    except requests.exceptions.RequestException as e:
        print('================================网络不通，重试一次===========================')
        try:
            sleep(10)
            response = requests.get(url=link_1, headers=headers, timeout=60)
        except requests.exceptions.RequestException as e:
            print('================================网络不通，请重新运行===========================')
            sys.exit()
    #     TODO 再做一个监测反爬虫的
    # 响应码是200而不是'200'
    if '封禁原因' not in response.text:
        analysis(province_1, city_1, area_1, response)
    else:
        print('================================存在反爬虫，请重新运行===========================')
        bro.quit()
        sys.exit()


def analysis(province_2, city_2, area_2, response):
    # TODO 选择request或者browser方法还要对应选择这里

    # request
    doc = pq(response.text)

    # browser
    # doc = pq(response)

    # items = doc('.sellListContent li').items
    # TODO 改用下面写法指定第一个元素可以避免找到小于30套房源的广告信息  find是找子孙 children是找子节点
    items = doc.find('.sellListContent').eq(0).children('li').items()
    for item in items:
        # 因为这个六个属性都在一个元素标签下，需要经过切分才能细分属性，但是房源元素不统一需要做一个判断
        # huxing = ''
        # mianzhi = ''
        # chaoxiang = ''
        # zhuangxiu = ''
        # loucheng = ''
        # louling = ''
        # jianzhuleixing = ''
        # TODO 去掉车位信息
        chewei = item.find('.houseInfo').text().replace(' ', '').split('|')[0]
        # 判断class=houseInfo下面的标签个数是否等于7，如果不等于7直接取值到字典会造成数据混乱，所以当前
        if len(item.find('.houseInfo').text().split('|')) == 7:
            huxing = item.find('.houseInfo').text().replace(' ', '').split('|')[0]
            mianzhi = item.find('.houseInfo').text().replace(' ', '').split('|')[1]
            chaoxiang = item.find('.houseInfo').text().replace(' ', '').split('|')[2]
            zhuangxiu = item.find('.houseInfo').text().replace(' ', '').split('|')[3]
            loucheng = item.find('.houseInfo').text().replace(' ', '').split('|')[4]
            louling = item.find('.houseInfo').text().replace(' ', '').split('|')[5]
            jianzhuleixing = item.find('.houseInfo').text().replace(' ', '').split('|')[6]
        #     TODO 目前分出6个标签的房源和7个标签的房源 后续根据数据样本进一步细化，提高数据质量
        elif len(item.find('.houseInfo').text().split('|')) == 6:
            huxing = item.find('.houseInfo').text().replace(' ', '').split('|')[0]
            mianzhi = item.find('.houseInfo').text().replace(' ', '').split('|')[1]
            chaoxiang = item.find('.houseInfo').text().replace(' ', '').split('|')[2]
            zhuangxiu = item.find('.houseInfo').text().replace(' ', '').split('|')[3]
            loucheng = item.find('.houseInfo').text().replace(' ', '').split('|')[4]
            louling = '暂无数据'
            jianzhuleixing = jianzhuleixing = item.find('.houseInfo').text().replace(' ', '').split('|')[-1]
        else:
            # 房源信息的7个属性均设为暂无数据，虽然缺失了一部分数据，但提高了整体数据完整度
            huxing = mianzhi = chaoxiang = zhuangxiu = loucheng = louling = jianzhuleixing = '暂无数据'

        house_info = {
            '房源主键': item.find('.title a').attr('href').replace('https://', '').replace('.lianjia.com/ershoufang/',
                                                                                       '').replace('.html', ''),
            '省份': province_2,
            '城市': city_2,
            '所属行政区': area_2,
            '所在街道': item.find('.positionInfo a').eq(-1).text(),
            '小区名称': item.find('.positionInfo a').eq(0).text(),
            '价格': item.find('.totalPrice').text().replace('万', '0000').replace('参考价: ', '').replace('.', '').replace(
                ' ', ''),
            '建筑面积': mianzhi,
            '每平方单价': item.find('.unitPrice span').text().replace(',', ''),
            '户型': huxing,
            '装修情况': zhuangxiu,
            '房屋朝向': chaoxiang,
            '楼层': loucheng,
            '楼龄': louling,
            '建筑类型': jianzhuleixing,
            '发布时间': item.find('.followInfo').text().replace(' ', '').split('/')[-1].replace('发布', ''),
            '关注人数': item.find('.followInfo').text().replace(' ', '').split('/')[0],
            '房源标签': item.find('.tag span').text() or '暂无数据',
            # 作为去重和表连接的字段
            '房源链接': item.find('.title a').attr('href'),
            # 页面的src属性并非是真实的图片url，真正的url在属性data-original里
            '房源图片链接': item.find('.noresultRecommend .lj-lazy').attr('data-original'),
            '当前信息时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            '是否已获取该房源明细信息': '0'

        }
        if house_info['小区名称'] != '' and chewei != '车位':
            print(house_info)
            save_to_mysql('链家全国二手房基本信息表', house_info)


# selenium方式不容易引起反爬
def browser(province_3, city_3, area_3, link_2):
    try:
        bro.get(link_2)
        try:
            bro.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/h2/span')
        except NoSuchElementException:
            print('====================未能找到指定元素，可能遇到爬虫====================')
            sys.exit()
        response = bro.page_source
        analysis(province_3, city_3, area_3, response)
    except TimeoutException:
        print('====================连接超时，请检查网络，30秒后重试====================')
        bro.quit()
        sys.exit()


def load_from_mysql():
    cursor = DB.cursor()
    # 通过SQL语句获取指定区域的信息
    sql = " select 省份,城市,区域,街道,街道主键,街道链接,当前街道房源数量,当前街道房源页数 from 房源数量中间表 WHERE 当前街道房源是否全部已获取 = 0 " \
          "AND 当前街道房源数量 > 0"
    # 只取未获取的街道来执行
    cursor.execute(sql)
    info = cursor.fetchall()
    DB.commit()
    for i in info:
        print('============================' + i[0] + '省（直辖市）' + i[1] + '市' + i[2] + '(县)下属' + i[3] + '共找到' + i[
            6] + '套二手房源============================\n')
        for u in range(1, int(i[7]) + 1):
            # request 速度快，容易反爬
                request(i[0], i[1], i[2], i[5] + 'pg' + str(u))
            # browser 速度慢，不容易反爬
            # browser(i[0], i[1], i[2], i[5] + 'pg' + str(u))
        # 一个城市所有页翻完才能去标记
        mark(i[4])
    cursor.close()


def mark(symbol):
    cursor = DB.cursor()
    sql_update = 'UPDATE 房源数量中间表 SET 当前街道房源是否全部已获取 = %s WHERE 街道主键 = %s'
    try:
        cursor.execute(sql_update, (1, symbol))
        DB.commit()
    except pymysql.Error as e:
        DB.rollback()
    cursor.close()


# 存储到MySQL数据库,建好表
def save_to_mysql(key, result):
    cursor = DB.cursor()
    table = key
    keys = ', '.join(result.keys())
    values = ', '.join(['%s'] * len(result))

    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                         values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in result])
    sql += update
    try:
        if cursor.execute(sql, tuple(result.values()) * 2):
            print('存储到MySQL数据库成功')
            DB.commit()
    except pymysql.Error as e:
        DB.rollback()
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


# 驱动函数
def main():
    load_from_mysql()


if __name__ == '__main__':
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
    # TODO 使用无头 提高速度
    option.add_argument('--headless')
    bro = webdriver.Chrome(options=option)
    # 隐藏selenium特性
    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
    print('================================================开始爬取================================================')
    # 初始化MySQL
    try:
        DB = pymysql.connect(host='localhost', port=3307, user='root', password='000000', database='house')
    except pymysql.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    main()
    sleep(5)
    print('==========================================爬取完成，释放资源================================================')
    bro.quit()
    DB.close()
