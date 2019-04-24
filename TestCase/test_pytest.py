

import  allure
@allure.feature("测试功能 一")
class Test_pytest:

    @allure.feature("测试功能 二")
    def test_demo2(self):
        a = 2
        b = 2
        assert a==b

    @allure.feature("测试功能 三")
    def test_demo3(self):

        a = 1
        b = 1
        assert a == b

