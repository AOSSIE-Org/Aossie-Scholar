<%@ Page Language="VB" AutoEventWireup="false" CodeFile="InteractiveEvent.aspx.vb" Inherits="Pages_InteractiveEvent" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Show data plot value on click</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
        function onDataplotClick(eventObj) {
            var dataValue = eventObj.data.dataValue;
            var categoryLabel = eventObj.data.categoryLabel;

            document.getElementById("plotclick").innerHTML = "category: " + categoryLabel + "\n" + "value: " + dataValue;
            
        }
    </script>
    <form id="form1" runat="server">
        <h3>Show data plot value on click</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div>
            <p id="plotclick"></p>
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   
    
</body>
</html>
