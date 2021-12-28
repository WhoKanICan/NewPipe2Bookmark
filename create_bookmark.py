import configparser
import datetime
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Read config file
config = configparser.ConfigParser()
if Path("private_config.ini").exists():
    config.read("private_config.ini")
else:
    config.read("config.ini")

# Set val to vars
INPUT_PATH = Path(config["PATHS"]["INPUT_PATH"])
OUTPUT_PATH = Path(config["PATHS"]["OUTPUT_PATH"])


def latest_json(json_path):
    if INPUT_PATH.is_dir():
        if OUTPUT_PATH.is_dir():
            json_files = list(json_path.glob("newpipe_subscriptions_*.json"))
            number = [int(x.stem.split("_")[-1]) for x in json_files]  # get ISO 8601 format from filename
            zipit = zip(number, json_files)
            file_number, file_path = sorted(zipit, key=lambda item: item[0], reverse=True)[0]
            return file_path
        else:
            sys.exit(f"Folder could not be found: {OUTPUT_PATH}")
    else:
        sys.exit(f"Folder could not be found: {INPUT_PATH}")


def create(newpipe_json, html_path):
    html_path = html_path.joinpath("YouTube Bookmarks.html")
    with html_path.open("w", encoding="UTF-8") as b:
        DATE = int((datetime.now() - datetime(1970, 1, 1)) / timedelta(seconds=1))
        b.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n'
                '<!-- This is an automatically generated file.\n'
                '\tIt will be read and overwritten.\n'
                '\tDO NOT EDIT! -->\n'
                '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n'
                '<TITLE>Bookmarks</TITLE>\n'
                '<H1>Bookmarks</H1>\n'
                '<DL><p>\n'
                f'\t<DT><H3 ADD_DATE="{DATE}" LAST_MODIFIED="{DATE}" PERSONAL_TOOLBAR_FOLDER="true">Youtube Subscriptions</H3>\n'
                '\t<DL><p>\n')
        with newpipe_json.open("r", encoding="UTF-8") as f:
            j = json.load(f)['subscriptions']
            for arr in j:
                b.write('\t\t<DT><A HREF="{}">{}</A>\n'.format(arr['url'], arr['name']))
            b.write("\t</DL><p>\n</DL><p>")


if __name__ == '__main__':
    latest = latest_json(INPUT_PATH)
    create(latest, OUTPUT_PATH)
