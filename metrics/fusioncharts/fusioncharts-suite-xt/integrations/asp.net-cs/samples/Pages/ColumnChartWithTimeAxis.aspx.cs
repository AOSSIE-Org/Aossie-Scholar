using FusionCharts.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Pages_ColumnChartWithTimeAxis : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/column-chart-with-time-axis-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/column-chart-with-time-axis-schema.json");
        }

        FusionTable fusionTable = new FusionTable(schema, data);
        TimeSeries timeSeries = new TimeSeries(fusionTable);

        timeSeries.AddAttribute("chart", @"{ 
                                        showLegend: 0
                                      }");

        timeSeries.AddAttribute("caption", @"{ 
                                        text: 'Daily Visitors Count of a Website'
                                      }");

        timeSeries.AddAttribute("yAxis", @"[{
                                              plot: {
                                                value: 'Daily Visitors',
                                                type: 'column'
                                                },
                                              title: 'Daily Visitors (in thousand)'
                                            }]");

        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}