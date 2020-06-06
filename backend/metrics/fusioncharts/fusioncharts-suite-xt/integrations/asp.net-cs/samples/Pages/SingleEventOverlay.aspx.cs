using FusionCharts.Charts;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Pages_SingleEventOverlay : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string schema, data;

        using (WebClient client = new WebClient())
        {
            data = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/single-event-overlay-data.json");
            schema = client.DownloadString("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/single-event-overlay-schema.json");
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
                                            start: 'Mar-1980',
                                            label: 'US inflation peaked at 14.8%.',
                                            timeFormat: ' % b -% Y',
                                            style: {
                                                marker:
                                                {
                                                    fill: '#D0D6F4'
                                                }
                                            }
                                        }, {
                                            start: 'May-1981',
                                            label: 'To control inflation, the Fed started {br} raising interest rates to over {br} 20%.',
                                            timeFormat: '%b-%Y'
                                            }, {
                                            start: 'Jun-1983',
                                            label: 'By proactive actions of Mr.Volcker, {br} the inflation falls to 2.4% {br} from the peak of over 14% {br} just three years ago.',
                                            timeFormat: '%b-%Y',
                                            style: {
                                                marker: {
                                                fill: '#D0D6F4'
                                                }
                                            }
                                            }, {
                                            start: 'Oct-1987',
                                            label: 'The Dow Jones Industrial Average lost {br} about 30% of it’s value.',
                                            timeFormat: '%b-%Y',
                                            style: {
                                                marker: {
                                                fill: '#FBEFCC'
                                                }
                                            }
                                            }, {
                                            start: 'Jan-1989',
                                            label: 'George H.W. Bush becomes {br} the 41st president of US!',
                                            timeFormat: '%b-%Y'
                                            }, {
                                            start: 'Aug-1990',
                                            label: 'The oil prices spiked to $35 {br} per barrel from $15 per barrel {br} because of the Gulf War.',
                                            timeFormat: '%b-%Y'
                                            }, {
                                            start: 'Dec-1996',
                                            label: 'Alan Greenspan warns of the dangers {br} of ""irrational exuberance"" in financial markets, {br} an admonition that goes unheeded',
                                            timeFormat: '%b-%Y'
                                            }, {
                                            start: 'Sep-2008',
                                            label: 'Lehman Brothers collapsed!',
                                            timeFormat: '%b-%Y'
                                            },{
                                            start: 'Mar-2009',
                                            label: 'The net worth of US households {br} stood at a trough of $55 trillion.',
                                            timeFormat: '%b-%Y',
                                            style: {
                                                marker: {
                                                fill: '#FBEFCC'
                                                }
                                            }
                                            }, {
                                            start: 'Oct-2009',
                                            label: 'Unemployment rate peaked {br} in given times to 10%.',
                                            timeFormat: '%b-%Y'
                                            }]
                                        }");


        // charttype, chartID, width, height, data format, TimeSeries object
        Chart chart = new Chart("timeseries", "first_chart", "800", "550", "json", timeSeries);
        Literal1.Text = chart.Render();
    }
}