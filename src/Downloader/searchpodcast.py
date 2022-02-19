'''
searchpodcast.py by Amitai Farber 12/2021
Search on google for the requested podcast
'''


import googlesearch
import feedparser
import sys

from Utils.prints import error_msg
from Utils.prints import info_msg


def search_podcast(podcast_name):
    query = 'site:https://www.omnycontent.com/ {}'.format(podcast_name)
    search = googlesearch.search(query)
    for result in search:
        link = result
        feed = feedparser.parse(link)
        if not feed.entries == []:
            name = feed.feed.title
            if name.lower() == podcast_name.lower():
                return link
    print(info_msg.format('Podcast name not found!'))
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(error_msg.format('Incorrect number of arguments!'))
        filename = sys.argv[0].split('\\')[-1].split('/')[-1]
        print(info_msg.format('Use: {} <podcast name>'.format(filename)))
    else:
        name = sys.argv[1]
        search_podcast(name)
