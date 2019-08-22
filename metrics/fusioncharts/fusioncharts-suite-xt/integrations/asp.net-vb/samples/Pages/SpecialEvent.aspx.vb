Imports FusionCharts.Charts
Partial Class Pages_SpecialEvent
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles MyBase.Load
        Dim jsonData As String = "{ 'chart': { 'caption': 'Server CPU Utilization', 'subcaption': 'food.hsm.com', 'lowerLimit': '0', 'upperLimit': '100', 'numberSuffix': '%', 'valueAbovePointer': '0', 'editmode':'1' }, 'colorRange': { 'color': [ { 'minValue': '0', 'maxValue': '35', 'label': 'Low', 'code': '#1aaf5d' }, { 'minValue': '35', 'maxValue': '70', 'label': 'Moderate', 'code': '#f2c500' }, { 'minValue': '70', 'maxValue': '100', 'label': 'High', 'code': '#c02d00' } ] }, 'pointers': { 'pointer': [ { 'value': '72.5' } ] } }"
        Dim lineargauge As Chart = New Chart("hlineargauge", "horizontal_lineargauge", "500", "150", "json", jsonData)
        lineargauge.AddEvent("realtimeUpdateComplete", "onUpdate")
        Literal1.Text = lineargauge.Render()
    End Sub
End Class
