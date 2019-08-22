<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
 <title>FusionCharts | shocasing use special chart type API</title>
 
</head>
<body>
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
            FusionCharts("pie_chart").slicePlotItem(0,false);
            FusionCharts("pie_chart").slicePlotItem(1,false);
            FusionCharts("pie_chart").slicePlotItem(2,false);
            FusionCharts("pie_chart").slicePlotItem(3,false);
        }
        apacheChecked = function(){
            FusionCharts("pie_chart").slicePlotItem(0,true);
        }
        microsoftChecked = function(){
            FusionCharts("pie_chart").slicePlotItem(1,true);
        }
        zeusChecked = function(){
            FusionCharts("pie_chart").slicePlotItem(2,true);
        }
        otherChecked = function(){
            FusionCharts("pie_chart").slicePlotItem(3,true);
        }
    </script>
   <h3>shocasing use special chart type API</h3>
    <div id ="chart"></div>
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
        <div><span><a href="../Index.jsp">Go Back</a></span></div>
    <%
        String jsonData;
        jsonData = "{ 'chart': { 'caption': 'Market Share of Web Servers', 'plottooltext': '<b>$percentValue</b> of web servers run on $label servers', 'showLegend': '0', 'enableMultiSlicing': '0', 'showPercentValues': '1', 'legendPosition': 'bottom', 'useDataPlotColorForLabels': '1', 'theme': 'fusion', }, 'data': [{ 'label': 'Apache', 'value': '32647479' }, { 'label': 'Microsoft', 'value': '22100932' }, { 'label': 'Zeus', 'value': '14376' }, { 'label': 'Other', 'value': '18674221' }] }";
        FusionCharts pie_chart = new FusionCharts(
    		  "pie2d",
   		      "pie_chart",
   		      "700", 
   		      "400",
   		      "chart",
   		      "json",
   		      jsonData      		      
    			);
      
 	     
        %>
		<%=pie_chart.render()%>
</body>
</html>