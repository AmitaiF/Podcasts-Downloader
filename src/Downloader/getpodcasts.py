'''
getpodcasts.py by Amitai Farber 12/2021
Downloads podcasts from a list of URLs from
an .uf file.
'''

import sys
import json
import pathlib
import requests
import os
from tqdm import tqdm

from Utils.prints import error_msg
from Utils.prints import info_msg


allowed_chars = [' ', '-']


def download_podcasts(file_path, new_dir):
    try:
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
    except Exception as e:
        print(error_msg.format('couldn\'t create the given folder!'))
        print(error_msg.format(e))
        return -1

    filename = pathlib.Path(file_path).as_posix().split('/')[-1]
    podcast_name = filename.split('.')[0]

    try:
        urls_file = open(file_path, 'r')
    except Exception as e:
        print(error_msg.format('can\'t open the file!'))
        print(error_msg.format(e))
        return -1

    podcast_urls = json.load(urls_file)
    urls_file.close()

    indexes_to_remove = []
    try:
        for index in tqdm(podcast_urls):
            title, url = podcast_urls[index]
            podcast = requests.get(url)
            if podcast.status_code != 200:
                print(error_msg.format('couldn\'t get {}'.format(title)))
            else:
                podcast_filename = '{} {} - '.format(podcast_name, int(index) + 1)
                # for cases that the title contains non-hebrew letters
                for char in title:
                    if char.isalpha() or char.isdigit() or char in allowed_chars:
                        podcast_filename += char
                    else:
                        podcast_filename += '_'
                try:
                    podcast_file = open('{}\\{}.mp3'.format(new_dir, podcast_filename), 'wb')
                    podcast_file.write(podcast.content)
                    podcast_file.close()
                    indexes_to_remove.append(index)
                except Exception as e:
                    print(error_msg.format('couldn\'t create {}/{}.mp3'.format(new_dir, podcast_filename)))
                    print(error_msg.format(e))

    # in case that the program breaks,
    # remove the podcasts that was downloaded
    except:
        pass

    for index in indexes_to_remove:
        podcast_urls.pop(index)

    try:
        urls_file = open(file_path, 'w')
        json.dump(podcast_urls, urls_file)
    except Exception as e:
        print(error_msg.format('couldn\'t save the new podcasts file!'))
        print(error_msg.format(e))
        return -1

    num_podcasts = len(indexes_to_remove)
    print(info_msg.format('Finished downloading {} podcasts!'.format(num_podcasts)))
    return num_podcasts


if __name__ == '__main__':
    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        new_dir = sys.argv[2]
        download_podcasts(file_path, new_dir)
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
        directory = pathlib.Path(__file__).parent.resolve().as_posix()
        new_dir = directory + '/{}'.format(podcast_name)
        download_podcasts(file_path, new_dir)
    else:
        print(error_msg.format('Incorrect number of arguments!'))
        filename = sys.argv[0].split('\\')[-1].split('/')[-1]
        print(info_msg.format('Use: {} <filename>.uf <target folder>'.format(filename)))
