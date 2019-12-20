using FusionCharts.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Pages_PlottingTwoVariables : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-two-variable-measures-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-two-variable-measures-schema.json");
        }

        FusionTable fusionTable = new FusionTable(schema, data);
        TimeSeries timeSeries = new TimeSeries(fusionTable);

        timeSeries.AddAttribute("caption", @"{ 
                                        text: 'Cariaco Basin Sampling'
                                      }");

        timeSeries.AddAttribute("subcaption", @"{ 
                                        text: 'Analysis of O₂ Concentration and Surface Temperature'
                                      }");

        timeSeries.AddAttribute("yAxis", @"[{
												plot: [{
													value: 'O2 concentration',
													connectNullData: true
												}],
												min: '3',
												max: '6',
												title: 'O₂ Concentration (mg/L)'  
											}, {
												plot: [{
													value: 'Surface Temperature',
													connectNullData: true
												}],
												min: '18',
												max: '30',
												title: 'Surface Temperature (°C)'
											}]");

        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}