<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="java.util.*" %>
<%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>FusionCharts | Customizing tooltip</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
</head>
<body>
<h3>Customizing tooltip</h3>
<div id="chartContainer"></div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
String jsonData = "{ \"chart\": { \"caption\": \"Top 3 Electronic Brands in Top 3 Revenue Earning States\", \"subcaption\": \"Last month\", \"aligncaptiontocanvas\": \"0\", \"yaxisname\": \"Statewise Sales (in %)\", \"xaxisname\": \"Brand\", \"numberprefix\": \"$\", \"showxaxispercentvalues\": \"1\", \"showsum\": \"1\", \"showPlotBorder\": \"1\",\"plottooltext\": \"<div id='nameDiv' style='font-size: 14px; border-bottom: 1px dashed #666666; font-weight:bold; padding-bottom: 3px; margin-bottom: 5px; display: inline-block;'>$label :</div>{br}State: <b>$seriesName</b>{br}Sales : <b>$dataValue</b>{br}Market share in State : <b>$percentValue</b>{br}Overall market share of $label: <b>$xAxisPercentValue</b>\", \"theme\": \"fusion\" }, \"categories\": [ { \"category\": [ { \"label\": \"Bose\" }, { \"label\": \"Dell\" }, { \"label\": \"Apple\" } ] } ], \"dataset\": [ { \"seriesname\": \"California\", \"data\": [ { \"value\": \"335000\" }, { \"value\": \"225100\" }, { \"value\": \"164200\" } ] }, { \"seriesname\": \"Washington\", \"data\": [ { \"value\": \"215000\" }, { \"value\": \"198000\" }, { \"value\": \"120000\" } ] }, { \"seriesname\": \"Nevada\", \"data\": [ { \"value\": \"298000\" }, { \"value\": \"109300\" }, { \"value\": \"153600\" } ] } ] }";
FusionCharts marimekko = new FusionCharts(
		  "marimekko",
	      "marimekko_chart",
	      "700", 
	      "400",
	      "chartContainer",
	      "json",
	      jsonData      		      
		);
%>
<%=marimekko.render()%>
</body>
</html>