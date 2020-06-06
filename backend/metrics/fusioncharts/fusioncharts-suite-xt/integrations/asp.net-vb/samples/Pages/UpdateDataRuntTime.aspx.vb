Imports FusionCharts.Charts
Partial Class Pages_UpdateDataRuntTime
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles MyBase.Load
        Dim jsonData As String = "{ 'chart': { 'caption': 'Customer Satisfaction Score', 'subcaption': 'Los Angeles Topanga', 'plotToolText': 'Current Score: $value', 'theme': 'fint', 'chartBottomMargin': '50', 'showValue': '1' }, 'colorRange': { 'color': [{ 'minValue': '0', 'maxValue': '45', 'code': '#e44a00' }, { 'minValue': '45', 'maxValue': '75', 'code': '#f8bd19' }, { 'minValue': '75', 'maxValue': '100', 'code': '#6baa01' }] }, 'dials': { 'dial': [{ 'value': '70', 'id': 'dial1' }] } }"
        Dim lineargauge As Chart = New Chart("angulargauge", "angular_gauge", "500", "400", "json", jsonData)
        Literal1.Text = lineargauge.Render()
    End Sub
End Class
