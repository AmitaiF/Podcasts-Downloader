import argparse
import sys

from Downloader.searchpodcast import search_podcast
from Downloader.getlinks import get_links
from Downloader.getpodcasts import download_podcasts
from Postprocessing.speedup import speedup_mp3
from Postprocessing.fixtags import fix_tags
from Utils.prints import error_msg
from Utils.prints import info_msg
import Utils.configuration

new_dir = None


def main(podcast_name, directory, speed, fix_tags):
    url = search_podcast(podcast_name)
    if url == 0:
        return -1
    links_path = get_links(url)
    if links_path == -1:
        return -1
    num_podcasts = download_podcasts(links_path, directory)
    if num_podcasts == -1:
        return -1
    if speed != 1 and speed is not None:
        new_dir = speedup_mp3(speed, directory)
    if fix_tags:
        fix_tags(directory)
        if new_dir is not None:
            fix_tags(new_dir)


if __name__ == '__main__':
    filename = sys.argv[0].split('\\')[-1].split('/')[-1]

    example_text = '''example:

 python {} -name podcast_name -dir dir_for_podcasts
 python {} -name podcast_name -dir dir_for_podcasts -speed 2 -fix-tags
'''.format(filename, filename)

    parser = argparse.ArgumentParser(description='Download Podcasts',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    requiredNamed = parser.add_argument_group('required arguments')
    requiredNamed.add_argument('-name', help='podcast name to download', required=True)
    requiredNamed.add_argument('-dir', help='directory to download the podcasts', required=True)
    parser.add_argument('-speed', help='optional to speed up the podcasts', type=float, required=False)
    parser.add_argument('-fix-tags', help='optional fix the tags of the podcasts', action='store_true')
    args = parser.parse_args()

    name = args.name
    directory = args.dir
    speed = args.speed
    fix_tags = args.fix_tags

    main(name, directory, speed, fix_tags)
