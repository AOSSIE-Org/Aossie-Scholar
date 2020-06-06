<%@ Page Language="VB" AutoEventWireup="false" CodeFile="DynamicChartTypeChange.aspx.vb" Inherits="Pages_DynamicChartTypeChange" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Chart Type Change At Runtime (client-side)</title>
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
                        changeChartType(this.value);
                    };
                }
            }
        });
        

        function changeChartType(chartType) {
            for (var k in FusionCharts.items) {
                if (FusionCharts.items.hasOwnProperty(k)) {
                    FusionCharts.items[k].chartType(chartType);
                }
            }
        };
    </script>
    <h3>Chart Type Change At Runtime</h3>
    <div align="center">
        <label style="padding: 0px 5px !important;">Select The Chart Type</label>
    </div>
    <br/>
    <div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
        <label style="padding: 0px 5px !important;">
            <input type="radio" name="div-size" checked value="column2d"/>Column 2D 
        </label>
        <label style="padding: 0px 5px !important;">
            <input type="radio" name="div-size" value="pie3d"/>Pie 3D
        </label>
        <label style="padding: 0px 5px !important;">
                <input type="radio" name="div-size" value="bar2d"/>Bar 2D
        </label>
    </div>
    <form id="form1" runat="server">
        
        <div style="width: 100%; display: block;" align="center">
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
</body>
</html>
