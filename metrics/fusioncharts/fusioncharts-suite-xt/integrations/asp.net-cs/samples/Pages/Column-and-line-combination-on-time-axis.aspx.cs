using FusionCharts.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Pages_Column_and_line_combination_on_time_axis : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {            
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/column-line-combination-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/column-line-combination-schema.json");
        }

        FusionTable fusionTable = new FusionTable(schema, data);
        TimeSeries timeSeries = new TimeSeries(fusionTable);

        timeSeries.AddAttribute("caption", @"{ 
                                        text: 'Web visits & downloads'
                                      }");

        timeSeries.AddAttribute("subcaption", @"{ 
                                        text: 'since 2015'
                                      }");

        timeSeries.AddAttribute("yAxis", @"[{
                                              plot: [{
                                                    value: 'Downloads',
                                                    type: 'column'
                                                  }, {
                                                    value: 'Web Visits',
                                                    type: 'line'
                                                  }]
                                            }]");

        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}