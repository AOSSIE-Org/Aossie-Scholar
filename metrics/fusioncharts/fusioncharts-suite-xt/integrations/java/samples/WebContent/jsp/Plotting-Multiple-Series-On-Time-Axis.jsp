<%@page import="java.io.InputStreamReader"%>
<%@page import="java.io.InputStream"%>
<%@page import="java.io.BufferedReader"%>
<%@page import="java.net.URLConnection"%>
<%@page import="java.net.URL"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
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
<h3>Plotting multiple series on time axis</h3>
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
		String data = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json");
		String schema = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json");
					
		FusionCharts.FusionTable fusionTable = new FusionCharts.FusionTable(schema, data);		
		FusionCharts.TimeSeries timeSeries = new FusionCharts.TimeSeries(fusionTable);
		
		timeSeries.AddAttribute("caption", "{" 
				+ "text: 'Sales Analysis'"
				+ "}");

		timeSeries.AddAttribute("subcaption", "{"
				+ "text: 'Grocery & Footwear'"
				+ "}");
			  
		timeSeries.AddAttribute("series", "'Type'");

		timeSeries.AddAttribute("yAxis", " [{"
						+ "plot: 'Sales Value',"
						+ "title: 'Sale Value',"
						+ "format: {"
						+ "prefix: '$'"
						+ "}"
						+ "}]");
		
	    FusionCharts chart = new FusionCharts(
	  			  "timeSeries",
	 		      "mychart",
	 		      "700", 
	 		      "450",
	 		      "chart-container",
	 		      "jSon",
	 		     timeSeries
	 		      );
	 	
     %>
     <%=chart.render()%>
</body>
</html>	