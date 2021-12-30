import googlesearch
import feedparser
from prints import error_msg
from prints import info_msg
import sys


def search_podcast(podcast_name):
    query = 'site:https://www.omnycontent.com/ {}'.format(podcast_name)
    search = googlesearch.search(query)
    for result in search:
        link = result
        feed = feedparser.parse(link)
        if not feed.entries == []:
            name = feed.feed.title
            if name == podcast_name:
                return link
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(error_msg.format('Incorrect number of arguments!'))
        filename = sys.argv[0].split('\\')[-1].split('/')[-1]
        print(info_msg.format('Use: {} <podcast name>'.format(filename)))
    else:
        name = sys.argv[1]
        search_podcast(name)
