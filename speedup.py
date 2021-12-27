'''
speedup.py by Amitai Farber 12/2021
Changes audio speed of all .mp3 files in a given folder
'''

from pathlib import Path
import argparse
import os
from tqdm import tqdm
from prints import info_msg


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
    parser = argparse.ArgumentParser(description='speed up MP3 files.')
    parser.add_argument('-speed', type=float, help='the required speed for the files', default=1)
    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument('-dir', type=str, help='a directory to the mp3 files', required=True)
    args = parser.parse_args()

    required_speed = args.speed
    dir_to_edit = args.dir

    speedup_mp3(required_speed, dir_to_edit)
