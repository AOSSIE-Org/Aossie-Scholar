from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# Example to create a Angular Gauge with the chart data passed as JSON string format.
# The `chart` method is defined to load chart data from a JSON string.

def chart(request):
      
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = FusionCharts("angulargauge", "ex1" , "450", "270", "chart-1", "json", 
        # The data is passed as a string in the `dataSource` as parameter.
        """{  
            "chart": { 
                "caption": "Customer Satisfaction Score", 
                "subcaption": "Los Angeles Topanga", 
                "plotToolText": "Current Score: $value", 
                "theme": "fint", 
                "chartBottomMargin": "50", 
                "showValue": "1" 
            }, 
            "colorRange": { 
                "color": [{ 
                    "minValue": "0", 
                    "maxValue": "45", 
                    "code": "#e44a00"
                }, { 
                    "minValue": "45", 
                    "maxValue": "75", 
                    "code": "#f8bd19" 
                }, { 
                    "minValue": "75", 
                    "maxValue": "100", 
                    "code": "#6baa01" 
                }] 
            }, 
            "dials": { 
                "dial": [{ 
                    "value": "70", 
                    "id": "dial1" 
                }] 
            }
        }""")
    # Alternatively, you can assign this string to a string variable in a separate JSON file
    # and pass the URL of that file to the `dataSource` parameter.
    return  render(request, 'update-data-runtime.html', {'output' : angularGauge.render(),'chartTitle': 'Update data at runtime'})