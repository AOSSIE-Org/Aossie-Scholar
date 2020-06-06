from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a marimekko chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the marimekko chart using the FusionCharts class constructor
  marimekko = FusionCharts("marimekko", "ex1", 600, 400, "chart-1", "json", 
          # The chart data is passed as a string to the `dataSource` parameter.
          # Custom tool-text string built using a combination of HTML and chart macro variables
        """{  
             "chart": {
                    "caption": "Top 3 Electronic Brands in Top 3 Revenue Earning States",
                    "subcaption": "Last month",
                    "aligncaptiontocanvas": "0",
                    "yaxisname": "Statewise Sales (in %)",
                    "xaxisname": "Brand",
                    "numberprefix": "$",
                    "showxaxispercentvalues": "1",
                    "showsum": "1",
                    "showPlotBorder": "1",
                    "plottooltext": "<div id='nameDiv' style='font-size: 14px; border-bottom: 1px dashed #666666; font-weight:bold; padding-bottom: 3px; margin-bottom: 5px; display: inline-block;'>$label :</div>{br}State: <b>$seriesName</b>{br}Sales : <b>$dataValue</b>{br}Market share in State : <b>$percentValue</b>{br}Overall market share of $label: <b>$xAxisPercentValue</b>",
                    "theme": "fusion"
                },
                "categories": [
                    {
                        "category": [
                            {
                                "label": "Bose"
                            },
                            {
                                "label": "Dell"
                            },
                            {
                                "label": "Apple"
                            }
                        ]
                    }
                ],
                "dataset": [
                    {
                        "seriesname": "California",
                        "data": [
                            {
                                "value": "335000"
                            },
                            {
                                "value": "225100"
                            },
                            {
                                "value": "164200"
                            }
                        ]
                    },
                    {
                        "seriesname": "Washington",
                        "data": [
                            {
                                "value": "215000"
                            },
                            {
                                "value": "198000"
                            },
                            {
                                "value": "120000"
                            }
                        ]
                    },
                    {
                        "seriesname": "Nevada",
                        "data": [
                            {
                                "value": "298000"
                            },
                            {
                                "value": "109300"
                            },
                            {
                                "value": "153600"
                            }
                        ]
                    }
                ]
        }""")

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  return  render(request, 'index.html', {'output' : marimekko.render(),'chartTitle': 'Customizing tooltip'})
