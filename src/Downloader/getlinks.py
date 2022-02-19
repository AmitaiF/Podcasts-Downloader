'''
getlinks.py by Amitai Farber 12/2021
Downloads links and titles of podcasts by given
RSS url (works on omnycontent's feed) to a .uf file
'''

import feedparser
import sys
import os
import pathlib
import json

from Utils.prints import error_msg
from Utils.prints import info_msg


def get_links(url):
    podcasts_feed = feedparser.parse(url)
    if podcasts_feed.entries == []:
        print(error_msg.format('feed url is invalid!'))
        return -1

    podcasts_name = podcasts_feed.feed.title

    podcasts_urls = [entry['links'][0]['href'] for entry in podcasts_feed.entries]
    podcasts_titles = [entry['title'] for entry in podcasts_feed.entries]

    podcasts_dict = {}
    for index, (title, url) in enumerate(zip(podcasts_titles, podcasts_urls)):
        podcasts_dict[index] = (title, url)

    directory = pathlib.Path(__file__).parent.resolve().as_posix()
    directory += '/links'
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
    except Exception as e:
        print(error_msg.format('couldn\'t create the links folder!'))
        print(error_msg.format(e))
        return -1
    file_path = directory + '/{}.uf'.format(podcasts_name)

    try:
        dump_file = open(file_path, 'w')
        json.dump(podcasts_dict, dump_file)
    except Exception as e:
        print(error_msg.format('couldn\'t write to the file!'))
        print(error_msg.format(e))
        return -1

    print(info_msg.format('Finished downloading {} URLs!'.format(len(podcasts_dict))))
    return file_path
