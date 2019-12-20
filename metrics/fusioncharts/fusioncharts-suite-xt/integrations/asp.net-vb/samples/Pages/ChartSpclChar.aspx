<%@ Page Language="VB" AutoEventWireup="false" CodeFile="ChartSpclChar.aspx.vb" Inherits="Pages_ChartSpclChar" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
     <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Chart using special character in XML data format</title>
</head>
<body>
     <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <h3>Chart using special character in XML data format</h3>
    <form id="form1" runat="server">
        <div>
            <asp:Literal ID="Literal1" runat="server"></asp:Literal>   
        </div>
         <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
</body>
</html>
