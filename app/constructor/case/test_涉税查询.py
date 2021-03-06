# -*- coding: utf-8 -*-

""" 测试工具自动生成的case """

import unittest
from app.controller.util.active import test_case_runner, test_case_parse
import logging

class 涉税查询(unittest.TestCase):
    """这是涉税查询接口测试用例"""

    def setUp(self):
        """ test setup function """

    def tearDown(self):
        """ test case tearDown function """

    @test_case_runner
    @test_case_parse
    def test_sscx(self, **kwargs):
        """ sscx 接口测试case """
        response, kwassert = kwargs.get('response'), kwargs.get('kwassert')
        logging.info(kwargs.get('response'))
        #logging.info(kwargs.get('exec_text'))
        #logging.info(kwargs.get('kwassert'))
        if kwargs.get('exec_text'):
            for item in kwargs.get('exec_text'):
                #logging.info(type(item))
                exec(item)
        else:
            assert_key, assert_value = kwassert.split('=')
            #logging.info(assert_value)
            self.assertEqual(response.get(assert_key), assert_value)
