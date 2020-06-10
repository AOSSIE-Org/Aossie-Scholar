<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ProductLifeCycleEvent.aspx.cs" Inherits="Pages_ProductLifeCycleEvent" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | sample to showcase one product life cycle event attachment</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
        function onDataLoaded() {
            document.getElementById("dataLoaded").innerHTML = "chart data is loaded succesfully";
            
        }
    </script>
    <form id="form1" runat="server">
        <h3>sample to showcase one product life cycle event attachment</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div>
            <p id ="dataLoaded"></p>
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   
    
</body>
</html>
