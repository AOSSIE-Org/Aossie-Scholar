<%@ Page Language="VB" AutoEventWireup="false" CodeFile="SpecialChartTypeAPI.aspx.vb" Inherits="Pages_SpecialChartTypeAPI" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | shocasing use special chart type API</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
         plotClickHandler = function(event){
            clickedPlot = (event.data.categoryLabel).toLowerCase();
              if (selectedItem !== clickedPlot) {
                    selectedItem = clickedPlot;
              } else{
                    selectedItem = 'none';
              }
        };
        selectedItem = "none";
        noneChecked = function(){
            FusionCharts("first_chart").slicePlotItem(0,false);
            FusionCharts("first_chart").slicePlotItem(1,false);
            FusionCharts("first_chart").slicePlotItem(2,false);
            FusionCharts("first_chart").slicePlotItem(3,false);
        }
        apacheChecked = function(){
            FusionCharts("first_chart").slicePlotItem(0,true);
        }
        microsoftChecked = function(){
            FusionCharts("first_chart").slicePlotItem(1,true);
        }
        zeusChecked = function(){
            FusionCharts("first_chart").slicePlotItem(2,true);
        }
        otherChecked = function(){
            FusionCharts("first_chart").slicePlotItem(3,true);
        }
    </script>
    <form id="form1" runat="server">
        <h3>shocasing use special chart type API</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
            <label style="padding: 0px 5px !important;">
                <input type="radio" name="rdGrp-options" checked="checked" onclick="noneChecked()"/> None
            </label>
            <label style="padding: 0px 5px !important;">
                <input type="radio" name="rdGrp-options" onclick="apacheChecked()"/> Apache
            </label>
            <label style="padding: 0px 5px !important;">
                    <input type="radio" name="rdGrp-options" onclick="microsoftChecked()"/> Microsoft
            </label>
            <label style="padding: 0px 5px !important;">
                <input type="radio" name="rdGrp-options" onclick="zeusChecked()"/> Zeus
            </label>
            <label style="padding: 0px 5px !important;">
                <input type="radio" name="rdGrp-options" onclick="otherChecked()"/> Other
            </label>        
        </div>
	<br/>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   
    
</body>
</html>
