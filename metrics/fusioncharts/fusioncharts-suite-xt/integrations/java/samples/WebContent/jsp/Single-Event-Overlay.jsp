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
<h3>Single event overlay</h3>
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
		String data = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/single-event-overlay-data.json");
		String schema = getContent("https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/single-event-overlay-schema.json");
					
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

	 	timeSeries.AddAttribute("xAxis", "{"
						+ "plot: 'Time',"
						+ "timemarker: [{"
						+ "start: 'Mar-1980',"
						+ "label: 'US inflation peaked at 14.8%.',"
						+ "timeFormat: ' % b -% Y',"
						+ "style: {"
							+ "marker:"
								+ "{"
									+ "fill: '#D0D6F4'"
								+ "}"
						+ "}"
					+ "}, {"
						+ "start: 'May-1981',"
						+ "label: 'To control inflation, the Fed started {br} raising interest rates to over {br} 20%.',"
						+ "timeFormat: '%b-%Y'"
					+ "}, {"
						+ "start: 'Jun-1983',"
						+ "label: 'By proactive actions of Mr.Volcker, {br} the inflation falls to 2.4% {br} from the peak of over 14% {br} just three years ago.',"
						+ "timeFormat: '%b-%Y',"
						+ "style: {"
							+ "marker: {"
									+ "fill: '#D0D6F4'"
								+ "}"
						+ "}"
					+ "}, {"
						+ "start: 'Oct-1987',"
						+ "label: 'The Dow Jones Industrial Average lost {br} about 30% of it’s value.',"
						+ "timeFormat: '%b-%Y',"
						+ "style: {"
							+ "marker: {"
								+ "fill: '#FBEFCC'"
							+ "}"
						+ "}"
					+ "}, {"
						+ "start: 'Jan-1989',"
						+ "label: 'George H.W. Bush becomes {br} the 41st president of US!',"
						+ "timeFormat: '%b-%Y'"
					+ "}, {"
						+ "start: 'Aug-1990',"
						+ "label: 'The oil prices spiked to $35 {br} per barrel from $15 per barrel {br} because of the Gulf War.',"
						+ "timeFormat: '%b-%Y'"
					+ "}, {"
						+ "start: 'Dec-1996',"
						+ "label: 'Alan Greenspan warns of the dangers {br} of \"irrational exuberance\" in financial markets, {br} an admonition that goes unheeded',"
						+ "timeFormat: '%b-%Y'"
					+ "}, {"
						+ "start: 'Sep-2008',"
						+ "label: 'Lehman Brothers collapsed!',"
						+ "timeFormat: '%b-%Y'"
					+ "},{"
						+ "start: 'Mar-2009',"
						+ "label: 'The net worth of US households {br} stood at a trough of $55 trillion.',"
						+ "timeFormat: '%b-%Y',"
						+ "style: {"
							+ "marker: {"
								+ "fill: '#FBEFCC'"
							+ "}"
						+ "}"
					+ "}, {"
						+ "start: 'Oct-2009',"
						+ "label: 'Unemployment rate peaked {br} in given times to 10%.',"
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