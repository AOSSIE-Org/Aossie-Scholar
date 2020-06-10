<%@ Page Language="VB" AutoEventWireup="false" CodeFile="ProductLevelAPI.aspx.vb" Inherits="Pages_ProductLevelAPI" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <style>
    input[type=radio], input[type=checkbox] {
		display:none;
	}

    input[type=radio] + label, input[type=checkbox] + label {
		display:inline-block;
		margin:-2px;
		padding: 4px 12px;
		margin-bottom: 0;
		font-size: 14px;
		line-height: 20px;
		color: #333;
		text-align: center;
		text-shadow: 0 1px 1px rgba(255,255,255,0.75);
		vertical-align: middle;
		cursor: pointer;
		background-color: #f5f5f5;
		background-image: -moz-linear-gradient(top,#fff,#e6e6e6);
		background-image: -webkit-gradient(linear,0 0,0 100%,from(#fff),to(#e6e6e6));
		background-image: -webkit-linear-gradient(top,#fff,#e6e6e6);
		background-image: -o-linear-gradient(top,#fff,#e6e6e6);
		background-image: linear-gradient(to bottom,#fff,#e6e6e6);
		background-repeat: repeat-x;
		border: 1px solid #ccc;
		border-color: #e6e6e6 #e6e6e6 #bfbfbf;
		border-color: rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);
		border-bottom-color: #b3b3b3;
		filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff',endColorstr='#ffe6e6e6',GradientType=0);
		filter: progid:DXImageTransform.Microsoft.gradient(enabled=false);
		-webkit-box-shadow: inset 0 1px 0 rgba(255,255,255,0.2),0 1px 2px rgba(0,0,0,0.05);
		-moz-box-shadow: inset 0 1px 0 rgba(255,255,255,0.2),0 1px 2px rgba(0,0,0,0.05);
		box-shadow: inset 0 1px 0 rgba(255,255,255,0.2),0 1px 2px rgba(0,0,0,0.05);
	}

	 input[type=radio]:checked + label, input[type=checkbox]:checked + label{
		   background-image: none;
		outline: 0;
		-webkit-box-shadow: inset 0 2px 4px rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.05);
		-moz-box-shadow: inset 0 2px 4px rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.05);
		box-shadow: inset 0 2px 4px rgba(0,0,0,0.15),0 1px 2px rgba(0,0,0,0.05);
			background-color:#e0e0e0;
	}
    </style>
    <title>FusionCharts | Change chart properties dynamically</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
        changeCaption = function () {
            debugger;
          FusionCharts("first_chart").setChartAttribute('caption', 'Test Caption');
        }
        changeXAxisName = function(){
          FusionCharts("first_chart").setChartAttribute('xAxisName', 'Test X-Axis');
        }
        changeYAxisName = function(){
          FusionCharts("first_chart").setChartAttribute('yAxisName', 'Test Y-Axis');
        }
        resetChanges = function () {
            
          FusionCharts("first_chart").setChartAttribute('caption', 'Countries With Most Oil Reserves [2017-18]');
          FusionCharts("first_chart").setChartAttribute('xAxisName', 'Country');
          FusionCharts("first_chart").setChartAttribute('yAxisName', 'Reserves (MMbbl)');
        }
    </script>
    <form id="form1" runat="server">
        <h3>Change chart properties dynamically</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div>
            <p align="center" id ="message"></p>
        </div>

        <div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
            <input type="radio" id="radio1" name="radios" onclick="changeCaption()" />
            <label for="radio1">Change Caption: Test Caption</label>
            <input type="radio" id="radio2" name="radios" onclick="changeXAxisName()" />
            <label for="radio2">Change X-Axis Name: Test X-Axis</label>
            <input type="radio" id="radio3" name="radios" onclick="changeYAxisName()" />
            <label for="radio3">Change Y-Axis Name: Test Y-Axis</label>
            <input type="radio" id="radio4" name="radios"  onclick="resetChanges()" />
            <label for="radio4">Reset</label>
        </div> 
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
    
    
</body>
</html>
