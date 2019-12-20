Imports FusionCharts.Charts

Partial Class Pages_ChartSpclChar
    Inherits System.Web.UI.Page

    Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs) Handles MyBase.Load
        Dim xmlData As String = "<chart caption='Harry&#39;s SuperMart' subcaption='Monthly revenue for last year' xaxisname='Month' yaxisname='Amount' numberprefix='¥' theme='fusion' rotatevalues='1' exportenabled='1'> <set label='Jan' value='420000' /> <set label='Feb' value='810000' /> <set label='Mar' value='720000' /> <set label='Apr' value='550000' /> <set label='May' value='910000' /> <set label='Jun' value='510000' /> <set label='Jul' value='680000' /> <set label='Aug' value='620000' /> <set label='Sep' value='610000' /> <set label='Oct' value='490000' /> <set label='Nov' value='900000' /> <set label='Dec' value='730000' /> </chart>"
        Dim column2d As Chart = New Chart("column2d", "first_chart", "700", "400", "xml", xmlData)
        Literal1.Text = column2d.Render()
    End Sub
End Class
