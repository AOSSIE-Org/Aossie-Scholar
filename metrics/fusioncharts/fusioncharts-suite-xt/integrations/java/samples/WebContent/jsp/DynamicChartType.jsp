<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
     <%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>FusionCharts | Chart type Change at Runtime</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
</head>
<body>
<script type="text/javascript">
            FusionCharts && FusionCharts.ready(function () {
            var trans = document.getElementById("controllers").getElementsByTagName("input");
            for (var i=0, len=trans.length; i<len; i++) {                
                if (trans[i].type == "radio"){
                    trans[i].onchange = function() {
                        changeChartType(this.value);
                    };
                }
            }
        });
        

        function changeChartType(chartType) {
            for (var k in FusionCharts.items) {
                if (FusionCharts.items.hasOwnProperty(k)) {
                    FusionCharts.items[k].chartType(chartType);
                }
            }
        };
</script>

<h3>Chart type Change at Runtime</h3>
<div align="center">
    <label style="padding: 0px 5px !important;">Select The Chart Type</label>
</div>
<br/>
<div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
    <label style="padding: 0px 5px !important;">
        <input type="radio" name="div-size" checked value="column2d"/>Column 2D 
    </label>
    <label style="padding: 0px 5px !important;">
        <input type="radio" name="div-size" value="pie3d"/>Pie 3D
    </label>
    <label style="padding: 0px 5px !important;">
            <input type="radio" name="div-size" value="bar2d"/>Bar 2D
    </label>
</div>


<div id="chartContainer" style="width: 100%; display: block;" align="center"></div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
        String jsonData;
        jsonData = "{      'chart': {        'caption': 'Countries With Most Oil Reserves [2017-18]',        'subCaption': 'In MMbbl = One Million barrels',        'xAxisName': 'Country',        'yAxisName': 'Reserves (MMbbl)',        'numberSuffix': 'K',        'theme': 'fusion'},      'data': [{        'label': 'Venezuela',        'value': '290'      }, {        'label': 'Saudi',        'value': '260'      }, {        'label': 'Canada',        'value': '180'      }, {        'label': 'Iran',        'value': '140'      }, {        'label': 'Russia',        'value': '115'      }, {        'label': 'UAE',        'value': '100'      }, {        'label': 'US',        'value': '30'      }, {        'label': 'China',        'value': '30'      }]    }";
        FusionCharts column_chart = new FusionCharts(
    		  "column2d",
   		      "column_chart",
   		      "700", 
   		      "400",
   		      "chartContainer",
   		      "json",
   		      jsonData      		      
    			);
      %>
 
		<%=column_chart.render()%>

</body>
</html>