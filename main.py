from reg_time_spider import *

url = 'https://data.stats.gov.cn/easyquery.htm?cn=E0103'
params = {}
headers = {'User-Agent': 'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Geko/20091201 Firefox/3.5.6'}
params['m'] = 'QueryData'
params['dbcode'] = 'fsnd'
params['rowcode'] = 'zb'
params['colcode'] = 'sj'
params['k1'] = str(get_time())

# 读取和写入

requests.packages.urllib3.disable_warnings()
print('农、林、牧、渔业总产值及指数.xlsx')
start_get('A0D05', 'result/农、林、牧、渔业总产值及指数.xlsx', url=url, params=params, headers=headers)
print('农用塑料薄膜使用量.xlsx')
start_get('A0D0L', 'result/农用塑料薄膜使用量.xlsx', url=url, params=params, headers=headers)
print('主要农业机械年末拥有量.xlsx')
start_get('A0D0G', 'result/主要农业机械年末拥有量.xlsx', url=url, params=params, headers=headers)
print('有效灌溉面积、农用化肥施用量、农村水电站及用电量.xlsx')
start_get('A0D0H', 'result/有效灌溉面积、农用化肥施用量、农村水电站及用电量.xlsx', url=url, params=params, headers=headers)
print('农林牧渔业增加值.xlsx')
start_get('A0D06', 'result/农林牧渔业增加值.xlsx', url=url, params=params, headers=headers)
print('农村水电建设和发电量.xlsx')
start_get('A0D0I', 'result/农村水电建设和发电量.xlsx', url=url, params=params, headers=headers)
print('全体及分城乡居民收支基本情况（2013-）.xlsx')
start_get('A0A00', 'result/others/全体及分城乡居民收支基本情况（2013-）.xlsx', url=url, params=params, headers=headers)
print('每万人口卫生技术人员数.xlsx')
start_get('A0O03', 'result/others/每万人口卫生技术人员数.xlsx', url=url, params=params, headers=headers)
print('互联网主要指标发展情况.xlsx')
start_get('A0G0J', 'result/others/互联网主要指标发展情况.xlsx', url=url, params=params, headers=headers)
print('城乡居民社会养老保险情况.xlsx')
start_get('A0S0B', 'result/others/城乡居民社会养老保险情况.xlsx', url=url, params=params, headers=headers)
print('农产品生产价格指数(上年=100).xlsx')
start_get('A0907', 'result/others/农产品生产价格指数(上年=100).xlsx', url=url, params=params, headers=headers)