Imports FusionCharts.Charts

Partial Class Pages_ChartLanguage
    Inherits System.Web.UI.Page

    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles MyBase.Load
        Dim jsonData As String = "{ 'chart': { 'caption': 'سوبرماركت هاري',         'subcaption': 'الإيرادات الشهرية للعام الماضي',         'xaxisname': 'الشهر',         'yaxisname': 'كمية',         'numberprefix': '$',         'theme': 'fusion',         'rotatevalues': '1',         'exportenabled': '1'     },     'data': [         {             'label': 'يناير',             'value': '420000'         },         {             'label': 'فبراير',             'value': '810000'         },         {             'label': 'مارس',             'value': '720000'         },         {             'label': 'أبريل',             'value': '550000'         },         {             'label': 'مايو',             'value': '910000'         },         {             'label': 'يونيو',             'value': '510000'         },         {             'label': 'يوليو',             'value': '680000'         },         {             'label': 'أغسطس',             'value': '620000'         },         {             'label': 'سبتمبر',             'value': '610000'         },         {             'label': 'أكتوبر',             'value': '490000'         },         {             'label': 'نوفمبر',             'value': '900000'         },         {             'label': 'ديسمبر',             'value': '730000'         }     ] }"
        Dim column2d As Chart = New Chart("column2d", "first_chart", "700", "400", "json", jsonData)
        Literal1.Text = column2d.Render()
    End Sub
End Class
