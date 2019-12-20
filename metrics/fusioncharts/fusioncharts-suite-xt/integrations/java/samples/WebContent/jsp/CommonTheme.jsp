<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="java.util.*" %>
<%@page import="fusioncharts.FusionCharts" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<title>FusionCharts | Use of Common Theme</title>
<link href="../Styles/ChartSampleStyleSheet.css" rel="stylesheet" />
<script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.gammel.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.zune.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.carbon.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.ocean.js"></script>
</head>
<body>
<script type="text/javascript">
        FusionCharts && FusionCharts.ready(function () {
        	FusionCharts.options.defaultTheme="fusion";
            var trans = document.getElementById("controllers").getElementsByTagName("input");
            for (var i=0, len=trans.length; i<len; i++) {                
                if (trans[i].type == "radio"){
                    trans[i].onchange = function() {
                        ChangeTheme(this.value);
                    };
                }
            }
        });

        function ChangeTheme(theme) {
           /* for (var k in FusionCharts.items) {
                if (FusionCharts.items.hasOwnProperty(k)) {
                    FusionCharts.items[k].setChartAttribute('theme', theme);
                }
            } */
        	FusionCharts.options.defaultTheme=theme;
        };

   </script>
<h3>Use of Common Theme</h3>
<div style="width: 100%; display: table;">
        <div style="display: table-row">
            <div id="first_chart" style="width: 40%; display: table-cell;"></div>
            <div id="second_chart" style="width: 40%; display: table-cell;"></div>
        </div>
    </div>
    <br/>
    <br/>
    
    <div align="center" style="font-family:'Helvetica Neue', Arial; font-size: 16px;">
            <label style="padding: 0px 5px !important;">Select a theme for all charts</label>
    </div>
    <br/>
    <div id="controllers" align="center" style="font-family:'Helvetica Neue', Arial; font-size: 14px;">
        <label style="padding: 0px 5px !important;">
           <input type="radio" name="theme-options" checked value="fusion"/> Fusion
       </label>
       <label style="padding: 0px 5px !important;">
           <input type="radio" name="theme-options" value="gammel"/> Gammel
       </label>
       <label style="padding: 0px 5px !important;">
               <input type="radio" name="theme-options" value="zune"/> Zune
       </label>
       <label style="padding: 0px 5px !important;">
           <input type="radio" name="theme-options" value="carbon"/> Carbon
       </label>
       <label style="padding: 0px 5px !important;">
           <input type="radio" name="theme-options" value="ocean"/> Ocean
       </label>
    </div>
<div><span><a href="../Index.jsp">Go Back</a></span></div>
<%
String multiSeriesData = "{      'chart': {        'caption': 'App Publishing Trend',        'subCaption': '2012-2016',        'xAxisName': 'Years',        'yAxisName' : 'Total number of apps in store',        'formatnumberscale': '1',        'drawCrossLine':'1',        'plotToolText' : '<b>$dataValue</b> apps on $seriesName in $label'   },      'categories': [{        'category': [{          'label': '2012'        }, {          'label': '2013'        }, {          'label': '2014'        }, {          'label': '2015'        },{        'label': '2016'        }        ]      }],      'dataset': [{        'seriesname': 'iOS App Store',        'data': [{          'value': '125000'        }, {          'value': '300000'        }, {          'value': '480000'        }, {          'value': '800000'        }, {          'value': '1100000'        }]      }, {        'seriesname': 'Google Play Store',        'data': [{          'value': '70000'        }, {          'value': '150000'        }, {          'value': '350000'        }, {          'value': '600000'        },{          'value': '1400000'        }]      }, {        'seriesname': 'Amazon AppStore',        'data': [{          'value': '10000'        }, {          'value': '100000'        }, {          'value': '300000'        }, {          'value': '600000'        },{          'value': '900000'        }]      }]    }";
String singlesSeriesData = "{      'chart': {        'caption': 'Average Fastball Velocity',        'yAxisName' : 'Velocity (in mph)',        'subCaption': '[2005-2016]',        'numberSuffix': ' mph',        'rotateLabels': '1',        'setAdaptiveYMin': '1',     },      'data': [{        'label': '2005',        'value': '89.45'      }, {        'label': '2006',        'value': '89.87'      }, {        'label': '2007',        'value': '89.64'      }, {        'label': '2008',        'value': '90.13'      }, {        'label': '2009',        'value': '90.67'      }, {        'label': '2010',        'value': '90.54'      }, {        'label': '2011',        'value': '90.75'      }, {        'label': '2012',        'value': '90.8'      }, {        'label': '2013',        'value': '91.16'      }, {        'label': '2014',        'value': '91.37'      }, {        'label': '2015',        'value': '91.66'      }, {        'label': '2016',        'value': '91.8'      }, ]    }";
//Create chart instance
// charttype, chartID, width, height,containerid, data format, data
FusionCharts firstChart = new FusionCharts(
		  "overlappedcolumn2d", 
		  "overlappedcolumn_chart", 
		  "600",
		  "300", 
		  "first_chart",
		  "json", 
		  multiSeriesData
);
FusionCharts secondChart = new FusionCharts(
		  "column2d", 
		  "column_chart", 
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