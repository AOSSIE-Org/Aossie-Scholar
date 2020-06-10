from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show how to attach event in chart.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", '700', '400', "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
        """{  
             "chart":
             {  
                "caption": "Countries With Most Oil Reserves [2017-18]",
                "subCaption": "In MMbbl = One Million barrels",
                "xAxisName": "Country",
                "yAxisName": "Reserves (MMbbl)",
                "numberSuffix": "K",
                "theme": "fusion"
             },
             "data": [{
                "label": "Venezuela",
                "value": "290"
            }, {
                "label": "Saudi",
                "value": "260"
            }, {
                "label": "Canada",
                "value": "180"
            }, {
                "label": "Iran",
                "value": "140"
            }, {
                "label": "Russia",
                "value": "115"
            }, {
                "label": "UAE",
                "value": "100"
            }, {
                "label": "US",
                "value": "30"
            }, {
                "label": "China",
                "value": "30"
            }]
        }""")        

    # Attach event with method name, and the callee method defined in html page.
    column2d.addEvent("dataplotClick", "onDataplotClick")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'interactive-event.html', {'output' : column2d.render(),'chartTitle': 'Example of event(interactive event)'})