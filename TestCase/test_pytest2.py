import allure

@allure.feature("测试功能 二")
class Test_py2:

    @allure.story("测试小功能 二 1")
    def test_demo3(self):
        a = 1
        b = 1
        assert a == b

    @allure.story("测试小功能 三  2")
    def test_demo4(self):
        a = 2
        b = 2
        assert a == b