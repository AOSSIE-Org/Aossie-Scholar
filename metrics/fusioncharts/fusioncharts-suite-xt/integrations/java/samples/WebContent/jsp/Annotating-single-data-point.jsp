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
<h3>Annotating single data point</h3>
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
		String data = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/annotating-single-data-point-data.json");
		String schema = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/annotating-single-data-point-schema.json");
					
		FusionCharts.FusionTable fusionTable = new FusionCharts.FusionTable(schema, data);		
		FusionCharts.TimeSeries timeSeries = new FusionCharts.TimeSeries(fusionTable);	

		timeSeries.AddAttribute("caption", "{ "
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
		
		timeSeries.AddAttribute("dataMarker", "[{"
		                    + "seriesName: 'Interest Rate',"
		                    + "time: 'Mar-1980',"
		                    + "identifier: 'H',"
		                    + "timeFormat: '%b-%Y',"
		                    + "tooltext: 'As a part of credit control program, under the leadership of Paul Volcker, the Fed tightened the money supply, allowing the federal fund rates to approach 20 percent.'"
		                 + "}, {"
		                    + "seriesName: 'Interest Rate',"
		                    + "time: 'Aug-1982',"
		                    + "identifier: 'L',"
		                    + "timeFormat: '%b-%Y',"
		                    + "tooltext: 'The FED eases off the monetary brakes, allowing interest rates to fall and the economy to begin a strong recovery.'"
		                 + "}, {"
	                		 + "seriesName: 'Interest Rate',"
	                		 + "time: 'Oct-1987',"
	                		 + "identifier: 'L',"
	                		 + "timeFormat: '%b-%Y',"
	                		 + "tooltext: 'The FED is forced to ease rate after the stock market crash.'"
		                 + "}, {"
	                		 + "seriesName: 'Interest Rate',"
	                		 + "time: 'May-1989',"
	                		 + "identifier: 'H',"
	                		 + "timeFormat: '%b-%Y',"
	                		 + "tooltext: 'Liquidity problem forced the Fed to increase rate to nearly 10%.'"
	                 	 + "}, {"
	                		 + "seriesName: 'Interest Rate',"
	                		 + "time: 'Sept-1992',"
	                		 + "identifier: 'L',"
	                		 + "timeFormat: '%b-%Y',"
	                		 + "tooltext: 'To fight the jobless economy growth the Fed had to reduce the interest rate to 3%.'"
	               	 	 + "}, {"
	               	 		+ "seriesName: 'Interest Rate',"
	               	 		+ "time: 'Jun-2003',"
	               	 		+ "identifier: 'L',"
	               	 		+ "timeFormat: '%b-%Y',"
	               			+ "tooltext: 'Struggling to revive the economy, the FED cuts it’s benchmark rate to 1%.'"
	               		 + "}, {"
               				+ "seriesName: 'Interest Rate',"
               				+ "time: 'Sep-2007',"
               				+ "identifier: 'L',"
               				+ "timeFormat: '%b-%Y',"
               				+ "tooltext: 'Fed started reducing the Federal Fund Rate.'"
               			 + "}, {"
		                	  + "seriesName: 'Interest Rate',"
		                	  + "time: 'Dec-2008',"
		                	  + "identifier: 'L',"
		                	  + "timeFormat: '%b-%Y',"
		                	  + "tooltext: 'Fed reduced the interest rates to sub 0.25% to manage the menace of longest economic downturn since World War 2'"
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