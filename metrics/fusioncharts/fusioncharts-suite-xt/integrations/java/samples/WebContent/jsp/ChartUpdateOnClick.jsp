<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>FusionCharts | Dynamic Chart Resize</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
</head>
<body>
<script type="text/javascript">
        
        function updateChart(value) {
            var chartData = "";
            switch (value) {
                case 'Europe':
                    chartData = {
                                "chart": {
                                    "caption": "Sales by Country",
                                    "xaxisname": "Country",
                                    "yaxisname": "Total Sales",
                                    "numbersuffix": "K",
                                    "theme": "fusion"
                                },
                                "data": [{
                                    "label": "Austria",
                                    "value": "139488"
                                }, {
                                    "label": "Belgium",
                                    "value": "35132"
                                }, {
                                    "label": "Denmark",
                                    "value": "34779"
                                }, {
                                    "label": "Finland",
                                    "value": "19776"
                                }]
                            }
                    break;
            
                case 'NA':
                    chartData = {
                                "chart": {
                                    "caption": "Sales by Country",
                                    "xaxisname": "Country",
                                    "yaxisname": "Total Sales",
                                    "numbersuffix": "K",
                                    "theme": "fusion"
                                },
                                "data": [{
                                    "label": "Canada",
                                    "value": "55329",
                                }, {
                                    "label": "Mexico",
                                    "value": "24072",
                                }, {
                                    "label": "USA",
                                    "value": "263546",
                                }]
                            }
                    break;
                case 'SA':
                    chartData = {
                            "chart": {
                                "caption": "Sales by Country",
                                "xaxisname": "Country",
                                "yaxisname": "Total Sales",
                                "numbersuffix": "K",
                                "theme": "fusion"
                            },
                            "data": [{
                                "label": "Argentina",
                                "value": "8119"
                            }, {
                                "label": "Brazil",
                                "value": "114954"
                            }, {
                                "label": "Venezuela",
                                "value": "60806"
                            }]
                    }
                    break;
            } // switch ends

            FusionCharts.items["second_column_chart"].setJSONData(chartData);
        }

   </script>

    <h3>Dynamic Chart Resize</h3>
    <table style="width: 100%;" >
        <tr>
            <td>
                <div id="first_chart"></div>
            </td>
            <td>
                <span>Click on the left chart to update this one</span>
                <div id="second_chart" ></div>
            </td>
        </tr>
    </table> 
    <br/>
    <br/>
    <br/>
<br/>
<br/>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
String multiSeriesData = "{            'chart': {                'caption': 'Sales by Region',                'xaxisname': 'Region',                'yaxisname': 'Total Sales',                'numbersuffix': 'K',                'theme': 'fusion'            },            'data': [{                'label': 'Europe',                'value': '827508',                'link': 'j-updateChart-Europe'            }, {                'label': 'North America',                'value': '342947',                'link': 'j-updateChart-NA'            }, {                'label': 'South America',                'value': '183881',                'link': 'j-updateChart-SA'            }]        }";
String singlesSeriesData = "{              'chart': {                             }         }";
//Create chart instance
// charttype, chartID, width, height,containerid, data format, data
FusionCharts firstChart = new FusionCharts(
		  "column2d", 
		  "first_column_chart", 
		  "600",
		  "300", 
		  "first_chart",
		  "json", 
		  multiSeriesData
);
FusionCharts secondChart = new FusionCharts(
		  "column2d", 
		  "second_column_chart", 
		  "600",
		  "300", 
		  "second_chart",
		  "json", 
		  singlesSeriesData
);
%>
<%=firstChart.render() %>
<%=secondChart.render() %>
</body>
</html>