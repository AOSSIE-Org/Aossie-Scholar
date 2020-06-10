using System;
using System.Text;
using System.Collections.Generic;
using FusionCharts.Charts;
using System.Net;

public partial class Pages_MultipleSeriesOnTimeAxis : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json");
        }

        FusionTable fusionTable = new FusionTable(schema, data);
        TimeSeries timeSeries = new TimeSeries(fusionTable);

        timeSeries.AddAttribute("caption", @"{ 
                                        text: 'Sales Analysis'
                                      }");

        timeSeries.AddAttribute("subcaption", @"{ 
                                        text: 'Grocery & Footwear'
                                      }");
        timeSeries.AddAttribute("series", "'Type'");

        timeSeries.AddAttribute("yAxis", @" [{
                                              plot: 'Sales Value',
                                              title: 'Sale Value',
                                              format: {
                                                prefix: '$'
                                              }
                                            }]");

        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}