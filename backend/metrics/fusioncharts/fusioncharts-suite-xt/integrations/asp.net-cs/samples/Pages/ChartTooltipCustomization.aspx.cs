using System;
using FusionCharts.Charts;

public partial class Pages_ChartTooltipCustomization : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        //json data in string format
        string jsonData = "{ 'chart': { 'caption': 'Top 3 Electronic Brands in Top 3 Revenue Earning States', 'subcaption': 'Last month', 'aligncaptiontocanvas': '0', 'yaxisname': 'Statewise Sales (in %)', 'xaxisname': 'Brand', 'numberprefix': '$', 'showxaxispercentvalues': '1', 'showsum': '1', 'showPlotBorder': '1', 'plottooltext': '<div id=\\'nameDiv\\' style=\\'font-size: 14px; border-bottom: 1px dashed #666666; font-weight:bold; padding-bottom: 3px; margin-bottom: 5px; display: inline-block;\\'>$label :</div>{br}State: <b>$seriesName</b>{br}Sales : <b>$dataValue</b>{br}Market share in State : <b>$percentValue</b>{br}Overall market share of $label: <b>$xAxisPercentValue</b>', 'theme': 'fusion' }, 'categories': [ { 'category': [ { 'label': 'Bose' }, { 'label': 'Dell' }, { 'label': 'Apple' } ] } ], 'dataset': [ { 'seriesname': 'California', 'data': [ { 'value': '335000' }, { 'value': '225100' }, { 'value': '164200' } ] }, { 'seriesname': 'Washington', 'data': [ { 'value': '215000' }, { 'value': '198000' }, { 'value': '120000' } ] }, { 'seriesname': 'Nevada', 'data': [ { 'value': '298000' }, { 'value': '109300' }, { 'value': '153600' } ] } ] }";
        // create chart instance
        // parameter
        // chrat type, chart id, chart widh, chart height, data format, data source
        Chart marimekko = new Chart("marimekko", "first_chart", "700", "400", "json", jsonData);
        //render chart
        Literal1.Text = marimekko.Render();
    }
}