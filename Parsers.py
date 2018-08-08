#!/usr/bin/env python
# load Excel workbook, iterate over sheets in book
# return a count of specified item
import re

class Parsers(object):
    
    def find_words_with_find(self, search_string):
        print('find_words_with_find')
        print('search_string is: %s' % (search_string, ))
        find_words = []
        position = 0
        if ((search_string in (None, '')) or (len(search_string.strip()) == 0)):
            return(find_words)
        search_string = search_string.strip()
        while (position != -1):
            if (position > 0):
                find_words.append(search_string[:position])
            search_string = search_string[position:].strip()
            position = search_string.find(' ')
        find_words.append(search_string)
        return(find_words)
    
    def find_words_with_split(self, search_string):
        print('find_words_with_split')
        print('search_string is: %s' % (search_string, ))
        find_words = []
        if ((search_string in (None, '')) or (len(search_string.strip()) == 0)):
            return(find_words)
        search_string = search_string.strip()
        split_list = search_string.split(' ')
        for split_item in split_list:
            if (split_item not in (None, '')):
                find_words.append(split_item) 
        print(find_words)
        return(find_words)
    
    def find_words_with_whitespace_regex(self, search_string):
        print('find_words_with_whitespace_regex')
        print('search_string is: %s' % (search_string, ))
        find_words = []
        if ((search_string in (None, '')) or (len(search_string.strip()) == 0)):
            return(find_words)
        search_pattern = re.compile(r'\s+')
        split_search = search_pattern.search(search_string)
        while (split_search is not None):
            if (split_search.span()[0] != 0):
                find_words.append(search_string[:split_search.span()[0]])
            search_string = search_string[split_search.span()[1]:]
            split_search = search_pattern.search(search_string)
        if (len(search_string) > 0):
            find_words.append(search_string)
        return(find_words)
    
    def find_words_with_word_regex(self, search_string):
        print('find_words_with_word_regex')
        print('search_string is: %s' % (search_string, ))
        find_words = []
        if ((search_string in (None, '')) or (len(search_string.strip()) == 0)):
            return(find_words)
        search_pattern = re.compile(r'[\w:]+')
        split_search = search_pattern.search(search_string)
        while (split_search is not None):
            find_words.append(search_string[split_search.span()[0]:split_search.span()[1]])
            search_string = search_string[split_search.span()[1]:]
            split_search = search_pattern.search(search_string)
        return(find_words)
        
    def find_words_with_word_findall_regex(self, search_string):
        print('find_words_with_word_findall_regex')
        print('search_string is: %s' % (search_string, ))
        find_words = []
        if ((search_string in (None, '')) or (len(search_string.strip()) == 0)):
            return(find_words)
        search_pattern = re.compile(r'[\w:]+')
        find_words = search_pattern.findall(search_string)
        return(find_words)
    