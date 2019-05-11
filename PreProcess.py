#coding=utf-8
from configure import *


def load_data(file_path):
	"""
	加载数据
	"""
	data = []
	


	with open(file_path) as f:
		for line in f:
			line = line.strip()
			contents = line.split(',"')
			assert len(contents) == 4
			text_id = contents[0][1:][:-2]
			text_content  = contents[1][:-2]
			event_type = contents[2][:-2]
			event_subject = contents[3][:-2]

			data.append([text_id, text_content, event_type, event_subject])
	return data

if __name__ == '__main__':
	train_data = load_data(train_data_path)

	# eval_data = load_data(eval_data_path)