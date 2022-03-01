import datetime
import sys
from time import sleep
import pymysql
# 导入pyquery解析页面
from selenium import webdriver
# 让selenium规避被检测风险
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
# 导入显示等待参数
from selenium.webdriver.support.ui import WebDriverWait
# 捕获抓不到元素和请求超时的异常
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# 获取链家全国城市链接方法
def get_city():
    try:
        bro.get('https://www.lianjia.com/city/')
    except TimeoutException:
        print('====================连接超时，10秒后重试====================')
        try:
            sleep(10)
            bro.get('https://www.lianjia.com/city/')
        except TimeoutException:
             print('====================连接超时，请检查网络====================')
             bro.quit()
             sys.exit()
    try:
        items = bro.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div/ul/li')
    except NoSuchElementException:
        print('====================未能找到指定元素，可能遇到爬虫====================')
        bro.quit()
        sys.exit()
    # 网页基础取首字母板块
    for item in items:
        # 首字母板块基础取省份
        for i in item.find_elements(By.XPATH, './div[2]/div'):
            # 省份基础取城市
            for u in i.find_elements(By.XPATH, './ul/li'):
                city_info = {
                    # 这里一定是用find_element方法而不是find_elements
                    '省份': i.find_element(By.XPATH, './div').text,
                    # 这里一定是用find_element方法而不是find_elements
                    '城市': u.text,
                    '城市主键': u.find_element(By.XPATH, './a').get_attribute('href').replace('https://', '').replace(
                        '.lianjia.com/', ''),
                    '城市链接': u.find_element(By.XPATH, './a').get_attribute('href') + 'ershoufang/',
                    '当前信息获取时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    '当前城市下属区域是否已获取': '0'
                }
                print(city_info)
                save_to_mysql('城市中间表', city_info)


# 获取每个城市下的全部区域信息
def get_area():
    # 使用cursor()方法获取操作游标
    cursor = DB.cursor()
    sql = "select 省份,城市,城市链接 from " + '城市中间表'
    cursor.execute(sql)
    info = cursor.fetchall()
    DB.commit()
    for i in info:
        # 这里取出的每个i是元组类型,如果需要获取城市链接应当用i[2]来表示
        try:
            bro.get(i[2])
        except TimeoutException:
            print('====================连接超时，10秒后重试====================')
            try:
                sleep(10)
                bro.get(i[2])
            except TimeoutException:
                print('====================连接超时，请重新运行====================')
                bro.quit()
                sys.exit()
        try:
            items = bro.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/dl[2]/dd/div[1]/div[1]/a')
        except NoSuchElementException:
            print('====================未能找到指定元素，可能遇到爬虫====================')
            bro.quit()
            sys.exit()
        for item in items:
            area_info = {
                '省份': i[0],
                '城市': i[1],
                '区域': item.text,
                '区域主键': item.get_attribute('href').replace('https://', '').replace('.lianjia.com/ershoufang/',
                                                                                   '').replace('/', ''),
                '区域链接': item.get_attribute('href'),
                '当前信息获取时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                '当前区域下属街道是否已获取': '0'
            }
            print(area_info)
            save_to_mysql('区域中间表', area_info)
    cursor.close()


# 获取每个区域下的街道信息
def get_street():
    # 使用cursor()方法获取操作游标
    cursor = DB.cursor()
    # 只取未获取的区域来执行
    sql = "select 省份,城市,区域,区域主键,区域链接 from 区域中间表 WHERE 当前区域下属街道是否已获取 = 0"
    cursor.execute(sql)
    info = cursor.fetchall()
    DB.commit()
    for i in info:
        # 这里取出的每个i是元组类型,如果需要获取城市链接应当用i[2]来表示
        try:
            bro.get(i[4])
        except TimeoutException:
            print('====================连接超时，10秒后重试====================')
            try:
                sleep(10)
                bro.get(i[4])
            except TimeoutException:
                print('====================连接超时，请检查网络====================')
                bro.quit()
                sys.exit()
        # 定位到街道url TODO @href不能解析多个属性，需要用到get_attribute方法
        try:
            items = bro.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/dl[2]/dd/div[1]/div[2]/a')
        except NoSuchElementException:
            print('====================未能找到指定元素，可能遇到爬虫====================')
            bro.quit()
            # 未能解析到信息就把进程中止，防止出现把没有获取到的房源做了错误的标记
            sys.exit()
        for item in items:
            street_info = {
                '省份': i[0],
                '城市': i[1],
                '区域': i[2],
                '街道': item.text,
                '街道主键': item.get_attribute('href').replace('https://', '').replace('.lianjia.com/ershoufang/',
                                                                                   '').replace('/', ''),
                '街道链接': item.get_attribute('href'),
                '当前信息获取时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                '当前街道下属房源数量是否已获取': '0'
            }
            print(street_info)
            save_to_mysql('街道中间表', street_info)
        # # 当前信息已经解析出更细化的信息时，把标志字段重置为1
        sql_update = 'UPDATE 区域中间表 SET 当前区域下属街道是否已获取 = %s WHERE 区域主键 = %s'
        try:
            cursor.execute(sql_update, (1, i[3]))
            DB.commit()
        except pymysql.Error as e:
            DB.rollback()
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    cursor.close()


# 获取最小单位街道下的所以房源数量
def get_number():
    num = ''
    page = ''
    cursor = DB.cursor()
    # 只取未获取的街道来执行
    sql = "select 省份,城市,区域,街道,街道主键,街道链接 from 街道中间表 WHERE 当前街道下属房源数量是否已获取 = 0"
    cursor.execute(sql)
    info = cursor.fetchall()
    DB.commit()
    for i in info:
        # 这里取出的每个i是元组类型,如果需要获取城市链接应当用i[2]来表示
        try:
            bro.get(i[5])
        except TimeoutException:
            print('====================连接超时，10秒后重试====================')
            try:
                sleep(10)
                bro.get(i[5])
            except TimeoutException:
                print('====================连接超时，请重新运行====================')
                bro.quit()
                sys.exit()
        try:
            num = bro.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/h2/span').text
            if int(num) == 0:
                page = 0
            elif 0 < int(num) < 3000:
                if int(num) % 30 == 0:
                    page = (int(num) // 30)
                elif int(num) % 30 != 0:
                    page = (int(num) // 30 + 1)
            elif int(num) >= 3000:
                page = int(100)
        except NoSuchElementException:
            print('====================未能找到指定元素，可能遇到爬虫====================')
            # 未能解析到信息就把进程中止，防止出现把没有获取到的房源做了错误的标记
            bro.quit()
            sys.exit()
        number_info = {
            '省份': i[0],
            '城市': i[1],
            '区域': i[2],
            '街道': i[3],
            '街道主键': i[4],
            '街道链接': i[5],
            '当前街道房源数量': num,
            '当前街道房源页数': page,
            '当前信息获取时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            '当前街道房源是否全部已获取': '0'
        }
        print(number_info)
        save_to_mysql('房源数量中间表', number_info)
        # # 当前信息已经解析出更细化的信息时，把标志字段重置为1
        sql_update = 'UPDATE 街道中间表 SET 当前街道下属房源数量是否已获取 = %s WHERE 街道主键 = %s'
        try:
            cursor.execute(sql_update, (1, i[4]))
            DB.commit()
        except pymysql.Error as e:
            DB.rollback()
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    cursor.close()


# key是各个中间表名,result是各个中间表结果
def save_to_mysql(key, result):
    cursor = DB.cursor()
    table = str(key)
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
    finally:
        cursor.close()


def main():
    # 1.先获取全国所有城市信息
    print('===========================================开始获取链家全国所有城市信息===========================================')
    # get_city()
    print('===========================================链家全国所有城市信息获取完成===========================================\n')
    # 2.获取每个城市全部区域信息
    print('===========================================开始获取链家全国所有区域信息===========================================')
    # get_area()
    print('===========================================链家全国所有区域信息获取完成===========================================\n')
    # 3.获取每个区域全部街道信息
    print('===========================================开始获取链家全国所有街道信息===========================================')
    # get_street()
    print('===========================================链家全国所有街道信息获取完成===========================================\n')
    # 4.获取全部街道下所有房源数
    print('===========================================开始获取链家全国所有街道房源数量===========================================')
    # get_number()
    print('===========================================链家全国所有街道房源数量获取完成===========================================')


if __name__ == '__main__':
    # 初始化MySQL
    try:
        DB = pymysql.connect(host='localhost', port=3307, user='root', password='000000', database='house')
    except pymysql.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        print('========================请启动Mysql8========================')
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
    bro = webdriver.Chrome(options=option)
    # 反淘宝js检测手段  解决滑块验证码
    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
    # 配置显示等待参数传入引擎对象和最大等待时间
    wait = WebDriverWait(bro, 60)
    print('====================================开始获取全国所有房源信息====================================')
    main()
    sleep(3)
    bro.quit()
    DB.close()
