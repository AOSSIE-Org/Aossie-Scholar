using System;
using FusionCharts.Charts;

public partial class Pages_SpecialChartTypeAPI : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        //json data in string format
        string jsonData = "{ 'chart': { 'caption': 'Market Share of Web Servers', 'plottooltext': '<b>$percentValue</b> of web servers run on $label servers', 'showLegend': '0', 'enableMultiSlicing': '0', 'showPercentValues': '1', 'legendPosition': 'bottom', 'useDataPlotColorForLabels': '1', 'theme': 'fusion', }, 'data': [{ 'label': 'Apache', 'value': '32647479' }, { 'label': 'Microsoft', 'value': '22100932' }, { 'label': 'Zeus', 'value': '14376' }, { 'label': 'Other', 'value': '18674221' }] }";
        // create chart instance
        // parameter
        // chrat type, chart id, chart widh, chart height, data format, data source
        Chart column2d = new Chart("pie2d", "first_chart", "700", "400", "json", jsonData);
        //attach event 
        column2d.AddEvent("dataplotClick", "plotClickHandler");
        //render chart
        Literal1.Text = column2d.Render();
    }
}