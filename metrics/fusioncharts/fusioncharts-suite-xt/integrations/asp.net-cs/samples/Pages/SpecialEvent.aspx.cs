using System;
using FusionCharts.Charts;

public partial class Pages_SpecialEvent : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        //json data in string format
        string jsonData = "{ 'chart': { 'caption': 'Server CPU Utilization', 'subcaption': 'food.hsm.com', 'lowerLimit': '0', 'upperLimit': '100', 'numberSuffix': '%', 'valueAbovePointer': '0', 'editmode':'1' }, 'colorRange': { 'color': [ { 'minValue': '0', 'maxValue': '35', 'label': 'Low', 'code': '#1aaf5d' }, { 'minValue': '35', 'maxValue': '70', 'label': 'Moderate', 'code': '#f2c500' }, { 'minValue': '70', 'maxValue': '100', 'label': 'High', 'code': '#c02d00' } ] }, 'pointers': { 'pointer': [ { 'value': '72.5' } ] } }";
        // create chart instance
        // parameter
        // chrat type, chart id, chart widh, chart height, data format, data source
        Chart lineargauge = new Chart("hlineargauge", "horizontal_lineargauge", "500", "150", "json", jsonData);
        //attach event 
        lineargauge.AddEvent("realtimeUpdateComplete", "onUpdate");
        //render chart
        Literal1.Text = lineargauge.Render();
    }
}