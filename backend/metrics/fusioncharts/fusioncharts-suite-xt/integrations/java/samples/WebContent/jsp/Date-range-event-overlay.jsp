<%@page import="java.io.InputStreamReader"%>
<%@page import="java.io.InputStream"%>
<%@page import="java.io.BufferedReader"%>
<%@page import="java.net.URLConnection"%>
<%@page import="java.net.URL"%>
<%@ page language="java" contentType="text/html; charset=utf-8"%>
<%@page import="java.util.*" %>
<%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>FusionCharts | Simple FusionTime Chart</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>

</head>
<body>
<h3>Date range event overlay</h3>
<div id="chart-container"></div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
	<%!    
		public String getContent(String url) throws Exception {
			URL website = new URL(url);
			URLConnection connection = website.openConnection();
			BufferedReader in = new BufferedReader(
                    new InputStreamReader(
                            connection.getInputStream()));
			
	        StringBuilder response = new StringBuilder();
	        String inputLine;
	
	        while ((inputLine = in.readLine()) != null) {
	            response.append(inputLine);
	        }
	        
	        in.close();
	
	        return response.toString();
	    }
    %>
    
	<%
		String data = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/date-range-event-overlay-data.json");
		String schema = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/date-range-event-overlay-schema.json");
					
		FusionCharts.FusionTable fusionTable = new FusionCharts.FusionTable(schema, data);		
		FusionCharts.TimeSeries timeSeries = new FusionCharts.TimeSeries(fusionTable);	

		timeSeries.AddAttribute("caption", "{"
					+ "text: 'Interest Rate Analysis'"
			  	+ "}");

		timeSeries.AddAttribute("subCaption", "{"
							+ "text: 'Federal Reserve (USA)'"
						  + "}");

		timeSeries.AddAttribute("yAxis", "[{"
								  + "plot: 'Interest Rate',"
								  + "format:{"
									+ "suffix: '%'"
								  + "},"
								  + "title: 'Interest Rate'"
							+ "}]");

		timeSeries.AddAttribute("xAxis", "{"
							  + "plot: 'Time',"
							  + "timemarker: [{"
								+ "start: 'Jul-1981',"
								+ "end: 'Nov-1982',"
								+ "label: 'Economic downturn was triggered by {br} tight monetary policy in an effort to {br} fight mounting inflation.',"
								+ "timeFormat: '%b-%Y'"
							  + "},{"
								+ "start: 'Jul-1990',"
								+ "end: 'Mar-1991',"
								+ "label: 'This eight month recession period {br} was characterized by a sluggish employment recovery, {br} most commonly referred to as a jobless recovery.',"
								+ "timeFormat: '%b-%Y'"
							  + "}, {"
								+ "start: 'Jun-2004',"
								+ "end: 'Jul-2006',"
								+ "label: 'The Fed after raising interest rates {br} at 17 consecutive meetings, ends its campaign {br} to slow the economy and forestall inflation.',"
								+ "timeFormat: '%b-%Y'"
							  + "}, {"
								+ "start: 'Dec-2007',"
								+ "end: 'Jun-2009',"
								+ "label: 'Recession caused by the worst {br} collapse of financial system in recent {br} times.',"
								+ "timeFormat: '%b-%Y'"
							  + "}]"
							+ "}");
	
	    FusionCharts chart = new FusionCharts(
	  			  "timeSeries",
	 		      "mychart",
	 		      "700", 
	 		      "450",
	 		      "chart-container",
	 		      "json",
	 		     timeSeries
	 		      );
	 	
     %>
     <%=chart.render()%>
</body>
</html>	