from os import rename, listdir

fnames = listdir('.')

for fname in fnames:
	result = fname
	result.replace('20', '')
	result.replace('0', '')
	print result
	rename(fname, result)