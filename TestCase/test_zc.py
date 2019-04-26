from Common import Request, Assert, read_excel, Tools
import allure
import pytest
json_ ='臭弟弟'
request = Request.Request()
assertion = Assert.Assertions()
iphone = Tools.phone_num()
username = Tools.random_str_abc(3) + Tools.random_123(3)

# excel_list = read_excel.read_excel_list('../document/注册.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:1811/'


@allure.feature('用户模块')
class Test_zc:

    @allure.story('注册')
    # @pytest.mark.parametrize('iphone,pwd,repwd,username,msg',excel_list,ids=idsList)
    def test_zc(self):
        json = {"phone": iphone, "pwd": "123456z", "rePwd": "123456z", "userName": username}
        zc_resp = request.post_request(url=url + 'user/signup', json=json)
        resp_json = zc_resp.json()
        assertion.assert_code(zc_resp.status_code, 200)
        assertion.assert_in_text(resp_json['respBase'], '成功')
    # @allure.story('登录')
    # def test_login(self):
    #     jsons = {"pwd": "123456z", "userName": "zqw1234"}
    #     dl_resp = request.post_request(url=url + 'user/login', json=jsons)
    #     resp_json = dl_resp.json()
    #     assertion.assert_code(dl_resp.status_code, 200)
    #     assertion.assert_text(resp_json['respDesc'], '成功')
    @allure.story('登录')
    def test_denglu(self):
        post_request = request.post_request(url=url + '/user/login', json={"pwd": "123456z",
            "userName": "zqw1234"})
        json = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(json['respDesc'], '成功')
    @allure.story('修改')
    def test_xiugai(self):
        _response = request.post_request(url=url + '/user/changepwd',
                                            json={"newPwd": "123456a", "oldPwd": "123456z", "reNewPwd": "123456a",
                                                  "userName": "zqw1234"})
        json_ = _response.json()
        assertion.assert_code(_response.status_code, 200)
        assertion.assert_in_text(json_['respDesc'], '成功')



