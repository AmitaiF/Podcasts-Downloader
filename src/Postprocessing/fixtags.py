'''
fixtags.py by Amitai Farber 12/2021
Changes the 'TITLE' tag of .mp3 file to the filename,
in a given folder
'''

import sys
from pathlib import Path
from tqdm import tqdm
import mutagen.id3

from Utils.prints import error_msg
from Utils.prints import info_msg


def fix_tags(dir_to_edit):
    try:
        mp3_files = list(Path(dir_to_edit).rglob("*.[mM][pP]3"))
    except Exception as e:
        print(error_msg.format('Invalid path!'))
        print(error_msg.format(e))
        return -1

    for filename in tqdm(mp3_files):
        tags = mutagen.id3.ID3(filename)
        for key, value in tags.items():
            try:
                if key == 'TIT2':
                    new_tag = filename.as_posix().split('/')[-1]
                    new_tag = new_tag.split('.')[0]
                    value.text[0] = new_tag
            except Exception as e:
                print(error_msg.format('couldn\'t fix {}!'.format(filename)))
                print(error_msg.format(e))
        tags.save(filename)
