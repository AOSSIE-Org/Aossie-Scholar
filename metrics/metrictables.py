import django_tables2 as tables
from .models import ScholarProfile

class NameTable(tables.Table):
   	Title = tables.Column()
   	CoAuthors= tables.Column()
   	Citations= tables.Column()
   	Ncitations= tables.Column()
   	Year= tables.Column()
   	
   	