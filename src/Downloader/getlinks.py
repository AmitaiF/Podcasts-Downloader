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
import Utils.configuration as conf


def get_links(url, from_episode=None):
    podcasts_feed = feedparser.parse(url)
    if podcasts_feed.entries == []:
        print(error_msg.format('feed url is invalid!'))
        return -1

    podcasts_name = podcasts_feed.feed.title

    try:
        podcasts_urls = [entry['links'][0]['href'] for entry in podcasts_feed.entries]
        podcasts_titles = [entry['title'] for entry in podcasts_feed.entries]
    except Exception as e:
        print(error_msg.format('couldn\'t parse feed!'))
        return -1

    podcasts_dict = {}
    for index, (title, url) in enumerate(zip(podcasts_titles, podcasts_urls)):
        if title == from_episode:
            break
        podcasts_dict[index] = (title, url)

    # reverse the dictionary, so the last episode will be last
    podcasts_dict = dict(reversed(list(podcasts_dict.items())))

    directory = conf.links_directory
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
