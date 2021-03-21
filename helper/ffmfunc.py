import subprocess as sp
import json


def probe(vid_file_path):
    """
    ffprobe əmr sətrindən bir json verin
    @vid_file_path : Video faylının mütləq (tam) yolu, sətri.
    """
    if type(vid_file_path) != str:
        raise Exception('Ffprobe'ya faylın tam bir fayl yolu verin')

    command = ["ffprobe",
               "-loglevel", "quiet",
               "-print_format", "json",
               "-show_format",
               "-show_streams",
               vid_file_path
               ]

    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    return json.loads(out)


def duration(vid_file_path):
    """
    Video's duration in seconds, return a float number
    """
    _json = probe(vid_file_path)

    if 'format' in _json:
        if 'duration' in _json['format']:
            return float(_json['format']['duration'])

    if 'streams' in _json:
        # commonly stream 0 is the video
        for s in _json['streams']:
            if 'duration' in s:
                return float(s['duration'])

    raise Exception('duration Not found')


if __name__ == "__main__":
    print(duration("examplefile.mp4"))  # 10.008
