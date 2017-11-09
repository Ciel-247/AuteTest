# -*-coding:utf-8*-

"""
@ Version : v0.1
@ Author  : xzl
@ File    : run.py
@ Project : AuteTest
@ Create Time: 2017-10-25 15:54
@python version : 3.x
"""

import time
import sys
import unittest
import logging
import logging.config
from app.controller.util import BSTestRunner
from HTMLTestRunner import HTMLTestRunner
from app.config import config
from app.constructor.create_case import CreateCase
from app.constructor.use_case_operation import  UseCaseOperation

logging.config.fileConfig("./app/config/log.conf")
logger = logging.getLogger("test")

start_time = time.time()
# create case_files ,将excle 中的用例生成 unittist 用例文件
case_path = CreateCase.create_unittest_files().get('final_case_path')
report_path = config.REPORT_PATH

def load_tests(loader,tests,pattern):
    #logging.info("load_tests 开始...")
    start_time = time.time()
    # create case_files ,将excle 中的用例生成 unittist 用例文件
    #case_path=CreateCase.create_unittest_files().get('final_case_path')
    #report_path= config.REPORT_PATH

    logging.info(start_time)
    logging.info(CreateCase.create_unittest_files().get('msg')+",case_path:"+case_path)

    #生成测试 suite
    suite = unittest.defaultTestLoader.discover(case_path,pattern='test_*.py')
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    #logging.info(suite)
    #选择不同的测试报告模板
    if config.SWITCH:
        logging.info("default report")
        with open(report_path, 'wb') as files:
            runner = BSTestRunner.BSTestRunner(
                files,
                title='TestReport_{0}'.format(int(time.time())),
                description=u'自动化生成用例测试'
            )
            runner.run(suite)
    else:
        logging.info("404....")

        #with open(report_path, 'wb') as files:
         #   runner = HTMLTestRunner(stream=files,
         #                          title='Guest Manage System Interface Test Report',
         #                         description='Implementation Example with: ')
        #    runner.run(discover)


if __name__ == '__main__':
    try:
        #logging.info(sys.getdefaultencoding())
        unittest.main()##[lesq??]这里用了unittest.main()是会直接搜索本模块中以"test"命名开头的测试方法吗？还是运行46行的runner.run(suite)?
    except TypeError:
        UseCaseOperation.clear_test_data()
