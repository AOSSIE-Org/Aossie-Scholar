from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a Column 2D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", '600', '400', "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
        """{  
             "chart":
             {  
                "caption": "Sales by Region",
                "xaxisname": "Region",
                "yaxisname": "Total Sales",
                "numbersuffix": "K",
                "theme": "fusion"
             },
             "data": [{
                "label": "Europe",
                "value": "827508",
                "link": "j-updateChart-Europe"
            }, {
                "label": "North America",
                "value": "342947",
                "link": "j-updateChart-NA"
            }, {
                "label": "South America",
                "value": "183881",
                "link": "j-updateChart-SA"
            }]
        }""")

    # Create an object for the column2d chart using the FusionCharts class constructor
    secondColumn2d = FusionCharts("column2d", "chartTwo", '600', '400', "chart-2", "json",
            # The chart data is passed as a string to the `dataSource` parameter.
        """{  
                "chart": {
                
            }
        }""")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'chart-update-onclick.html', {'output1' : column2d.render(), 'output2' : secondColumn2d.render(),'chartTitle': 'Updating Different Chart'}) 