Imports FusionCharts.Charts
Partial Class Pages_ChartMessageExample
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles MyBase.Load
        Dim jsonData As String = "{      'chart': {        'caption': 'Countries With Most Oil Reserves [2017-18]',        'subCaption': 'In MMbbl = One Million barrels',        'xAxisName': 'Country',        'yAxisName': 'Reserves (MMbbl)',        'numberSuffix': 'K',        'theme': 'fusion',  'exportEnabled':'1'    },      'data': [{        'label': 'Venezuela',        'value': '290'      }, {        'label': 'Saudi',        'value': '260'      }, {        'label': 'Canada',        'value': '180'      }, {        'label': 'Iran',        'value': '140'      }, {        'label': 'Russia',        'value': '115'      }, {        'label': 'UAE',        'value': '100'      }, {        'label': 'US',        'value': '30'      }, {        'label': 'China',        'value': '30'      }]    }"
        Dim column2d As Chart = New Chart("column2d", "first_chart", "700", "400", "json", jsonData)
        column2d.AddMessage("loadMessage", "please wait data is being loaded")
        column2d.AddMessage("loadMessageFontSize", "18")
        Literal1.Text = column2d.Render()
    End Sub
End Class
