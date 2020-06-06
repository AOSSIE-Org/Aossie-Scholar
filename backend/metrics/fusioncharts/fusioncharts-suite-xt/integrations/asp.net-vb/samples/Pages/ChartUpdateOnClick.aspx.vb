Imports FusionCharts.Charts
Partial Class Pages_ChartUpdateOnClick
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'store chart config data as json string
        Dim firstChartData, secondChartData As String
        firstChartData = "{            'chart': {                'caption': 'Sales by Region',                'xaxisname': 'Region',                'yaxisname': 'Total Sales',                'numbersuffix': 'K',                'theme': 'fusion'            },            'data': [{                'label': 'Europe',                'value': '827508',                'link': 'j-updateChart-Europe'            }, {                'label': 'North America',                'value': '342947',                'link': 'j-updateChart-NA'            }, {                'label': 'South America',                'value': '183881',                'link': 'j-updateChart-SA'            }]        }"
        secondChartData = "{              'chart': {                             }         }"
        'create chart instance
        'chart type, chart id, width, height, data format, data source as string
        Dim firstChart As New Chart("column2d", "first_chart", "600", "400", "json", firstChartData)
        Dim secondChart As New Chart("column2d", "second_chart", "600", "400", "json", secondChartData)
        'render chart
        Literal1.Text = firstChart.Render()
        Literal2.Text = secondChart.Render()
    End Sub
End Class
