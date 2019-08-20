<%@ Page Language="C#" AutoEventWireup="true" CodeFile="SpecialEvent.aspx.cs" Inherits="Pages_SpecialEvent" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | example of data update event</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
        function onUpdate(eventObj) {
            document.getElementById("dataUpdate").innerHTML = "previous value: " + eventObj.data.prevData;
            
        }
    </script>
    <form id="form1" runat="server">
        <h3>example of data update event</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div>
            <p id ="dataUpdate"></p>
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   
  </body>  
</html>
