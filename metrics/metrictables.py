import django_tables2 as tables
from .models import ScholarProfile

class NameTable(tables.Table):
	Title = tables.Column()
	CoAuthors= tables.Column()
	Citations= tables.Column()
	Ncitations= tables.Column()
	Year= tables.Column()
	class Meta:
		attrs = {
			'class': 'table table-striped table-dark table-bordered table-hover',
			'thead' : {
				'class': 'thead-dark'
			}
		}

	def createtable(publications, normalized_citations, citations, coAuthors, Year):
		dlist=[]

		for i, j, k, l, m in zip(publications, normalized_citations, citations,coAuthors, Year):
			d={}
			d["Title"]= i
			d["Ncitations"]= j
			d["Citations"]= k
			d["CoAuthors"]= l
			d["Year"]= m
			dlist.append(d)

		table= NameTable(dlist)
		return (table)