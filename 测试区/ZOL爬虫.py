import requests

#最后一位为页数
url = "https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_p17563_1_1_0_2.html"

data = requests.get(url).text
data = data[data.find('<div class="pro-intro">'):data.find('<div class="page-box">')].split('<div class="list-item clearfix" data-follow-id="')


# for i in range(len(data)):
#     print(data[i])

print(data[1])