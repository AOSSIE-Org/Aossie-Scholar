<%@ page language="java" contentType="text/html;" pageEncoding="utf-8"  %>
<%@page import="java.util.*" %>
<%@page import="fusioncharts.FusionCharts" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;">
<title>FusionCharts | use of different languages</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
</head>
<body>
<h3>use of different languages</h3>
<div id="chartContainer"></div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
String jsonData = "{    \"chart\": {        \"caption\": \"سوبرماركت هاري\",        \"subCaption\": \"الإيرادات الشهرية للعام الماضي\",        \"xAxisName\": \"الشهر\",        \"yAxisName\": \"كمية\",        \"numberPrefix\": \"$\",        \"theme\": \"fusion\",        \"rotateValues\": \"1\",        \"exportEnabled\": \"1\"    },    \"data\": [{            \"label\": \"يناير\",            \"value\": \"420000\"        },        {            \"label\": \"فبراير\",            \"value\": \"810000\"        },        {            \"label\": \"مارس\",            \"value\": \"720000\"        },        {            \"label\": \"أبريل\",            \"value\": \"550000\"        },        {            \"label\": \"مايو\",            \"value\": \"910000\"        },        {            \"label\": \"يونيو\",            \"value\": \"510000\"        },        {            \"label\": \"يوليو\",            \"value\": \"680000\"        },        {            \"label\": \"أغسطس\",            \"value\": \"620000\"        },        {            \"label\": \"سبتمبر\",            \"value\": \"610000\"        },        {            \"label\": \"أكتوبر\",            \"value\": \"490000\"        },        {            \"label\": \"نوفمبر\",            \"value\": \"900000\"        },        {            \"label\": \"ديسمبر\",            \"value\": \"730000\"        }    ]}";
FusionCharts column = new FusionCharts(
		  "column2d",
	      "column_chart",
	      "700", 
	      "400",
	      "chartContainer",
	      "json",
	      jsonData
		);
%>
<%=column.render()%>
</body>
</html>