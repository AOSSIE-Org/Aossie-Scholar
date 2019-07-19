import matplotlib
import matplotlib.pyplot as plt

class Graph():

	def piechart(h_index, g_index, m_index, user):
		print (h_index, g_index, m_index)
		data_to_fill= [h_index, g_index, m_index]
		labels= ['h-index', 'g-index', 'm-index']
		colors= ['#F3E355', '#C4C4C4', '#D50BF6']
		plt.pie(data_to_fill, labels= labels, colors= colors, startangle=90, autopct='%.1f%%')
		plt.title('Metrics')
		plt.savefig('metrics/static/metrics/images/'+ user +'.png', bbox_inches=None)
