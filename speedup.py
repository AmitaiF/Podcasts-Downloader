'''
speedup.py by Amitai Farber 12/2021
Changes audio speed of all .mp3 files in a given folder
'''

from pathlib import Path
import os
import sys
from tqdm import tqdm
from prints import info_msg
from prints import error_msg


COMMAND = 'ffmpeg -y -i "{}" -filter:a "atempo={}" -vn "{}" 2>NUL'


def speedup_mp3(required_speed, dir_to_edit):
    mp3_files = list(Path(dir_to_edit).rglob("*.[mM][pP]3"))

    for filename in tqdm(mp3_files):
        filename = filename.as_posix()
        if '(פי ' in filename:
            continue
        current_dir = '/'.join(filename.split('/')[:-1])
        if required_speed % 1 == 0:
            title_addition = ' (פי ' + str(int(required_speed)) + ')'
        else:
            title_addition = ' (פי ' + str(required_speed) + ')'
        new_dir = current_dir + title_addition
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        new_filename = filename.split('/')[-1].split('.')[0] + title_addition + '.mp3'
        new_file = new_dir + '/' + new_filename

        os.system(COMMAND.format(filename, required_speed, new_file))

    print(info_msg.format('Speeduped {} files!'.format(len(mp3_files))))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        dir_to_edit = sys.argv[1]
        required_speed = sys.argv[2]
        speedup_mp3(required_speed, dir_to_edit)
    else:
        print(error_msg.format('Incorrect number of arguments!'))
        filename = sys.argv[0].split('\\')[-1].split('/')[-1]
        print(info_msg.format('Use: {} <folder> <speed>'.format(filename)))
