using System;
using FusionCharts.Charts;

public partial class Pages_ChartSpclChar : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        //xml data in string format
        string xmlData = "<chart caption='Harry&#39;s SuperMart' subcaption='Monthly revenue for last year' xaxisname='Month' yaxisname='Amount' numberprefix='¥' theme='fusion' rotatevalues='1' exportenabled='1'> <set label='Jan' value='420000' /> <set label='Feb' value='810000' /> <set label='Mar' value='720000' /> <set label='Apr' value='550000' /> <set label='May' value='910000' /> <set label='Jun' value='510000' /> <set label='Jul' value='680000' /> <set label='Aug' value='620000' /> <set label='Sep' value='610000' /> <set label='Oct' value='490000' /> <set label='Nov' value='900000' /> <set label='Dec' value='730000' /> </chart>";
        // create chart instance
        // parameter
        // chrat type, chart id, chart widh, chart height, data format, data source
        Chart column2d = new Chart("column2d", "first_chart", "700", "400", "xml", xmlData);
        //render chart
        Literal1.Text = column2d.Render();
    }
}