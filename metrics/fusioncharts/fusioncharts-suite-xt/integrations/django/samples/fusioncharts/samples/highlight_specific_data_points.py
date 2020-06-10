from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a spline chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the spline chart using the FusionCharts class constructor
  spline = FusionCharts("spline", "ex1", 600, 400, "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
        """{  
             "chart":
             {  
                "caption": "Bakersfield Central - Total footfalls",
                "subCaption": "Last week",
                "xAxisName": "Day",
                "yAxisName": "No. of Visitors (In 1000s)",
                "showValues": "0",
                "theme": "fusion"
             },
             "annotations":{
                "groups": [
                    {
                        "id": "anchor-highlight",
                        "items": [
                            {
                                "id": "high-star",
                                "type": "circle",
                                "x": "$dataset.0.set.2.x",
                                "y": "$dataset.0.set.2.y",
                                "radius": "12",
                                "color": "#6baa01",
                                "border": "2",
                                "borderColor": "#f8bd19"
                            },
                            {
                                "id": "label",
                                "type": "text",
                                "text": "Highest footfall 25.5K",
                                "fillcolor": "#6baa01",
                                "rotate": "90",
                                "x": "$dataset.0.set.2.x+75",
                                "y": "$dataset.0.set.2.y-2"
                            }
                        ]
                    }
                ]
            },
             "data": [
                {
                    "label": "Mon",
                    "value": "15123"
                },
                {
                    "label": "Tue",
                    "value": "14233"
                },
                {
                    "label": "Wed",
                    "value": "25507"
                },
                {
                    "label": "Thu",
                    "value": "9110"
                },
                {
                    "label": "Fri",
                    "value": "15529"
                },
                {
                    "label": "Sat",
                    "value": "20803"
                },
                {
                    "label": "Sun",
                    "value": "19202"
                }
            ]
        }""")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : spline.render(),'chartTitle': 'Highlight specific data points through API'})