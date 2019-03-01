import tarfile, shutil, sys

shutil.make_archive(
	'work_sample', 'gztar',
	root_dir='..',
	base_dir='work'
)
print('Archive contents:')
with tarfile.open('work_sample.tar.gz', 'r') as t_file:
	for names in t_file.getnames():
		print(names)
