import re
import requests
from ...dev import x
from learntools.core import *
import os
import subprocess

class Question1(CodingProblem):

    def produce_expected(code):
        produce_expected_code = x.get_produce_expected("lab6", "q1", "q1")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        exec_globals['produce_expected'](code)

    # For consistency, still use this testcase but put `hot_100_mar` in it. please loop through one test case
    _test_cases = [
        ("""import scrapy

#### create a parse method and define the relevant xpaths to extract the data that we want

class Hot100Item(scrapy.Item):
    rank = scrapy.Field()
    song = scrapy.Field()
    artist = scrapy.Field()


#### create a parse method and define the relevant xpaths to extract the data that we want

class Hot100Spider(scrapy.Spider):
    name = 'hot100_list'
    allowed_domains = ['www.billboard.com']
    start_urls = ["https://www.billboard.com/charts/hot-100/"]

    def parse(self, response):
        list_100 = response.xpath('//div[@class="o-chart-results-list-row-container"]') 
        items = []
        for one_song in list_100:
            one_song_rank = one_song.xpath('descendant-or-self::span[@class = "c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"]/text()')[0].extract()
            one_song_lower = one_song.xpath('descendant-or-self::h3[1]')
            song_name = one_song_lower.xpath('text()')[0].extract()
            artist_name   = one_song_lower.xpath('following-sibling::span[1]/text()')[0].extract()
            items.append(Hot100Item(rank=one_song_rank,song=song_name,artist = artist_name))
        return items""")
    ]

    def check(self):
        for test in self._test_cases:
            Question1.produce_expected(test)
            current_directory = os.getcwd()
            print(current_directory)
            os.chdir(current_directory)  # Change the working directory to the home directory

            folder_path = os.path.join(os.getcwd() + "/hot_100_mar")
            expected_folder = os.path.join(os.getcwd() + "/.hot_100_mar")
            x.grading_directory4(folder_path, expected_folder)