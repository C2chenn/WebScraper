from os import rename, listdir

fnames = listdir('.')

for fname in fnames:
	result = ""
	for char in fname:
		if char != '%':
			result += char
	if result != 'fix_name.py':
		result = result[5:]
		if result[0] == '0':
			result = result[0:]
	result.replace("20", "")
	result.replace("0", "")
	rename(fname, result)
