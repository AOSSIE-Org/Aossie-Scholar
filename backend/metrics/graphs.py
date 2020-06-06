
from .fusioncharts import FusionCharts


class my_dictionary(dict): 
  
    def __init__(self): 
        self = dict() 

    def add(self, key, value): 
        self[key] = value 


class Graph():

	#def piechart(h_index, g_index, m_index, user):



	def histFusionchart(Citations):
		Citations = list(map(int, Citations))
		prelabel_list=[]
		lab=[1, 21, 51, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751]
		label=[20, 50, 100, 150, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
		for i in label:
			if(max(Citations)> i):
				prelabel_list.append(i)
			else:
				prelabel_list.append(i)
				break
		G=[]
		c=0
		for i in prelabel_list:
			k=[]
			if (c==0):
				k= [j for j in Citations if j<= i]
			else:
				k= [j for j in Citations if (j<= i) and (j>prelabel_list[c-1])]
			c+=1
			G.append(k)

		datalist=[]
		x=lab[0:len(prelabel_list)]

		for i, j, k in zip(x, prelabel_list, G):

			my_dict= my_dictionary()
			my_dict.add("label", str(i)+'-'+str(j))
			my_dict.add("value", len(k))
			datalist.append(my_dict)
			
		d=0
		datastring="["
		for i in datalist:
			if(d != 0):
				datastring+=","
			datastring+= str(i)
			d+=1
		datastring=datastring+"]"

		chartObj = FusionCharts( 'column2d', 'ex1', '600', '400', 'chart-1', 'json', """{
			  "chart": {
			    "caption": "Publications per Citations",
			    "xaxisname": "Citations",
			    "yaxisname": "Publications",
			    "theme": "gammel"
				  },
				  "data": """+datastring+"""
				}""")

		return (chartObj)
