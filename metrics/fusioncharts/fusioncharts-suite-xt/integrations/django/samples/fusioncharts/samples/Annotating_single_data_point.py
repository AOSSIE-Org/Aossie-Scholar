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

    data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/annotating-single-data-point-data.json').text
    schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/annotating-single-data-point-schema.json').text

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

    timeSeries.AddAttribute("dataMarker", """[{
                                        seriesName: 'Interest Rate',
                                        time: 'Mar-1980',
                                        identifier: 'H',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'As a part of credit control program, under the leadership of Paul Volcker, the Fed tightened the money supply, allowing the federal fund rates to approach 20 percent.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'Aug-1982',
                                        identifier: 'L',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'The FED eases off the monetary brakes, allowing interest rates to fall and the economy to begin a strong recovery.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'Oct-1987',
                                        identifier: 'L',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'The FED is forced to ease rate after the stock market crash.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'May-1989',
                                        identifier: 'H',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'Liquidity problem forced the Fed to increase rate to nearly 10%.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'Sept-1992',
                                        identifier: 'L',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'To fight the jobless economy growth the Fed had to reduce the interest rate to 3%.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'Jun-2003',
                                        identifier: 'L',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'Struggling to revive the economy, the FED cuts it’s benchmark rate to 1%.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'Sep-2007',
                                        identifier: 'L',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'Fed started reducing the Federal Fund Rate.'
                                        }, {
                                        seriesName: 'Interest Rate',
                                        time: 'Dec-2008',
                                        identifier: 'L',
                                        timeFormat: '%b-%Y',
                                        tooltext: 'Fed reduced the interest rates to sub 0.25% to manage the menace of longest economic downturn since World War 2'
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : fcChart.render(),'chartTitle': "Annotating single data point"})