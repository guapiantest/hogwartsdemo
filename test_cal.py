import pytest
import os
from pythoncode.calculator import Calculator
import allure


class  TestCal:
    def setup_class(self):
        self.cal=Calculator
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @allure.feature('加法测试')
    @pytest.mark.parametrize('m,n,expect',[(1,2,3),(-1,-2,-3),(10000,30000,40000)])
    def test_add(self,m,n,expect):
        assert self.cal.add(self,m,n) == expect


    @allure.feature('减法测试')
    @pytest.mark.parametrize('m,n,expect',[(9,1,8),(9,9,0),(9,10,-1),(-1,-1,0)])
    def test_sub(self,m,n,expect):
        assert self.cal.sub(self,m,n)==expect


    @allure.feature('乘法测试')
    @pytest.mark.parametrize('m,n,expect',[(1,2,2),(0,-2,0),(9,100,900)])
    def test_mul(self,m,n,expect):
        assert self.cal.mul(self,m,n)==expect


    @allure.feature('除法测试--除数不为0')
    @pytest.mark.parametrize('m,n,expect',[(1,2,0.5),(4.5,2,2.25),(8,1,8)])
    def test_div(self,m,n,expect):
        assert self.cal.div(self,m,n)==expect

    @allure.feature('除法测试--除数为0')
    def test_div2(self):
       with pytest.raises(ZeroDivisionError):
            assert  self.cal.div(self,1,0)



if __name__=='__main__':
    pytest.main()

    # pytest.main(['-s', '-q','--alluredir','./report'])
# os.system('allure generate ./result -o ./report --clean')
# os.system('allure open -h 127.0.0.1 -p 8883 ./report')







