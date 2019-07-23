<%@ Page Language="VB" AutoEventWireup="false" CodeFile="GetDataSelectScatterChart.aspx.vb" Inherits="Pages_GetDataSelectScatterChart" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <link href="../Styles/SampleStyleSheet.css" rel="stylesheet" />
    <title>FusionCharts | Get data from select scatter chart and show them in tabular format</title>
</head>
<body>
    <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
   <script type="text/javascript" src="//cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
    <script>
        onRenderComplete = function (evtObj, argObj) {
            
            // creating div for controllers
            var controllers = document.createElement('div');
            controllers.setAttribute('id', 'controllers');
            controllers.style.display = "inline-block";
            controllers.innerHTML = "<div id='tableView-1' style='width:500px;display:none;margin-left:0px;max-height:250px;overflow:scroll;border: 1px solid #CCCCCC;margin: 3px;float: left;display:none; color: #666666;font-family:'Arial','Helvetica';font-size: 12px;'></div>";
            //Display container div and write table
            document.getElementById("showData").appendChild(controllers);
           // argObj.container.parentNode.insertBefore(controllers, argObj.container.nextSibling);
            /*
             * getDataFromChart method prepares the
             * tabular string from selection and
             * write in a div and display it.
             */
            evtObj.sender.getDataFromChart = function() {
                var i,
                    j,
                    str,
                    ds = "",
                    dataArr,
                    flagData = false,
                    objDataset = evtObj.sender.getJSONData && evtObj.sender.getJSONData().dataset,
                    tableContainer = document.getElementById("tableView-1");

                //Form tabular string
                str = "<div style='margin:3px;font-family:'Arial','Helvetica';font-size: 12px;'> Data is returned by the chart as Array. The data is converted into tabular format using JavaScript.</div>";
                str += '<table border="1" cellpadding="1" cellspacing="0" bordercolor="#ffffff" width="100%">';
                for (i in objDataset) {
                    dataArr = objDataset[i].data;
                    if (dataArr.length > 0) {
                        flagData = true;
                        str += '    <tr>';
                        str += '        <td width="20%" style="font-weight: bold;font-size: 14px;vertical-align: top;text-align:right;padding: 3px" color="' + objDataset[i].color + '">' + objDataset[i].seriesname + '</td>';

                        ds = '<table border="1" cellpadding="1" cellspacing="0" bordercolor="' + objDataset[i].color + '" width="100%">';
                        ds += '<tr>';
                        ds += '<td width="20%" style="font-weight: bold;font-size: 12px;background-color: #EEEEEE;text-align:center"> Id</td>';
                        ds += '<td width="40%" style="font-weight: bold;font-size: 12px;background-color: #EEEEEE;text-align:center"> Price (in USD)</td>';
                        ds += '<td width="40%" style="font-weight: bold;font-size: 12px;background-color: #EEEEEE;text-align:center"> Quantity Sold</td>';
                        ds += '</tr>';
                        for (j = 0; j < dataArr.length; j++) {
                            var id = String(dataArr[j].id),
                                price = String(dataArr[j].x),
                                qty = String(dataArr[j].y);

                            ds += '<tr>';
                            ds += '<td width="20%" align="center">' + id + '</td>';
                            ds += '<td width="40%" align="center">&#36;' + price + ' </td>';
                            ds += '<td width="40%" align="center">' + qty + ' units</td>';
                            ds += '</tr>';
                        }
                        ds += '</table>';
                        str += '        <td width="80%" style="padding: 3px">' + ds + '</td>';
                        str += '    </tr>';
                    }

                }
                str += '</table>';
                if (!flagData) {
                    str = "No Data Selected";
                }
                tableContainer.style.display = "block";
                tableContainer.innerHTML = str;
            }
        },
            onBeforeDataSubmit = function (evtObj, argObj) {
            
             evtObj.sender.getDataFromChart();
        },
            onDataRestored = function (evtObj, argObj) {
                
            document.getElementById("tableView-1").style.display = "none";
            document.getElementById("tableView-1").innerHTML = "";
        }
       
    </script>
    <form id="form1" runat="server">
        <h3>Get data from select scatter chart and show them in tabular format</h3>
        <div>
             <asp:Literal ID="Literal1" runat="server"></asp:Literal>     
        </div>
        <div id ="showData"></div>
        <div><span><asp:HyperLink id="hyperlink1" NavigateUrl="../Default.aspx" Text="Go Back" runat="server"/></span></div>
    </form>
   
    
</body>
</html>
