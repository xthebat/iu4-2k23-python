from argparse import *
from argparse import Namespace
from sys import stderr

lim = 200


def file_load(filename_):
    '''
    Performs file loading
    @ arg: filename_ [str] - name of loading file
    @ return: [str] content of the file
    '''
    try:
        with open(file=filename_, mode='r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        log(text_=f'ERROR: Can\'t open file {filename_}!', terminate_=True)


def log(text_, terminate_ = False):
    '''
    Performs console message print
    @ arg: text_ [str] - printed message
    @ arg: terminate_ [bool] - script termination flag
    @ return: [None]
    '''
    print(text_, file=stderr)
    if terminate_:
        exit(1)


def splitString(string_, char_limit_, is_full_score_= False):
    '''
    Performs string splitting into separate words
    @ arg: string_ [str] - string for split
    @ arg: char_limit_ [int] - string for split maximum length
    @ arg: is_full_score_ [bool] - flag whether we add 
    unsplitted string to stringlist
    @ return: stringlist [list[str]] - list with all words (and maybe lines)
    '''
    raw_stringlist = string_.strip().split('\n')
    stringlist = []

    for line in raw_stringlist:
        if is_full_score_ and 'score' in line:
            stringlist.append(line + '\n')
            if len(line) > char_limit_:
                log(text_=f'ERROR: Can\'t parse word with chosen maximum number of chars!', terminate_=True)
            continue
        words = line.split(' ')
        for word in words:
            if len(word) > char_limit_:
                log(text_=f'ERROR: Can\'t parse word with chosen maximum number of chars!', terminate_=True)
            stringlist.append(word)
        stringlist.append('\n')

    return stringlist


def tagMerge(words_):
    '''
    Performs tags merging for splitted words
    @ arg: words_ [list[str]] - list with splitted words
    @ return: words_ [list[str]] - list with splitted words with merged tags
    '''
    tag_start = None
    for index, word in enumerate(words_):
        if word.startswith('@') and word.endswith(':'):
            continue
        if word.startswith('@'):
            tag_start = index
            continue
        if tag_start is not None:
            words_[tag_start] += ' ' + word
            words_[index] = ''
        if word.endswith(':') and tag_start is not None:
            tag_start = None
            continue

    while '' in words_:
        words_.remove('')

    return words_


def wordGroup(words_, char_limit_):
    '''
    Perform words grouping by lines
    @ arg: words_ [list[str]] - preprocessed list with words
    @ arg: char_limit_ [int] - line maximum length
    @ return: data [list[str]] - list with words groupes by lines
    '''

    data = []
    substring = ''

    for word in words_:
        if word == '\n':
            substring += word
            continue
        if word.endswith('\n'):
            if len(word) + len(substring) <= char_limit_:
                substring += word
                continue
            data.append(substring)
            substring = word
            continue
        if len(word) + len(substring) <= char_limit_:
            substring += word + ' '
            continue

        data.append(substring)
        substring = word

    if substring != '':
        data.append(substring)

    return data


def handleData(string_, char_limit_, is_full_score_):
    '''
    Performs initial data processing
    @ string_ [str] - string for split
    @ arg: char_limit_ [int] - line maximum length
    @ arg: is_full_score_ [bool] - flag whether we add 
    unsplitted string to stringlist
    @ return: data [list[str]] - preprocessed data
    '''
    words = splitString(string_=string_, char_limit_=char_limit_, is_full_score_=is_full_score_)
    words = tagMerge(words_=words)
    data = wordGroup(words_=words, char_limit_=char_limit_)

    return data


def dataFilter(data_, requirement_):
    '''
    Perform data filtering
    @ arg: data_ [list[str]] - data for filtration
    @ arg: requirement_ [str] - particular filtering requirement
    @ return: [tuple[str]] - data filter by requirement
    '''
    return tuple(filter(eval(requirement_), data_))


def dataPrint(data_):
    '''
    Performs data printing
    @ arg: data_ [list[str] or tuple[str]] - data for printing
    @ return: [None] 
    '''
    for i, substr in enumerate(data_):
        print(f'Substring #{i}')
        print(f'{substr}')


def dataDump(data_, outdir_ = None):
    '''
    Performs data dumping
    @ arg: data_ [list[str] or tupke[str]] - data for dump
    @ arg: outdir_ [str] - directory for data dumping
    @ return: [None] 
    '''
    for i, substr in enumerate(data_):
        try:
            with open(file=f'{outdir_}/substring_{i}', mode='w', encoding='utf-8') as file:
                file.write(f'Substring #{i}\n')
                file.write(f'{substr}')
        except FileNotFoundError:
            log(text_=f'ERROR: Can\'t open directory <{outdir_}>!\n', terminate_=True)


def argsParse():
    '''
    Performs arguments parsing
    @ arg: [None]
    @ return: [Namespace] - namespace of parsed arguments
    '''
    parser = ArgumentParser(description="Best py prog ever!")
    parser.add_argument('-f', '--filename',
                        dest='filename',
                        required=True,
                        nargs=1,
                        metavar='<filename>',
                        help='input File name'
                        )
    parser.add_argument('-n', '--number',
                        dest='char_limit',
                        required=False,
                        nargs=1,
                        default=lim,
                        metavar='<chars number>',
                        help='maximum Number of chars in the string'
                        )

    parser.add_argument('-l', '--line',
                        dest='is_whole_line',
                        required=False,
                        default=None,
                        action='store_true',
                        help='key with no args, indicates, '
                             'that you can\'t separate `score` Line')
    parser.add_argument('-d', '--dir',
                        dest='dir',
                        required=False,
                        nargs=1,
                        metavar='<directory>',
                        help='output Directory'
                        )
    parser.add_argument('-r', '--requirement',
                        dest='req',
                        required=False,
                        nargs=1,
                        metavar='<lambda-func>',
                        help='bonus Requirement for parser')

    return parser.parse_args()


def main():
    args = argsParse()

    try:
        limit = int(args.char_limit[0])
    except ValueError:
        limit = lim
    if limit < 0:
        log(f'ERROR: Maximum number of characters in line is negative!', terminate_=True)

    filestr = file_load(filename_=args.filename[0])
    parsed_data: list = handleData(string_=filestr, char_limit_=limit, is_full_score_=args.is_whole_line)

    if args.req:
        parsed_data: tuple = dataFilter(data_=parsed_data, requirement_=args.req[0])

    if args.dir:
        dataDump(data_=parsed_data, outdir_=args.dir[0])
        exit(0)
    dataPrint(data_=parsed_data)


if __name__ == '__main__':
    main()