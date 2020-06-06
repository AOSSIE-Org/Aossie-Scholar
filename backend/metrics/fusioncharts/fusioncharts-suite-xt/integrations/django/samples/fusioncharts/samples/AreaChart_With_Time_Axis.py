from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts
from ..fusioncharts import FusionTable
from ..fusioncharts import TimeSeries
import requests

# Loading Data and schema from a Static JSON String url
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/area-chart-with-time-axis-data.json').text
    schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/area-chart-with-time-axis-schema.json').text

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("chart", """{ 
											showLegend: 0
										}""")

    timeSeries.AddAttribute("caption", """{ 
                                        text: 'Daily Visitors Count of a Website'
                                    }""")

    timeSeries.AddAttribute("yAxis", """[{
                                            plot: {
                                            value: 'Daily Visitors',
                                            type: 'area'
                                            },
                                        title: 'Daily Visitors (in thousand)'
                                    }]""")
                                    
    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : fcChart.render(),'chartTitle': "Area chart with time axis"})