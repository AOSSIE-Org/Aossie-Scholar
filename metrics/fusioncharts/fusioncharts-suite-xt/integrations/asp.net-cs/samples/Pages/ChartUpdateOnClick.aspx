<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ChartUpdateOnClick.aspx.cs" Inherits="Pages_ChartUpdateOnClick" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Updating Different Chart</title>
</head>
<body>
      <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
     <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
     <script type="text/javascript">
        
        function updateChart(value) {
            var chartData = "";
            switch (value) {
                case 'Europe':
                    chartData = {
                                "chart": {
                                    "caption": "Sales by Country",
                                    "xaxisname": "Country",
                                    "yaxisname": "Total Sales",
                                    "numbersuffix": "K",
                                    "theme": "fusion"
                                },
                                "data": [{
                                    "label": "Austria",
                                    "value": "139488"
                                }, {
                                    "label": "Belgium",
                                    "value": "35132"
                                }, {
                                    "label": "Denmark",
                                    "value": "34779"
                                }, {
                                    "label": "Finland",
                                    "value": "19776"
                                }]
                            }
                    break;
            
                case 'NA':
                    chartData = {
                                "chart": {
                                    "caption": "Sales by Country",
                                    "xaxisname": "Country",
                                    "yaxisname": "Total Sales",
                                    "numbersuffix": "K",
                                    "theme": "fusion"
                                },
                                "data": [{
                                    "label": "Canada",
                                    "value": "55329",
                                }, {
                                    "label": "Mexico",
                                    "value": "24072",
                                }, {
                                    "label": "USA",
                                    "value": "263546",
                                }]
                            }
                    break;
                case 'SA':
                    chartData = {
                            "chart": {
                                "caption": "Sales by Country",
                                "xaxisname": "Country",
                                "yaxisname": "Total Sales",
                                "numbersuffix": "K",
                                "theme": "fusion"
                            },
                            "data": [{
                                "label": "Argentina",
                                "value": "8119"
                            }, {
                                "label": "Brazil",
                                "value": "114954"
                            }, {
                                "label": "Venezuela",
                                "value": "60806"
                            }]
                    }
                    break;
            } // switch ends

            FusionCharts.items["second_chart"].setJSONData(chartData);
        }

   </script>
    <form id="form1" runat="server">
        <asp:Table runat ="server" style="width: 100%;">
            <asp:TableRow>
                <asp:TableCell>
                    <asp:Literal ID="Literal1" runat="server"></asp:Literal>   
                </asp:TableCell>
                <asp:TableCell>
                    <asp:Literal ID="Literal2" runat="server"></asp:Literal>   
                </asp:TableCell>
            </asp:TableRow>
        </asp:Table>
         <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
</body>
</html>
