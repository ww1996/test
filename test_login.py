import pytest
from Common import Shell

if __name__ == '__main__':
    shell = Shell.Shell()
    pytest.main(['-s', '-q', '--alluredir', './Report/xml/', './TestCase'])

    cmd = "allure generate ./Report/xml/ -o ./Report/html/ --clean"
    try:
        shell.invoke(cmd)
    except Exception:
        print('XXX')















from Common import Request, Assert
import allure


request = Request.Request()

assertion = Assert.Assertions()

@allure.feature("登录功能")
class Test_login:

    @allure.story("登录")
    def test_login(self):


        login_resp = request.post_request(url='http://192.168.1.137:8080/admin/login',
                                            json={"username": "admin", "password": "123456"})


        resp_text = login_resp.text
        print(type(resp_text))

        resp_dict = login_resp.json()
        print(type(resp_dict))

        assertion.assert_code(login_resp.status_code,403)
        assertion.assert_in_text(resp_dict['message'],'成功')