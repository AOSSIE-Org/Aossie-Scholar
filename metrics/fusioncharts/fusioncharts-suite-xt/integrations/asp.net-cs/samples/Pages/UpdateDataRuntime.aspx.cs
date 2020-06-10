using System;
using FusionCharts.Charts;

public partial class Pages_UpdateDataRuntime : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        //json data in string format
        string jsonData = "{ 'chart': { 'caption': 'Customer Satisfaction Score', 'subcaption': 'Los Angeles Topanga', 'plotToolText': 'Current Score: $value', 'theme': 'fint', 'chartBottomMargin': '50', 'showValue': '1' }, 'colorRange': { 'color': [{ 'minValue': '0', 'maxValue': '45', 'code': '#e44a00' }, { 'minValue': '45', 'maxValue': '75', 'code': '#f8bd19' }, { 'minValue': '75', 'maxValue': '100', 'code': '#6baa01' }] }, 'dials': { 'dial': [{ 'value': '70', 'id': 'dial1' }] } }";
        // create chart instance
        // parameter
        // chrat type, chart id, chart widh, chart height, data format, data source
        Chart lineargauge = new Chart("angulargauge", "angular_gauge", "500", "400", "json", jsonData);
        
        //render chart
        Literal1.Text = lineargauge.Render();
    }
}