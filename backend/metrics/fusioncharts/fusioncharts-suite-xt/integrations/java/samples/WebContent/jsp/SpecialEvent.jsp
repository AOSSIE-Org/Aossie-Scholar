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
 <title>FusionCharts | example of data update event</title>
</head>
<body>
<script>
        function onUpdate(eventObj) {
            document.getElementById("dataUpdate").innerHTML = "previous value: " + eventObj.data.prevData;
            
        }
    </script>
   <h3>example of data update event</h3>
    <div id ="gauge"></div>
     <div>
            <p id ="dataUpdate"></p>
        </div>
        <div><span><a href="../Index.jsp">Go Back</a></span></div>
    <%
        String jsonData;
        jsonData = "{ 'chart': { 'caption': 'Server CPU Utilization', 'subcaption': 'food.hsm.com', 'lowerLimit': '0', 'upperLimit': '100', 'numberSuffix': '%', 'valueAbovePointer': '0', 'editmode':'1' }, 'colorRange': { 'color': [ { 'minValue': '0', 'maxValue': '35', 'label': 'Low', 'code': '#1aaf5d' }, { 'minValue': '35', 'maxValue': '70', 'label': 'Moderate', 'code': '#f2c500' }, { 'minValue': '70', 'maxValue': '100', 'label': 'High', 'code': '#c02d00' } ] }, 'pointers': { 'pointer': [ { 'value': '72.5' } ] } }";
        FusionCharts hlineargauge = new FusionCharts(
    		  "hlineargauge",
   		      "hlinear_gauge",
   		      "500", 
   		      "150",
   		      "gauge",
   		      "json",
   		      jsonData      		      
    			);
      
        hlineargauge.addEvent("realtimeUpdateComplete", "onUpdate");
      
        %>
		<%=hlineargauge.render()%>
</body>
</html>