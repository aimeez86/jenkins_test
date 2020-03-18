import pytest
import allure

@allure.feature('登录功能')
class TestLogin:
    @allure.story('test 1')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login1(self):
        with allure.step("判断断言1"):
            allure.attach('test1','断言成功', allure.attachment_type.TEXT)
            assert 1

    @allure.story('test 2')
    def test_login2(self):
        with allure.step("判断断言1"):
            allure.attach('test1', '断言失败')
            assert 0

