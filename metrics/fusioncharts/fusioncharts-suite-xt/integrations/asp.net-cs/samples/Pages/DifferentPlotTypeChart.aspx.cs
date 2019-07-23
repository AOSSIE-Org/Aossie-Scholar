using FusionCharts.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Pages_DifferentPlotTypeChart : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/different-plot-type-for-each-variable-measure-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/different-plot-type-for-each-variable-measure-schema.json");
        }

        FusionTable fusionTable = new FusionTable(schema, data);
        TimeSeries timeSeries = new TimeSeries(fusionTable);

        timeSeries.AddAttribute("caption", @"{ 
                                        text: 'Sales Performance'
                                      }");

        timeSeries.AddAttribute("yAxis", @"[{
                                              plot: {
                                                value: 'Sale Amount',
                                                type: 'area'
                                              },
                                              title: 'Sale Amount',
                                              format: {
                                                prefix: '$'
                                              }
                                            }, {
                                              plot: {
                                                value: 'Units Sold',
                                                type: 'column'
                                              },
                                              title: 'Units Sold'
                                            }]");

        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}