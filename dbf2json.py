#!/usr/bin/env python
import dbfread
import sys
import json
import iso8601
import datetime


class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, datetime.date):
			return o.strftime('%Y-%m-%d')

if __name__ == '__main__':
	try:
		dbf_fn = ('people.dbf')
		json_fn = ('K.json')
		try:
			json_fn = sys.argv[2]
		except IndexError:
			pass
	except IndexError:
		sys.stderr.write('usage: dbf2json <dbf_filename_input> (json_filename_input)\n\t json filename is optional, will write to stdout if not given or -. If - is given for input, it will read from stdin\n')
		sys.stderr.flush()
		sys.exit(1)
	
	def get_handle(fn, mode, do_open=True):
		if fn == '-':
			if mode == 'r':
				if do_open:
					return sys.stdin
				else:
					return '/dev/stdin'
			elif mode == 'w':
				if do_open:
					return sys.stdout
				else:
					return '/dev/stdout'
		else:
			if do_open:
				return open(fn, mode)
			else:
				return fn

	in_filename = get_handle(dbf_fn, 'r', do_open=False)
	out_handle = get_handle(json_fn, 'w')

	output = [rec for rec in DBF(in_filename)]

	json.dump(output, out_handle, indent=4, sort_keys=True, cls=JSONEncoder)
	out_handle.flush()
	out_handle.close()
	sys.exit(0)
	
 
