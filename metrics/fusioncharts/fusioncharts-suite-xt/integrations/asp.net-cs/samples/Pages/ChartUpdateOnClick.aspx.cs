using System;
using FusionCharts.Charts;

public partial class Pages_ChartUpdateOnClick : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        // store chart data as json string
        string jsonDataFirstChart, jsonDataSecondChart;
        jsonDataFirstChart = "{            'chart': {                'caption': 'Sales by Region',                'xaxisname': 'Region',                'yaxisname': 'Total Sales',                'numbersuffix': 'K',                'theme': 'fusion'            },            'data': [{                'label': 'Europe',                'value': '827508',                'link': 'j-updateChart-Europe'            }, {                'label': 'North America',                'value': '342947',                'link': 'j-updateChart-NA'            }, {                'label': 'South America',                'value': '183881',                'link': 'j-updateChart-SA'            }]        }";
        jsonDataSecondChart = "{              'chart': {                             }         }";

        // Create chart instance for first chart
        Chart firstChart = new Chart("column2d", "first_chart", "600", "300", "json", jsonDataFirstChart);
        // create chart instance for second chart
        Chart secondChart = new Chart("column2d", "second_chart", "600", "300", "json", jsonDataSecondChart);
        // render first chart
        Literal1.Text = firstChart.Render();
        // render second chart
        Literal2.Text = secondChart.Render();
    }
}