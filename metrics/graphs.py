import matplotlib
import matplotlib.pyplot as plt

class Graph():

	def piechart(h_index, g_index, m_index, user):
		data_to_fill= [h_index, g_index, m_index]
		labels= ['h_index', 'g_index', 'm_index']
		#colors= ['#9CF0E0', '#0DF408', '#D50BF6']
		plt.pie(data_to_fill, labels= labels, startangle=90, autopct='%.1f%%')
		plt.title('Metrics')
		plt.savefig('metrics/static/metrics/images/'+ user +'.png', bbox_inches=None)
