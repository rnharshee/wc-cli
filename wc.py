import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser(prog="ccwc",description="Counts number of bytes,characters,words and lines",epilog="Thanks for using ccwc")

parser.add_argument("files",nargs="*",default=sys.stdin, type=argparse.FileType('r'))

parser.add_argument("-c","--bytes",action="store_true")

parser.add_argument("-w","--words",action="store_true")

parser.add_argument("-m","--chars",action="store_true")

parser.add_argument("-l","--lines",action="store_true")

args = parser.parse_args()


def printResult(content,file_name=""):
    chars = words = lines =bytes_count = 0
    for line in content:
        lines += 1
        words += len(line.split())
        chars += len(line)+1
        bytes_count += len(line.encode('utf-8')) + len("\n".encode('utf-8'))

    res = [" "]
    if args.bytes:
        res.append(bytes_count)
    if args.words:
        res.append(words)
    if args.chars:
        res.append(chars)
    if args.lines:
        res.append(lines)
    res.append(file_name)
    if len(res) > 2:
        for i in res:
            print(i, end=" ")
        print()
    else:
        print(lines,words,bytes_count,file_name)

if args.files:
    if(type(args.files) is list):
        for file in args.files:
            target_file = Path(file.name)
            if not target_file.exists():
                print("The target file does not exists")
                raise SystemExit(1)

            if target_file.is_dir():
                print("The target file is a directory")
                raise SystemExit(1)   
            content = open(str(target_file), 'r')
            printResult(content,file.name)
    else:
        # print(files)
        content = args.files.read().splitlines()
        printResult(content)
        

    

    



      


    