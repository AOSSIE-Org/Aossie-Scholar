<%@ Page Language="C#" AutoEventWireup="true" CodeFile="NumberFormatModule.aspx.cs" Inherits="Pages_NumberFormatModule" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Use of fusioncharts number module API</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
        function onRenderComplete(eventObj) {
            var formattedNumber = eventObj.sender.formatNumber(1234.5);
            document.getElementById("rendered").innerHTML = "format  1234.5 : " + formattedNumber;
            
        }
    </script>
    <form id="form1" runat="server">
        <h3>Use of fusioncharts number module API</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   <div>
        <p id ="rendered"></p>
    </div>
    
</body>
</html>
