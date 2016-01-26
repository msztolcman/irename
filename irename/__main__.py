import argparse
import atexit
import configparser
import glob
import os
import shlex
import shutil
import subprocess
import sys
import tempfile

from irename import __version__ as version

TMP_FILE_PATH = None
CONFIG_FILE_PATH = os.path.expanduser('~/.irename.rc')
DEFAULT_EDITOR = 'vim'
DEFAULT_EDITOR_ARGUMENTS = ''

def cleanup():
    if not TMP_FILE_PATH:
        return

    try:
        os.unlink(TMP_FILE_PATH)
    except:
        pass
atexit.register(cleanup)


class ConfigError(Exception):
    pass


class Config:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)


def get_config(path):
    data = configparser.ConfigParser()
    read = data.read(path)

    cfg = Config()
    cfg.set('editor', os.environ.get('EDITOR', os.environ.get('VISUAL', 'vim')))
    cfg.set('editor_arguments', '')
    cfg.set('force', False)
    cfg.set('interactive', False)
    cfg.set('verbose', False)

    if not read:
        return cfg

    if 'irename' not in data:
        raise ConfigError("Missing 'irename' section in config file")

    for key in data['irename']:
        cfg.set(key, data['irename'][key])

    return cfg


def parse_args(argv, defaults=None):
    if defaults is None:
        defaults = {}

    p = argparse.ArgumentParser()
    p.add_argument('--editor', '-e', type=str, default=defaults.get('editor'),
        help='Change default editor')
    p.add_argument('--editor-arguments', '-c', type=str, default=defaults.get('editor-arguments'), metavar='ARGUMENTS',
        help='Pass additional arguments to editor')
    p.add_argument('--verbose', '-v', action='store_true', default=defaults.get('verbose'),
        help='Be verbose')
    p.add_argument('--interactive', '-i', action='store_true', default=defaults.get('interactive'),
        help='Ask before every rename')
    p.add_argument('--force', '-f', action='store_true', default=defaults.get('force'),
        help='Do not ask if destination file already exists')
    p.add_argument('files', type=str, nargs='*',
        help='files to rename')
    p.add_argument('--version', action='version', version='%%(prog)s %s' % version)

    args = p.parse_args(argv)

    if not args.files:
        args.files = glob.glob('./*')

    if not args.files:
        p.error('Can\'t find any files')

    args.files.sort()

    return args


def main():
    global TMP_FILE_PATH

    config = get_config(CONFIG_FILE_PATH)
    args = parse_args(sys.argv[1:], config)

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as fh:
        TMP_FILE_PATH = fh.name
        fh.write("\n".join(args.files))

    if args.verbose:
        print("Using temporary file %s" % fh.name)

    editor_command = [args.editor]
    if args.editor_arguments:
        editor_command.extend(shlex.split(args.editor_arguments))
    editor_command.append(fh.name)

    proc = subprocess.Popen(editor_command)
    proc.wait()

    with open(fh.name, 'r') as fh:
        new_names = [name.strip() for name in fh]

    if len(args.files) != len(new_names):
        print('Number of lines does not match', file=sys.stderr)
        sys.exit(1)

    for old_name, new_name in zip(args.files, new_names):
        if old_name == new_name:
            continue

        agree = True
        asked = False
        if not args.force and os.path.exists(new_name):
            agree = input("Path '%s' already exists. Overwrite? (y/N) " % new_name).lower() in ('y', 'yes')
            asked = True

        if not asked and args.interactive:
            agree = input("Rename '%s' -> '%s'? (Y/n) " % (old_name, new_name)).lower() in ('y', 'yes')
            asked = True

        if agree:
            if not asked and args.verbose:
                print("Renaming %s -> %s" % (old_name, new_name))

            if os.path.isdir(new_name):
                shutil.rmtree(new_name)

            shutil.move(old_name, new_name)


if __name__ == '__main__':
    main()
