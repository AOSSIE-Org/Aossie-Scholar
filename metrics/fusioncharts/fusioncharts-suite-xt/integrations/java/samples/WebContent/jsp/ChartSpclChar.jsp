<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="java.util.*" %>
<%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>FusionCharts | use of special character</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
</head>
<body>
<h3>use of special character</h3>
<div id="chartContainer"></div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
String xmlData;
xmlData = "<chart caption=\"Harry&apos;s SuperMart\" subcaption=\"Monthly revenue for last year\" xaxisname=\"Month\" yaxisname=\"Amount\" numberprefix=\"¥\" theme=\"fusion\" rotatevalues=\"1\" exportenabled=\"1\">";
xmlData += "<set label=\"Jan\" value=\"420000\" />";
xmlData += "<set label=\"Feb\" value=\"810000\" />";
xmlData += "<set label=\"Mar\" value=\"720000\" />";
xmlData += "<set label=\"Apr\" value=\"550000\" />";
xmlData += "<set label=\"May\" value=\"910000\" />";
xmlData += "<set label=\"Jun\" value=\"510000\" />";
xmlData += "<set label=\"Jul\" value=\"680000\" />";
xmlData += "<set label=\"Aug\" value=\"620000\" />";
xmlData += "<set label=\"Sep\" value=\"610000\" />";
xmlData += "<set label=\"Oct\" value=\"490000\" />";
xmlData += "<set label=\"Nov\" value=\"900000\" />";
xmlData += "<set label=\"Dec\" value=\"730000\" />";
xmlData += "</chart>";
FusionCharts column2d = new FusionCharts(
		  "column2d",
	      "column2d_chart",
	      "700", 
	      "400",
	      "chartContainer",
	      "xml",
	      xmlData      		      
		);
%>
<%=column2d.render()%>
</body>
</html>