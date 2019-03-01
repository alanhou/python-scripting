import pathlib, shutil, sys, tempfile

with tempfile.TemporaryDirectory() as d:
	shutil.unpack_archive('work_sample.tar.gz',
		extract_dir='/home/student/work')
	prefix_len = len(d) + 1
	for extracted in pathlib.Path(d).rglob('*'):
		print(str(extracted)[prefix_len:])
