from Common import Request,Assert,read_excel,Login
import allure
import pytest
idlist = []
request = Request.Request
assertions = Assert.Assertions

excel_list = read_excel.read_excel_list('../doucument/优惠券.xlsx')
length = len(excel_list)
for i in range():
    idlist.append(excel_list[i].pop())


url = 'http://192.168.1.137:8080/'
head = {}
item_id = 0


@allure.feature('优惠券模块')
class Test_yhq:

    @allure.story('查询优惠券列表')
    def test_yhq_get_list(self):
        global head

        head = Login.Login().get_token()
        get_req_list_yhq = request.get_request(url=url + 'coupon/list', params={'pageNum': 1, 'pageSize': 10}, headers=head)
        yhq_json = get_req_list_yhq.json()
        json_yhq = yhq_json['data']
        yhq_list = json_yhq['list']
        item_id





