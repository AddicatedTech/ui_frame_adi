# pytest入口
import pytest

# 运行测试用例，生成allure报告
pytest.main(['--alluredir=allure_report'])
# 查看allure报告，需要另外启动服务
# 用例重复执行机制
# pip install pytest-repeat
# pytest 要执行的用例名 --count=数字，重复执行该用例多少次  重复执行可以用来检测用例的稳定性
# 通过py执行的话写代码有所不同
# pytest.main(['-m 用例标签名'，'--reruns 3','--reruns-delay 2']) 失败重复执行3次，每次间隔两秒
pytest.main(['-m 用例标签名','--count=3'])

#用例失败重复执行机制
# pip install pytest-rerunfailures
# pytest 要执行的用例名 --reruns 3 用例执行失败的时候重新执行的次数 --reruns

# 如果要进行无界面的运行，跑测试流程。需要配置无头参数，使用无头浏览器
# 1 设置为无头浏览器，无头浏览器，即不显示页面 浏览器在后台执行，在执行过程中不会显示浏览器的页面
# 2 目标服务器上要装好web自动执行的环境， Python环境+ 要使用到的第三方库