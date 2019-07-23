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
 <title>FusionCharts | Show data plot value on click</title>
</head>
<body>
<script>
        function onDataplotClick(eventObj) {
            var dataValue = eventObj.data.dataValue;
            var categoryLabel = eventObj.data.categoryLabel;

            document.getElementById("plotclick").innerHTML = "category: " + categoryLabel + "\n" + "value: " + dataValue;
            
        }
    </script>
   <h3>Show data plot value on click</h3>
    <div id ="chart"></div>
    <div>
            <p id="plotclick"></p>
        </div>
        <div><span><a href="../Index.jsp">Go Back</a></span></div>
    <%
        String jsonData;
        jsonData = "{      'chart': {        'caption': 'Countries With Most Oil Reserves [2017-18]',        'subCaption': 'In MMbbl = One Million barrels',        'xAxisName': 'Country',        'yAxisName': 'Reserves (MMbbl)',        'numberSuffix': 'K',        'theme': 'fusion',  },      'data': [{        'label': 'Venezuela',        'value': '290'      }, {        'label': 'Saudi',        'value': '260'      }, {        'label': 'Canada',        'value': '180'      }, {        'label': 'Iran',        'value': '140'      }, {        'label': 'Russia',        'value': '115'      }, {        'label': 'UAE',        'value': '100'      }, {        'label': 'US',        'value': '30'      }, {        'label': 'China',        'value': '30'      }]    }";
        FusionCharts column_chart = new FusionCharts(
    		  "column2d",
   		      "column_chart",
   		      "700", 
   		      "400",
   		      "chart",
   		      "json",
   		      jsonData      		      
    			);
      
 		column_chart.addEvent("dataplotClick", "onDataplotClick");
      
        %>
		<%=column_chart.render()%>
</body>
</html>