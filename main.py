import pandas as pd
import urllib.parse as url_parser
from collections import defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt



def search_words(text, words):
	for word in words:
		if text.find(word) != -1:
			return True
	return False


def count_video_related(total, video_related_requests):
	names = ['Запросы, относящиеся к телевидению', 'Всё остальное']
	values = [video_related_requests, total]
	
	dpi = 80

	fig = plt.figure(dpi=dpi, figsize=(512/dpi, 384/dpi))
	mpl.rcParams.update({'font.size': 9})

	plt.title('Запросы о телевидении в общем потоке запросов (%)')

	xs = range(len(names))

	plt.pie( 
	    values, autopct='%.1f', radius = 1.1,
	    explode = [0.15] + [0 for _ in range(len(names) - 1)] )
	plt.legend(
	    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
	    loc = 'lower left', labels = names )
	fig.savefig('general_relation.png')



def classify(requests):
	content_types = {
		"adult": ["порно", "секс", "минет", "куни"],
		"series": ["сезон", "серия", "престолов"]
	}

	for request in requests:
			pass

	for content_type, key_words in content_types.items():
		pass


if __name__ == "__main__":
	log = pd.read_csv("log", sep='\t', header=0)

	devices = defaultdict(int)
	count = 0
	with open("filter_requests.txt", "w") as file:
		for index, row in log.iterrows():
			query = url_parser.urlparse(row['request']).query
			try:
				text = url_parser.parse_qs(query).get('text')[0]
			except TypeError:
				continue

			video_content_search = []
			if search_words(text, [' телев', 'телепер', 'телепрог', 'смотреть', 'сериал', 'кино']):
				count+=1
				video_content_search.append(text)
			# else:
				file.write(text + '\n')

	# classify(video_content_search)

	count_video_related(count, index)

	

# print(set(devices))
	# if i>100:
	# 	break
	# i += 1
	# print(row.__dict__)
