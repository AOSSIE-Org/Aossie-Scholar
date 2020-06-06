Imports FusionCharts.Charts
Partial Class Pages_SpecialChartTypeAPI
    Inherits System.Web.UI.Page
    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles MyBase.Load
        Dim jsonData As String = "{ 'chart': { 'caption': 'Market Share of Web Servers', 'plottooltext': '<b>$percentValue</b> of web servers run on $label servers', 'showLegend': '0', 'enableMultiSlicing': '0', 'showPercentValues': '1', 'legendPosition': 'bottom', 'useDataPlotColorForLabels': '1', 'theme': 'fusion', }, 'data': [{ 'label': 'Apache', 'value': '32647479' }, { 'label': 'Microsoft', 'value': '22100932' }, { 'label': 'Zeus', 'value': '14376' }, { 'label': 'Other', 'value': '18674221' }] }"
        Dim column2d As Chart = New Chart("pie2d", "first_chart", "700", "400", "json", jsonData)
        column2d.AddEvent("dataplotClick", "plotClickHandler")
        Literal1.Text = column2d.Render()
    End Sub
End Class
