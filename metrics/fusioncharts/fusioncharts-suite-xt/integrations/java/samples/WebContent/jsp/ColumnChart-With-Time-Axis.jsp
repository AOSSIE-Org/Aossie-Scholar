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
<h3>Column chart with time axis</h3>
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
		String data = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/column-chart-with-time-axis-data.json");
		String schema = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/column-chart-with-time-axis-schema.json");
					
		FusionCharts.FusionTable fusionTable = new FusionCharts.FusionTable(schema, data);		
		FusionCharts.TimeSeries timeSeries = new FusionCharts.TimeSeries(fusionTable);	

		timeSeries.AddAttribute("chart", "{" 
				+ "showLegend: 0"
			    + "}");

		timeSeries.AddAttribute("caption", "{ "
				+ "text: 'Daily Visitors Count of a Website'"
				+ "}");		
		
		timeSeries.AddAttribute("yAxis", "[{"
							  + "plot: {"
								+ "value: 'Daily Visitors',"
								+ "type: 'column'"
								+ "},"
							  + "title: 'Daily Visitors (in thousand)'"
							+ "}]");
						
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