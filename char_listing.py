import sys
import re

def char2singlequotachar(match):
	return "'%s',"%match.group(1)

def str2charlist(match):
	replace_str = '{'
	char_split = re.compile(r'(\\x[a-fA-F0-9]{1,2}|\\[0-7]{1,3}|\\[a-z\"\'\\]|.)')
	replace_str += char_split.sub(char2singlequotachar, match.group(1)[1:-1])[:-1]
	replace_str += '}'
	return match.group(0).replace(match.group(1),replace_str)

if len(sys.argv) != 2:
	print "Need argv1!"
	exit()

with open(sys.argv[1],'rb') as f:
	source_data = f.read()

search = re.compile(r'char *[a-zA-Z0-9_]*\[\] *= *(".*");*')
with open(sys.argv[1],'wb') as f:
	f.write(search.sub(str2charlist,source_data))