from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show how to attach event in chart.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    # Create an object for the hlineargauge chart using the FusionCharts class constructor
    lineargauge = FusionCharts("hlineargauge", "ex1", '700', '400', "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
        """{  
            "chart": { 
                "caption": "Server CPU Utilization", 
                "subcaption": "food.hsm.com", 
                "lowerLimit": "0", 
                "upperLimit": "100", 
                "numberSuffix": "%", 
                "valueAbovePointer": "0", 
                "editmode":"1" 
            }, 
            "colorRange": { 
                "color": [ 
                    { 
                        "minValue": "0", 
                        "maxValue": "35", 
                        "label": "Low", 
                        "code": "#1aaf5d"
                    }, { 
                        "minValue": "35", 
                        "maxValue": "70", 
                        "label": "Moderate", 
                        "code": "#f2c500"
                    }, { 
                        "minValue": "70",
                        "maxValue": "100",
                        "label": "High",
                        "code": "#c02d00" 
                    } ] 
                }, 
                "pointers": 
                { 
                    "pointer": [{
                        "value": "72.5" 
                    }]
                }
        }""")        

    # Attach event with method name, and the callee method defined in html page.
    lineargauge.addEvent("realtimeUpdateComplete", "onUpdate")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'special-event.html', {'output' : lineargauge.render(),'chartTitle': 'Example of event(interactive event)'})