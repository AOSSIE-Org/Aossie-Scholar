from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts

# Loading Data from a Static XML String
# It is a example to show a Column 2D chart where data is passed as XML string format.
# The `chart` method is defined to load chart data from an XML string.

def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", '600', '400', "chart-1", "xml", 
            # The chart data is passed as a string to the `dataSource` parameter.
        """
                <chart caption='Harry&#39;s SuperMart' 
                            subcaption='Monthly revenue for last year' xaxisname='Month' 
                            yaxisname='Amount' numberprefix='¥' theme='fusion' 
                            rotatevalues='1' exportenabled='1'>
                <set label='Jan' value='420000' />
                <set label='Feb' value='810000' />
                <set label='Mar' value='720000' />
                <set label='Apr' value='550000' />
                <set label='May' value='910000' />
                <set label='Jun' value='510000' />
                <set label='Jul' value='680000' />
                <set label='Aug' value='620000' />
                <set label='Sep' value='610000' />
                <set label='Oct' value='490000' />
                <set label='Nov' value='900000' />
                <set label='Dec' value='730000' />
            </chart>
        """)
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : column2d.render(),'chartTitle': 'Chart using special character in XML data format'})