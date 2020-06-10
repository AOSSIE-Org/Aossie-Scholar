using FusionCharts.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Pages_Date_range_event_overlay : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/date-range-event-overlay-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/date-range-event-overlay-schema.json");
        }

        FusionTable fusionTable = new FusionTable(schema, data);
        TimeSeries timeSeries = new TimeSeries(fusionTable);

        timeSeries.AddAttribute("caption", @"{ 
                                        text: 'Interest Rate Analysis'
                                      }");

        timeSeries.AddAttribute("subCaption", @"{ 
                                        text: 'Federal Reserve (USA)'
                                      }");

        timeSeries.AddAttribute("yAxis", @"[{
                                              plot: 'Interest Rate',
                                              format:{
                                                suffix: '%'
                                              },
                                              title: 'Interest Rate'
                                            }]");

        timeSeries.AddAttribute("xAxis", @"{
                                          plot: 'Time',
                                          timemarker: [{
                                            start: 'Jul-1981',
                                            end: 'Nov-1982',
                                            label: 'Economic downturn was triggered by {br} tight monetary policy in an effort to {br} fight mounting inflation.',
                                            timeFormat: '%b-%Y'
                                          }, {
                                            start: 'Jul-1990',
                                            end: 'Mar-1991',
                                            label: 'This eight month recession period {br} was characterized by a sluggish employment recovery, {br} most commonly referred to as a jobless recovery.',
                                            timeFormat: '%b-%Y'
                                          }, {
                                            start: 'Jun-2004',
                                            end: 'Jul-2006',
                                            label: 'The Fed after raising interest rates {br} at 17 consecutive meetings, ends its campaign {br} to slow the economy and forestall inflation.',
                                            timeFormat: '%b-%Y'
                                          }, {
                                            start: 'Dec-2007',
                                            end: 'Jun-2009',
                                            label: 'Recession caused by the worst {br} collapse of financial system in recent {br} times.',
                                            timeFormat: '%b-%Y'
                                          }]
                                        }");


        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}