<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>FusionCharts | Using Annotations On Chart</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
</head>
<body>
<h3>Using Annotations On Chart</h3>
<div id="chart"></div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
        String jsonData;
        jsonData = "{            'chart': {                'caption': 'Bakersfield Central - Total footfalls',                'subCaption': 'Last week',                'xAxisName': 'Day',                'yAxisName': 'No. of Visitors (In 1000s)',                'showValues': '0',                'theme': 'fusion'            },        'annotations':{            'groups': [                {                    'id': 'anchor-highlight',                    'items': [                        {                            'id': 'high-star',                            'type': 'circle',                            'x': '$dataset.0.set.2.x',                            'y': '$dataset.0.set.2.y',                            'radius': '12',                            'color': '#6baa01',                            'border': '2',                            'borderColor': '#f8bd19'                        },                        {                            'id': 'label',                            'type': 'text',                            'text': 'Highest footfall 25.5K',                            'fillcolor': '#6baa01',                            'rotate': '90',                            'x': '$dataset.0.set.2.x+75',                            'y': '$dataset.0.set.2.y-2'                        }                    ]                }            ]        },            'data': [                {                    'label': 'Mon',                    'value': '15123'                },                {                    'label': 'Tue',                    'value': '14233'                },                {                    'label': 'Wed',                    'value': '25507'                },                {                    'label': 'Thu',                    'value': '9110'                },                {                    'label': 'Fri',                    'value': '15529'                },                {                    'label': 'Sat',                    'value': '20803'                },                {                    'label': 'Sun',                    'value': '19202'                }            ]        }";
        FusionCharts column_chart = new FusionCharts(
    		  "column2d",
   		      "column_chart",
   		      "700", 
   		      "400",
   		      "chart",
   		      "json",
   		      jsonData      		      
    			);
      %>
 
		<%=column_chart.render()%>
</body>
</html>