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
 <title>FusionCharts | update dial value on runtime</title>
</head>
<body>
 <script>
       updateData = function () {
           var value = document.getElementById("dial-val").value;
           FusionCharts("angular_gauge").setDataForId("dial1",value);
       }
   </script>
   <h3>update dial value on runtime</h3>
   <label for="dial-val">Input dial value</label>
        <input name="dial-val" id="dial-val" type= "number"/><input type ="button" name ="update dial" value ="update dial"onclick ="updateData()" />
        <br />
        <br />
    <div id ="gauge"></div>
    <div>
            <p id="plotclick"></p>
        </div>
        <div><span><a href="../Index.jsp">Go Back</a></span></div>
    <%
        String jsonData;
        jsonData = "{ 'chart': { 'caption': 'Customer Satisfaction Score', 'subcaption': 'Los Angeles Topanga', 'plotToolText': 'Current Score: $value', 'theme': 'fint', 'chartBottomMargin': '50', 'showValue': '1' }, 'colorRange': { 'color': [{ 'minValue': '0', 'maxValue': '45', 'code': '#e44a00' }, { 'minValue': '45', 'maxValue': '75', 'code': '#f8bd19' }, { 'minValue': '75', 'maxValue': '100', 'code': '#6baa01' }] }, 'dials': { 'dial': [{ 'value': '70', 'id': 'dial1' }] } }";
        FusionCharts angulargauge = new FusionCharts(
    		  "angulargauge",
   		      "angular_gauge",
   		      "500", 
   		      "400",
   		      "gauge",
   		      "json",
   		      jsonData      		      
    			);
      
    
      
        %>
		<%=angulargauge.render()%>
</body>
</html>