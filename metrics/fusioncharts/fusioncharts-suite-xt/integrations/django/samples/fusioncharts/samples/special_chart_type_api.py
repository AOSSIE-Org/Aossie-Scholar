from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show how to attach event in chart.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    # Create an object for the pie2d chart using the FusionCharts class constructor
    pie2d = FusionCharts("pie2d", "ex1", '700', '400', "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
        """{  
            "chart": 
            { 
                "caption": "Market Share of Web Servers",
                "plottooltext": "<b>$percentValue</b> of web servers run on $label servers",
                "showLegend": "0",
                "enableMultiSlicing": "0",
                "showPercentValues": "1",
                "legendPosition": "bottom",
                "useDataPlotColorForLabels": "1",
                "theme": "fusion"
            },
            "data": [{ 
                    "label": "Apache",
                    "value": "32647479"
                }, { 
                    "label": "Microsoft", 
                    "value": "22100932" 
                }, { 
                    "label": "Zeus", 
                    "value": "14376" 
                }, { 
                    "label": "Other",
                    "value": "18674221" 
            }]
        }""")        

    # Attach event with method name, and the callee method defined in html page.)
    pie2d.addEvent("dataplotClick", "plotClickHandler")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'special-chart-type-api.html', {'output' : pie2d.render(),'chartTitle': 'Special chart type API'})