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

    data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/date-range-event-overlay-data.json').text
    schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/date-range-event-overlay-schema.json').text

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{ 
								text: 'Interest Rate Analysis'
							  }""")

    timeSeries.AddAttribute("subCaption", """{ 
                                        text: 'Federal Reserve (USA)'
                                    }""")

    timeSeries.AddAttribute("yAxis", """[{
                                            plot: 'Interest Rate',
                                            format:{
                                            suffix: '%'
                                            },
                                            title: 'Interest Rate'
                                        }]""")

    timeSeries.AddAttribute("xAxis", """{
                                        plot: 'Time',
                                        timemarker: [{
                                            start: 'Jul-1981',
                                            end: 'Nov-1982',
                                            label: 'Economic downturn was triggered by {br} tight monetary policy in an effort to {br} fight mounting inflation.',
                                            timeFormat: '%b-%Y'
                                        }, {
                                            start: 'Jul-1990',
                                            end: 'Mar-1991',
                                            label: 'This eight month recession period {br} was characterized by a sluggish employment recovery, {br} most commonly referred to as a jobless recovery.',
                                            timeFormat: '%b-%Y'
                                        }, {
                                            start: 'Jun-2004',
                                            end: 'Jul-2006',
                                            label: 'The Fed after raising interest rates {br} at 17 consecutive meetings, ends its campaign {br} to slow the economy and forestall inflation.',
                                            timeFormat: '%b-%Y'
                                        }, {
                                            start: 'Dec-2007',
                                            end: 'Jun-2009',
                                            label: 'Recession caused by the worst {br} collapse of financial system in recent {br} times.',
                                            timeFormat: '%b-%Y'
                                        }]
                                    }""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : fcChart.render(),'chartTitle': "Date range event overlay"})