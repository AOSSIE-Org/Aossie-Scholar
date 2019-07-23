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
            FusionCharts && FusionCharts.ready(function () {
            var trans = document.getElementById("controllers").getElementsByTagName("input");
            for (var i=0, len=trans.length; i<len; i++) {                
                if (trans[i].type == "radio"){
                    trans[i].onchange = function() {
                        changeSize(this.value);
                    };
                }
            }
        });
        

        function changeSize(size) {
            document.getElementById('chartContainer').style.width =  size.split('x')[0] + 'px';
            document.getElementById('chartContainer').style.height = size.split('x')[1] + 'px';
        };
</script>

<h3>Dynamic Chart Resize</h3>
<div align="center">
    <label style="padding: 0px 5px !important;">Select Chart Container Size (in pixels)</label>
</div>
<br/>
<div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
    <label style="padding: 0px 5px !important;">
        <input type="radio" name="div-size" checked value="400x300"/>400x300 
    </label>
    <label style="padding: 0px 5px !important;">
        <input type="radio" name="div-size" value="600x500"/>600x500
    </label>
    <label style="padding: 0px 5px !important;">
            <input type="radio" name="div-size" value="800x600"/>800x600
    </label>
</div>


<div style="width: 100%; display: block;" align="center">
        <div id="chartContainer" style="border-style: solid;border-color:#5a5a5a;width: 400px; height: 300px;"></div>
</div>

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