from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a different language other than english using column2d chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
  column2d = FusionCharts("column2d", "ex1", 600, 400, "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
        """{  
             "chart": {
                    "caption": "سوبرماركت هاري",
                    "subCaption": "الإيرادات الشهرية للعام الماضي",
                    "xAxisName": "الشهر",
                    "yAxisName": "كمية",
                    "numberPrefix": "$",
                    "theme": "fusion",
                    "rotateValues": "1",
                    "exportEnabled": "1"
                },
                "data": [
                    {
                        "label": "يناير",
                        "value": "420000"
                    },
                    {
                        "label": "فبراير",
                        "value": "810000"
                    },
                    {
                        "label": "مارس",
                        "value": "720000"
                    },
                    {
                        "label": "أبريل",
                        "value": "550000"
                    },
                    {
                        "label": "مايو",
                        "value": "910000"
                    },
                    {
                        "label": "يونيو",
                        "value": "510000"
                    },
                    {
                        "label": "يوليو",
                        "value": "680000"
                    },
                    {
                        "label": "أغسطس",
                        "value": "620000"
                    },
                    {
                        "label": "سبتمبر",
                        "value": "610000"
                    },
                    {
                        "label": "أكتوبر",
                        "value": "490000"
                    },
                    {
                        "label": "نوفمبر",
                        "value": "900000"
                    },
                    {
                        "label": "ديسمبر",
                        "value": "730000"
                    }
                ]
        }""")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : column2d.render(),'chartTitle': 'Different language example'})