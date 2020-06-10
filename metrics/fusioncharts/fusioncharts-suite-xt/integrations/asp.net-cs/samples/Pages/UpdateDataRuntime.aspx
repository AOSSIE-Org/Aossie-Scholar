<%@ Page Language="C#" AutoEventWireup="true" CodeFile="UpdateDataRuntime.aspx.cs" Inherits="Pages_UpdateDataRuntime" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | update dial value on runtime</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
   <script>
       updateData = function () {
           var value = document.getElementById("dial-val").value;
           FusionCharts("angular_gauge").setDataForId("dial1",value);
       }
   </script>
    <form id="form1" runat="server">
        <h3>update dial value on runtime</h3>
        <label for="dial-val">Input dial value</label>
        <input name="dial-val" id="dial-val" type= "number"/><input type ="button" name ="update dial" value ="update dial"onclick ="updateData()" />
        <br />
        <br />
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   
    
</body>
</html>
