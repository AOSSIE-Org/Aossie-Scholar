<%@ Page Language="VB" AutoEventWireup="false" CodeFile="RenderCharWithPercentageWidthHeight.aspx.vb" Inherits="Pages_RenderCharWithPercentageWidthHeight" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Chart Auto Resize Sample</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script type="text/javascript">
            FusionCharts && FusionCharts.ready(function () {
            var trans = document.getElementById("controllers").getElementsByTagName("input");
            for (var i=0, len=trans.length; i<len; i++) {                
                if (trans[i].type == "radio"){
                    trans[i].onchange = function() {
                        changeSize(this.value);
                    };
                }
            }
        });
        

        function changeSize(size) {
            document.getElementById('chartContainer').style.width =  size.split('x')[0] + 'px';
            document.getElementById('chartContainer').style.height = size.split('x')[1] + 'px';
        };
    </script>
    <h3>Chart Auto Resize Sample</h3>
    <div align="center">
        <label style="padding: 0px 5px !important;">Select Chart Container Size (in pixels)</label>
    </div>
    <br/>
    <div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
        <label style="padding: 0px 5px !important;">
            <input type="radio" name="div-size" checked value="400x300"/>400x300 
        </label>
        <label style="padding: 0px 5px !important;">
            <input type="radio" name="div-size" value="600x500"/>600x500
        </label>
        <label style="padding: 0px 5px !important;">
                <input type="radio" name="div-size" value="800x600"/>800x600
        </label>
    </div>
    <form id="form1" runat="server">
        
        <div id="chartContainer" style="border-style: solid;border-color:#5a5a5a;width: 400px; height: 300px;" align="center">
             <asp:Literal ID="Literal1" runat="server" ></asp:Literal>     
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
</body>
</html>
