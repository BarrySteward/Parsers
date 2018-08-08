#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright � 2014-2017 Intrexon, Inc. All rights reserved.

import unittest
import datetime
import random
from Parsers import Parsers
import re


class ParsersTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
        """
        Negative Testing First.
        Boundary conditions.
        Postive test second.
        Ideal test methods have minimum code so as to avoid
        bugs in the test code itself.
        Ideal is test value inputs paired with expected results as input pairs, i.e.
        ((1, 1), (365, 31))
        then assert the test result.
        """ 

    #@unittest.skip('test commented out')
    def test01_find_words_with_find(self):
        """ Simple test.
            Initialization
        """ 
        parsers = Parsers()
        # parsers.init_attrs()
        now = datetime.datetime.now()
        date1 = now.strftime("%a %b %m %d %I:%M:%S EST %Y")
        date2 = now.strftime("%a  %b  %m  %d  %I:%M:%S  EST  %Y")
        splits = now.strftime("%a %b %m %d %I:%M:%S EST %Y").split(' ')
        date3 = ""
        for split_item in splits:
            date3 += "%s%s" % (split_item, ' ' * random.randint(1, 10))
        expected_negative_result = []
        for search_string in (None, ''):
            print("Negative Testing, find_words_with_find: expected_negative_result = %s, search_string = %s" %
                        (expected_negative_result, search_string))
            test_result = parsers.find_words_with_find(search_string)
            self.assertTrue(test_result == expected_negative_result,
                            'test failed, test_result of %s does not equal expected_negative_result of %s' %
                            (test_result, expected_negative_result))
            print(test_result)
            print('passed')
        
        expected_positive_result = date1.split(' ')
        for search_string in (date1, date2, date3):
            print("Positive Testing, find_words_with_find: expected_positive_result = %s, search_string = %s" %
                        (expected_positive_result, search_string))
            test_result = parsers.find_words_with_find(search_string)
            self.assertTrue(test_result == expected_positive_result,
                            'test failed, test_result of %s does not equal expected_positive_result of %s' %
                                (test_result, expected_positive_result))
            print(test_result)
        print('passed')
    
    #@unittest.skip('test commented out')    
    def test02_find_words_with_split(self):
        """ Simple test.
            Initialization
        """ 
        parsers = Parsers()
        now = datetime.datetime.now()
        date1 = now.strftime("%a %b %m %d %I:%M:%S EST %Y")
        date2 = now.strftime("%a  %b  %m  %d  %I:%M:%S  EST  %Y")
        splits = now.strftime("%a %b %m %d %I:%M:%S EST %Y").split(' ')
        date3 = ""
        for split_item in splits:
            date3 += "%s%s" % (split_item, ' ' * random.randint(1, 10))
        expected_negative_result = []
        for search_string in (None, ''):
            print("Negative Testing, find_words_with_split: expected_negative_result = %s, search_string = %s" %
                        (expected_negative_result, search_string))
            test_result = parsers.find_words_with_split(search_string)
            self.assertTrue(test_result == expected_negative_result,
                            'test failed, test_result of %s does not equal expected_negative_result of %s' %
                            (test_result, expected_negative_result))
            print(test_result)
            print('passed')
        
        expected_positive_result = date1.split(' ')
        for search_string in (date1, date2, date3):
            print("Positive Testing, find_words_with_split: expected_positive_result = %s, search_string = %s" %
                        (expected_positive_result, search_string))
            test_result = parsers.find_words_with_split(search_string)
            self.assertTrue(test_result == expected_positive_result,
                            'test failed, test_result of %s does not equal expected_positive_result of %s' %
                                (test_result, expected_positive_result))
            print(test_result)
        print('passed')
        
    #@unittest.skip('test commented out')
    def test03_find_words_with_whitespace_regex(self):
        """ Simple test.
            Initialization
        """ 
        parsers = Parsers()
        now = datetime.datetime.now()
        date1 = now.strftime("%a %b %m %d %I:%M:%S EST %Y")
        date2 = now.strftime("%a  %b  %m  %d  %I:%M:%S  EST  %Y")
        splits = now.strftime("%a %b %m %d %I:%M:%S EST %Y").split(' ')
        date3 = ""
        for split_item in splits:
            date3 += "%s%s" % (split_item, ' ' * random.randint(1, 10))
        expected_negative_result = []
        for search_string in (None, ''):
            print("Negative Testing, find_words_with_whitespace_regex: expected_negative_result = %s, search_string = %s" %
                        (expected_negative_result, search_string))
            test_result = parsers.find_words_with_whitespace_regex(search_string)
            self.assertTrue(test_result == expected_negative_result,
                            'test failed, test_result of %s does not equal expected_negative_result of %s' %
                            (test_result, expected_negative_result))
            print(test_result)
            print('passed')
        
        expected_positive_result = date1.split(' ')
        for search_string in (date1, date2, date3):
            print("Positive Testing, find_words_with_whitespace_regex: expected_positive_result = %s, search_string = %s" %
                        (expected_positive_result, search_string))
            test_result = parsers.find_words_with_whitespace_regex(search_string)
            self.assertTrue(test_result == expected_positive_result,
                            'test failed, test_result of %s does not equal expected_positive_result of %s' %
                                (test_result, expected_positive_result))
            print(test_result)
        print('passed')
        
    #@unittest.skip('test commented out')
    def test04_find_words_with_word_regex(self):
        """ Simple test.
            Initialization
        """ 
        parsers = Parsers()
        now = datetime.datetime.now()
        date1 = now.strftime("%a %b %m %d %I:%M:%S EST %Y")
        date2 = now.strftime("%a  %b  %m  %d  %I:%M:%S  EST  %Y")
        splits = now.strftime("%a %b %m %d %I:%M:%S EST %Y").split(' ')
        date3 = ""
        for split_item in splits:
            date3 += "%s%s" % (split_item, ' ' * random.randint(1, 10))
        expected_negative_result = []
        for search_string in (None, ''):
            print("Negative Testing, find_words_with_word_regex: expected_negative_result = %s, search_string = %s" %
                        (expected_negative_result, search_string))
            test_result = parsers.find_words_with_word_regex(search_string)
            self.assertTrue(test_result == expected_negative_result,
                            'test failed, test_result of %s does not equal expected_negative_result of %s' %
                            (test_result, expected_negative_result))
            print(test_result)
            print('passed')
        
        expected_positive_result = date1.split(' ')
        for search_string in (date1, date2, date3):
            print("Positive Testing, find_words_with_word_regex: expected_positive_result = %s, search_string = %s" %
                        (expected_positive_result, search_string))
            test_result = parsers.find_words_with_word_regex(search_string)
            self.assertTrue(test_result == expected_positive_result,
                            'test failed, test_result of %s does not equal expected_positive_result of %s' %
                                (test_result, expected_positive_result))
            print(test_result)
        print('passed')
        
    #@unittest.skip('test commented out')
    def test05_find_words_with_word_findall_regex(self):
        """ Simple test.
            Initialization
        """ 
        parsers = Parsers()
        now = datetime.datetime.now()
        date1 = now.strftime("%a %b %m %d %I:%M:%S EST %Y")
        date2 = now.strftime("%a  %b  %m  %d  %I:%M:%S  EST  %Y")
        splits = now.strftime("%a %b %m %d %I:%M:%S EST %Y").split(' ')
        date3 = ""
        for split_item in splits:
            date3 += "%s%s" % (split_item, ' ' * random.randint(1, 10))
        expected_negative_result = []
        for search_string in (None, ''):
            print("Negative Testing, find_words_with_word_findall_regex: expected_negative_result = %s, search_string = %s" %
                        (expected_negative_result, search_string))
            test_result = parsers.find_words_with_word_findall_regex(search_string)
            self.assertTrue(test_result == expected_negative_result,
                            'test failed, test_result of %s does not equal expected_negative_result of %s' %
                            (test_result, expected_negative_result))
            print(test_result)
            print('passed')
        
        expected_positive_result = date1.split(' ')
        for search_string in (date1, date2, date3):
            print("Positive Testing, find_words_with_word_findall_regex: expected_positive_result = %s, search_string = %s" %
                        (expected_positive_result, search_string))
            test_result = parsers.find_words_with_word_findall_regex(search_string)
            self.assertTrue(test_result == expected_positive_result,
                            'test failed, test_result of %s does not equal expected_positive_result of %s' %
                                (test_result, expected_positive_result))
            print(test_result)
        print('passed')
    