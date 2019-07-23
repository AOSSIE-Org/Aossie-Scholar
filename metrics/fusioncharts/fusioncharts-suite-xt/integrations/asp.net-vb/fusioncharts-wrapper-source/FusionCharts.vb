Imports Microsoft.VisualBasic

Imports System.Text
Imports System.Collections
Imports System.Web.UI.WebControls
Imports System.Web
Imports System.Collections.Generic
Imports System.Globalization

Namespace FusionCharts.Charts
    ''' <summary>
    ''' Contains static methods to render FusionCharts in the Page. 
    ''' </summary>
    Public Class Chart
        'Implements System.ICloneable
        Private __CONFIG__ As Hashtable = Nothing
        Private Shared __PARAMMAP__ As Hashtable = Nothing
        Private events As String = ""

        ''' <summary>
        ''' User configurable chart parameter list 
        ''' </summary>
        Public Enum ChartParameter
            chartType
            chartId
            chartWidth
            chartHeight
            dataFormat
            dataSource
            renderAt
            bgColor
            bgOpacity
        End Enum

        ''' <summary>
        ''' List of supported data formats
        ''' </summary>
        Public Enum DataFormat
            json
            jsonurl
            xml
            xmlurl
            csv
        End Enum

#Region "constructor methods"
        ''' <summary>
        ''' Chart constructor
        ''' Chart configuration parameters can be supplyed to the constructor also.
        ''' </summary>
        Public Sub New()
            __INIT()
        End Sub


        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        Public Sub New(chartType As String)
            __INIT()

            SetChartParameter("type", chartType)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        Public Sub New(chartType As String, chartId As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("id", chartId)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        Public Sub New(chartType As String, chartId As String, chartWidth As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        Public Sub New(chartType As String, chartId As String, chartWidth As String, chartHeight As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        Public Sub New(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <param name="dataSource">Data for the chart</param>
        Public Sub New(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String, dataSource As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetData(dataSource)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <param name="dataSource">Data for the chart</param>
        ''' <param name="bgColor">Background color of the chart container</param>
        Public Sub New(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String, dataSource As String, _
            bgColor As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetData(dataSource)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
            SetChartParameter("containerBackgroundColor", bgColor)
        End Sub

        ''' <summary>
        ''' Chart constructor
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <param name="dataSource">Data for the chart</param>
        ''' <param name="bgColor">Back-ground-color of the chart container</param>
        ''' <param name="bgOpacity">Background opacity of the chart container</param>
        Public Sub New(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String, dataSource As String, _
            bgColor As String, bgOpacity As String)
            __INIT()

            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetData(dataSource)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
            SetChartParameter("containerBackgroundColor", bgColor)
            SetChartParameter("containerBackgroundOpacity", bgOpacity)
        End Sub
#End Region

#Region "RenderALL methods"

        ''' <summary>
        ''' Generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>
        Private Function RenderChartALL() As String

            Dim dataSource As String = GetChartParameter("dataSource")
            Dim dataFormat As String = GetChartParameter("dataFormat")
            Dim chartId As String = GetChartParameter("id")
            Dim renderAt As String = GetChartParameter("renderAt")



            Dim builder As New StringBuilder()
            builder.AppendFormat("<!-- Using ASP.NET FusionCharts Wrapper and JavaScript rendering --><!-- START Script Block for Chart {0} -->" + Environment.NewLine, chartId)
            ' if the user has provided renderAt then assume that the HTML container is already present in the page.
            If renderAt.Trim().Length = 0 Then
                renderAt = chartId & Convert.ToString("_div")
                ' Now create the container div also.
                builder.AppendFormat("<div id='{0}' >" + Environment.NewLine, renderAt)
                builder.Append("Chart..." + Environment.NewLine)
                builder.Append("</div>" + Environment.NewLine)
            End If

            Dim chartConfigJSON As String = fc_encodeJSON(GetConfigurationGroup("params"), True)

            ' Removes the extra trailing commas in generated JavaScript Object
            Dim Place As Integer = chartConfigJSON.LastIndexOf(","c)
            chartConfigJSON = If((Place >= 0), chartConfigJSON.Remove(Place, 1).Insert(Place, ""), chartConfigJSON)

            builder.Append("<script type=""text/javascript"">" + Environment.NewLine)
            builder.Append("FusionCharts && FusionCharts.ready(function () {" + Environment.NewLine)
            builder.AppendFormat("if (FusionCharts(""{0}"") ) FusionCharts(""{0}"").dispose();" & vbLf, chartId)
            builder.AppendFormat("var chart_{0} = new FusionCharts({1}).render();" + Environment.NewLine, chartId, chartConfigJSON)
            builder.Append(events)
            builder.Append("});" + Environment.NewLine)
            builder.Append("</script>" + Environment.NewLine)
            builder.AppendFormat("<!-- END Script Block for Chart {0} -->" + Environment.NewLine, chartId)

            Return builder.ToString()

        End Function

#End Region

#Region "Public Methods"
		' <summary>
        ' public method to attach event from client side
        ' </summary>
        ' <param name="eventName"></param>
        ' <param name="funcName"></param>
        Public Sub AddEvent(ByVal eventName As String, ByVal funcName As String)
            Dim eventHTML As String
            Dim chartId As String = GetChartParameter("id")
            eventHTML = String.Format("FusionCharts(""{0}"").addEventListener(""{1}"",{2});" & Environment.NewLine, chartId, eventName, funcName)
            events += eventHTML
        End Sub
		' <summary>
        ' public method to add attributes for message customization
        ' </summary>
        ' <param name="messageAttribute"></param>
        ' <param name="messageAttributeValue"></param>
        Public Sub AddMessage(ByVal messageAttribute As String, ByVal messageAttributeValue As String)
            Dim messageHTML As String
            messageHTML = String.Format("{0}:""{1}"",", messageAttribute, messageAttributeValue)
            SetChartParameter("message", messageHTML)
        End Sub
        ''' <summary>
        ''' Public method to clone an exiting FusionCharts instance
        ''' To make the chartId unique, this function will add "_clone" as suffix in the clone chart's Id.
        ''' </summary>
        Public Function Clone() As Object
            Dim ChartClone As New Chart()
            ChartClone.__CONFIG__ = DirectCast(Me.__CONFIG__.Clone(), Hashtable)
            ChartClone.SetChartParameter("id", DirectCast(ChartClone.__CONFIG__("params"), Hashtable)("id").ToString() + "_clone")

            Return ChartClone
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>
        Public Function Render() As String
            Return RenderChartALL()
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String) As String
            SetChartParameter("type", chartType)

            Return RenderChartALL()
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("id", chartId)

            Return RenderChartALL()
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String, chartWidth As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)

            Return RenderChartALL()
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String, chartWidth As String, chartHeight As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)

            Return RenderChartALL()
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)

            Return RenderChartALL()
        End Function

        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <param name="dataSource">Data for the chart</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String, dataSource As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetData(dataSource)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)

            Return RenderChartALL()
        End Function


        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <param name="dataSource">Data for the chart</param>
        ''' <param name="bgColor">Background color of the chart container</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String, dataSource As String, _
            bgColor As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetData(dataSource)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
            SetChartParameter("containerBackgroundColor", bgColor)

            Return RenderChartALL()
        End Function


        ''' <summary>
        ''' Public method to generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartType">The type of chart that you intend to plot</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="dataFormat">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        ''' <param name="dataSource">Data for the chart</param>
        ''' <param name="bgColor">Background color of the chart container</param>
        ''' <param name="bgOpacity">Background opacity of the chart container</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>

        Public Function Render(chartType As String, chartId As String, chartWidth As String, chartHeight As String, dataFormat As String, dataSource As String, _
            bgColor As String, bgOpacity As String) As String
            SetChartParameter("type", chartType)
            SetChartParameter("dataFormat", dataFormat)
            SetData(dataSource)
            SetChartParameter("id", chartId)
            SetChartParameter("width", chartWidth)
            SetChartParameter("height", chartHeight)
            SetChartParameter("containerBackgroundColor", bgColor)
            SetChartParameter("containerBackgroundOpacity", bgOpacity)

            Return RenderChartALL()
        End Function





        ''' <summary>
        ''' SetChartParameter sets various configurations of a FusionCharts instance
        ''' </summary>
        ''' <param name="param">Name of chart parameter</param>
        ''' <param name="value">Value of chart parameter</param>
        Public Sub SetChartParameter(param As ChartParameter, value As Object)

            SetChartParameter(__PARAMMAP__(param.ToString()).ToString(), value)
        End Sub

        ''' <summary>
        ''' GetChartParameter returns the value of a parameter of a FusionCharts instance
        ''' </summary>
        ''' <param name="param">Name of chart parameter</param>
        ''' <returns>String</returns>

        Public Function GetChartParameter(param As ChartParameter) As String
            Return GetChartParameter(__PARAMMAP__(param.ToString()).ToString())
        End Function

        ''' <summary>
        ''' This method to set the data for the chart
        ''' </summary>
        ''' <param name="dataSource">Data for the chart</param>

        Public Sub SetData(dataSource As String)
            SetChartParameter("dataSource", dataSource)
        End Sub

        ''' <summary>
        ''' This method to set the data for the chart
        ''' </summary>
        ''' <param name="dataSource">Data for the chart</param>
        ''' <param name="format">Data format. e.g. json, jsonurl, csv, xml, xmlurl</param>
        Public Sub SetData(dataSource As String, format As DataFormat)
            SetChartParameter("dataSource", dataSource)
            SetChartParameter("dataFormat", format.ToString())
        End Sub

#End Region



#Region "Helper Private Methods"

        ''' <summary>
        ''' SetConfiguration sets various configurations of FusionCharts
        ''' It takes configuration names as first parameter and its value a second parameter
        ''' There are config groups which can contain common configuration names. All config names in all groups gets set with this value
        ''' unless group is specified explicitly
        ''' </summary>
        ''' <param name="setting">Name of configuration</param>
        ''' <param name="value">Value of configuration</param>
        Private Sub SetChartParameter(setting As String, value As Object)
            If DirectCast(__CONFIG__("params"), Hashtable).ContainsKey(setting) Then
                If setting.Equals("message", StringComparison.InvariantCultureIgnoreCase) Then
                    DirectCast(__CONFIG__("params"), Hashtable)(setting) += value.ToString()
                Else
                    DirectCast(__CONFIG__("params"), Hashtable)(setting) = value
                End If
            End If
        End Sub


        Private Sub SetParamsMap()
            If __PARAMMAP__ Is Nothing Then
                __PARAMMAP__ = New Hashtable(StringComparer.InvariantCultureIgnoreCase)
                __PARAMMAP__("chartType") = "type"
                __PARAMMAP__("chartId") = "id"
                __PARAMMAP__("chartWidth") = "width"
                __PARAMMAP__("chartHeight") = "height"
                __PARAMMAP__("message") = "message"
                __PARAMMAP__("dataFormat") = "dataFormat"
                __PARAMMAP__("dataSource") = "dataSource"
                __PARAMMAP__("renderAt") = "renderAt"
                __PARAMMAP__("bgColor") = "containerBackgroundColor"
                __PARAMMAP__("bgOpacity") = "containerBackgroundOpacity"
            End If

        End Sub

        Private Sub __INIT()
            __CONFIG__ = New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            Dim param As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            param("type") = ""
            param("width") = ""
            param("height") = ""
            param("message") = ""
            param("renderAt") = ""
            param("dataSource") = ""
            param("dataFormat") = ""
            param("id") = Guid.NewGuid().ToString().Replace("-", "_")
            param("containerBackgroundColor") = ""
            param("containerBackgroundOpacity") = ""

            __CONFIG__("params") = param

            param = Nothing
            SetParamsMap()
        End Sub



        ''' <summary>
        ''' Transform the meaning of boolean value in integer value
        ''' </summary>
        ''' <param name="value">true/false value to be transformed</param>
        ''' <returns>1 if the value is true, 0 if the value is false</returns>
        Private Shared Function boolToNum(value As Boolean) As Integer
            Return If(value, 1, 0)
        End Function


        Private Function GetChartParameter(setting As String) As String
            If DirectCast(__CONFIG__("params"), Hashtable).ContainsKey(setting) Then
                Return DirectCast(__CONFIG__("params"), Hashtable)(setting).ToString()
            End If
            Return Nothing
        End Function


        Private Function fc_encodeJSON(json As Hashtable, enclosed As Boolean) As String
            Dim strjson As String = "", Key As String = "", Value As String = ""

            For Each ds As DictionaryEntry In json
                If ds.Value.ToString().Trim() <> "" Then
                    Key = ds.Key.ToString()
                    Value = ds.Value.ToString()
                    ' If this is not the dataSource then convert the value as JavaScript string
                    If Key.ToLower().Equals("datasource") Then
                        ' Remove new line char from the dataSource
                        Value.Replace(vbLf & vbCr, "")
                        ' detect if non-JSON format then wrap with quot '"'
                        If Not (Value.StartsWith("{") AndAlso Value.EndsWith("}")) Then
                            Value = (Convert.ToString("""") & Value) + """"
                        End If
                        strjson = (Convert.ToString((Convert.ToString(strjson + Environment.NewLine & Convert.ToString("""")) & Key) + """ : ") & Value) + ", "
                    ElseIf Key.ToLower().Equals("message") Then
                        strjson = strjson + Environment.NewLine + Value.ToString()

                    Else
                        Value = (Convert.ToString("""") & Value) + """"
                        strjson = (Convert.ToString((Convert.ToString(strjson + Environment.NewLine & Convert.ToString("""")) & Key) + """ : ") & Value) + ", "
                    End If

                ElseIf ds.Key.ToString().Equals("renderAt") Then
                    strjson = (strjson + Environment.NewLine & Convert.ToString("""renderAt"" : """)) + DirectCast(json, Hashtable)("id").ToString() + "_div"", "
                End If
            Next
            ' remove ending comma
            If strjson.EndsWith(",") Then
                strjson = strjson.Remove(strjson.Length - 1)
            End If

            If enclosed = True Then
                strjson = (Convert.ToString("{") & strjson) + Environment.NewLine + "}"
            End If

            Return strjson
        End Function

        Private Function GetConfigurationGroup(setting As String) As Hashtable
            If __CONFIG__.ContainsKey(setting) Then
                Return DirectCast(__CONFIG__(setting), Hashtable)
            End If
            Return Nothing
        End Function

#End Region

    End Class
End Namespace



Namespace InfoSoftGlobal
    ''' <summary>
    ''' Contains static methods to render FusionCharts in the Page.
    ''' 
    ''' @version: v3.2.2.2 
    ''' @date: 15 August 2012
    ''' 
    ''' </summary>
    Public Class FusionCharts

        'private static Hashtable __CONFIG__ = new Hashtable(new CaseInsensitiveHashCodeProvider(), new CaseInsensitiveComparer());
        Private Shared __CONFIG__ As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
        Private Shared __CONFIG__Initialized As Boolean = False

#Region "RenderALL methods"

        ''' <summary>
        ''' Generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <param name="allowTransparent">Whether allowTransparent chart (true / false)</param>
        ''' <param name="bgColor">Back Ground Color</param>
        ''' <param name="scaleMode">Set Scale Mode</param>
        ''' <param name="language">Set SWF file Language</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>
        Private Shared Function RenderChartALL(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean, allowTransparent As Boolean, bgColor As String, scaleMode As String, language As String) As String
            __INIT()

            ' Creating a local copy of global Configuration.
            Dim __CONFIGCLONE__ As Hashtable = DirectCast(__CONFIG__.Clone(), Hashtable)

            ' string dataprovider_js_code;
            SetConfiguration(__CONFIGCLONE__, "debugMode", boolToNum(debugMode))
            SetConfiguration(__CONFIGCLONE__, "registerWithJS", boolToNum(True))

            ' setup debug mode js parameter
            Dim debugMode_js_param As Integer = boolToNum(debugMode)
            ' setup register with js js parameter
            Dim registerWithJS_js_param As Integer = boolToNum(True)
            Dim dataFormat As String = GetConfiguration(__CONFIGCLONE__, "dataFormat")
            dataFormat = (If(dataFormat = "", "xml" + (If(dataStr = "", "url", "")), dataFormat & Convert.ToString((If(dataStr = "", "url", "")))))

            If GetConfiguration(__CONFIGCLONE__, "renderAt") = "" Then
                SetConfiguration(__CONFIGCLONE__, "renderAt", chartId & Convert.ToString("Div"))
            End If

            Dim wmode As String = GetConfiguration(__CONFIGCLONE__, "wMode")
            If wmode.Trim() = "" OrElse wmode Is Nothing Then
                wmode = If(allowTransparent, "transparent", "opaque")
            End If

            SetConfiguration(__CONFIGCLONE__, "swfUrl", chartSWF)
            SetConfiguration(__CONFIGCLONE__, "dataFormat", dataFormat)
            SetConfiguration(__CONFIGCLONE__, "id", chartId)
            SetConfiguration(__CONFIGCLONE__, "width", chartWidth)
            SetConfiguration(__CONFIGCLONE__, "height", chartHeight)
            SetConfiguration(__CONFIGCLONE__, "wMode", wmode)

            SetConfiguration(__CONFIGCLONE__, "bgColor", bgColor)
            SetConfiguration(__CONFIGCLONE__, "scaleMode", scaleMode)
            SetConfiguration(__CONFIGCLONE__, "lang", language)


            Dim dataSource As String = (If(dataStr = "", dataUrl, dataStr.Replace(vbLf & vbCr, "")))
            Dim dataSourceJSON As String = """dataSource"" : " + (If(dataFormat = "json", dataSource, (Convert.ToString("""") & dataSource) + """"))
            Dim chartConfigJSON As String = (Convert.ToString((Convert.ToString("{") & fc_encodeJSON(GetConfigurationGroup(__CONFIGCLONE__, "params"), False)) + ",") & dataSourceJSON) + "}"

            ' Removes the extra trailing commas in generated JavaScript Object
            Dim Place As Integer = chartConfigJSON.LastIndexOf(","c)
            chartConfigJSON = If((Place >= 0), chartConfigJSON.Remove(Place, 1).Insert(Place, ""), chartConfigJSON)

            Dim builder As New StringBuilder()
            builder.AppendFormat("<!-- Using ASP.NET FusionCharts v3.2.2.1 Wrapper and JavaScript rendering --><!-- START Script Block for Chart {0} -->" + Environment.NewLine, chartId)
            builder.AppendFormat("<div id='{0}Div' >" + Environment.NewLine, chartId)
            builder.Append("Chart." + Environment.NewLine)
            builder.Append("</div>" + Environment.NewLine)
            builder.Append("<script type=""text/javascript"">" + Environment.NewLine)
            builder.AppendFormat("if (FusionCharts && FusionCharts(""{0}"") ) FusionCharts(""{0}"").dispose();" & vbLf, chartId)
            builder.AppendFormat("var chart_{0} = new FusionCharts({1}).render();", chartId, chartConfigJSON)
            builder.Append("</script>" + Environment.NewLine)
            builder.AppendFormat("<!-- END Script Block for Chart {0} -->" + Environment.NewLine, chartId)

            ' Re-Initializing...
            __fc__initialize__()

            __CONFIGCLONE__ = Nothing

            Return builder.ToString()



        End Function




        ''' <summary>
        ''' Renders the HTML code for the chart. This
        ''' method does NOT embed the chart using JavaScript class. Instead, it uses
        ''' direct HTML embedding. So, if you see the charts on IE 6 (or above), you'll
        ''' see the "Click to activate..." message on the chart.
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <param name="allowTransparent">Whether allowTransparent chart (true / false)</param>
        ''' <param name="bgColor">Back Ground Color</param>
        ''' <param name="scaleMode">Set Scale Mode</param>
        ''' <param name="language">Set SWF file Language</param>
        ''' <returns></returns>
        Private Shared Function RenderChartHTMLALL(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean, allowTransparent As Boolean, bgColor As String, scaleMode As String, language As String) As String
            __INIT()

            ' Creating a local copy of global Configuration.
            Dim __CONFIGCLONE__ As Hashtable = DirectCast(__CONFIG__.Clone(), Hashtable)

            Dim wmode As String = GetConfiguration(__CONFIGCLONE__, "wMode")
            If wmode.Trim() = "" OrElse wmode Is Nothing Then
                wmode = If(allowTransparent, "transparent", "opaque")
            End If

            SetConfiguration(__CONFIGCLONE__, "data", chartSWF)
            SetConfiguration(__CONFIGCLONE__, "movie", chartSWF)

            SetConfiguration(__CONFIGCLONE__, "dataURL", dataUrl)
            SetConfiguration(__CONFIGCLONE__, "dataXML", dataStr)

            SetConfiguration(__CONFIGCLONE__, "DOMId", chartId)
            SetConfiguration(__CONFIGCLONE__, "id", chartId)

            SetConfiguration(__CONFIGCLONE__, "width", chartWidth)
            SetConfiguration(__CONFIGCLONE__, "chartWidth", chartWidth)

            SetConfiguration(__CONFIGCLONE__, "height", chartHeight)
            SetConfiguration(__CONFIGCLONE__, "chartHeight", chartHeight)

            SetConfiguration(__CONFIGCLONE__, "debugMode", boolToNum(debugMode))
            SetConfiguration(__CONFIGCLONE__, "registerWithJS", boolToNum(True))

            SetConfiguration(__CONFIGCLONE__, "wMode", wmode)

            SetConfiguration(__CONFIGCLONE__, "bgColor", bgColor)
            SetConfiguration(__CONFIGCLONE__, "scaleMode", scaleMode)
            SetConfiguration(__CONFIGCLONE__, "lang", language)


            Dim strFlashVars As String = FC_Transform(GetConfigurationGroup(__CONFIGCLONE__, "fvars"), "&{key}={value}", True)
            SetConfiguration(__CONFIGCLONE__, "flashvars", strFlashVars)

            Dim strObjectNode As String = FC_Transform(GetConfigurationGroup(__CONFIGCLONE__, "object"), " {key}=""{value}""", True)
            Dim strObjectParamsNode As String = FC_Transform(GetConfigurationGroup(__CONFIGCLONE__, "objparams"), vbTab & "<param name=""{key}"" value=""{value}"">" & vbLf, True)


            Dim htmlcodes As New StringBuilder()

            htmlcodes.AppendFormat("<!-- Using ASP.NET FusionCharts v3.2.2.1 Wrapper --><!-- START HTML Code Block for Chart {0} -->" & vbLf, chartId)
            htmlcodes.AppendFormat("<object classid='clsid:d27cdb6e-ae6d-11cf-96b8-444553540000' {0}>" & vbLf, strObjectNode)
            htmlcodes.Append(strObjectParamsNode + Environment.NewLine)
            htmlcodes.AppendFormat("<!--[if !IE]>-->" & vbLf & "<object type='application/x-shockwave-flash' {0}>" & vbLf & "{1}</object>" & vbLf & "<!--<![endif]-->" & vbLf & "</object>" & vbLf, strObjectNode, strObjectParamsNode)
            htmlcodes.AppendFormat("<!-- END HTML Code Block for Chart {0} -->" & vbLf, chartId)

            ' Re-Initializing...
            __fc__initialize__()

            Return htmlcodes.ToString()
        End Function
#End Region

        ''' <summary>
        ''' Generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>
        <Obsolete("")> _
        Public Shared Function RenderChart(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean) As String
            Return RenderChartALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, registerWithJS, False, "", "noScale", "EN")
        End Function

        ''' <summary>
        ''' Generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <param name="allowTransparent">Whether allowTransparent chart (true / false)</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>
        <Obsolete("")> _
        Public Shared Function RenderChart(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean, allowTransparent As Boolean) As String
            Return RenderChartALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, registerWithJS, allowTransparent, "", "noScale", "EN")
        End Function

        ''' <summary>
        ''' Generate html code for rendering chart
        ''' This function assumes that you've already included the FusionCharts JavaScript class in your page
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <param name="allowTransparent">Whether allowTransparent chart (true / false)</param>
        ''' <param name="bgColor">Back Ground Color</param>
        ''' <param name="scaleMode">Set Scale Mode</param>
        ''' <param name="language">Set SWF file Language</param>
        ''' <returns>JavaScript + HTML code required to embed a chart</returns>
        <Obsolete("")> _
        Public Shared Function RenderChart(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean, allowTransparent As Boolean, bgColor As String, scaleMode As String, language As String) As String
            Return RenderChartALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, registerWithJS, allowTransparent, bgColor, scaleMode, language)
        End Function

        ''' <summary>
        ''' Renders the HTML code for the chart. This
        ''' method does NOT embed the chart using JavaScript class. Instead, it uses
        ''' direct HTML embedding. So, if you see the charts on IE 6 (or above), you'll
        ''' see the "Click to activate..." message on the chart.
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <returns></returns>
        <Obsolete("")> _
        Public Shared Function RenderChartHTML(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean) As String
            Return RenderChartHTMLALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, False, False, "", "noScale", "EN")
        End Function

        ''' <summary>
        ''' Renders the HTML code for the chart. This
        ''' method does NOT embed the chart using JavaScript class. Instead, it uses
        ''' direct HTML embedding. So, if you see the charts on IE 6 (or above), you'll
        ''' see the "Click to activate..." message on the chart.
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <returns></returns>
        <Obsolete("")> _
        Public Shared Function RenderChartHTML(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean) As String
            Return RenderChartHTMLALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, registerWithJS, False, "", "noScale", "EN")
        End Function

        ''' <summary>
        ''' Renders the HTML code for the chart. This
        ''' method does NOT embed the chart using JavaScript class. Instead, it uses
        ''' direct HTML embedding. So, if you see the charts on IE 6 (or above), you'll
        ''' see the "Click to activate..." message on the chart.
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <param name="allowTransparent">Whether allowTransparent chart (true / false)</param>
        ''' <returns></returns>
        <Obsolete("")> _
        Public Shared Function RenderChartHTML(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean, allowTransparent As Boolean) As String
            Return RenderChartHTMLALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, registerWithJS, allowTransparent, "", "noScale", "EN")
        End Function

        ''' <summary>
        ''' Renders the HTML code for the chart. This
        ''' method does NOT embed the chart using JavaScript class. Instead, it uses
        ''' direct HTML embedding. So, if you see the charts on IE 6 (or above), you'll
        ''' see the "Click to activate..." message on the chart.
        ''' </summary>
        ''' <param name="chartSWF">SWF File Name (and Path) of the chart which you intend to plot</param>
        ''' <param name="dataUrl">If you intend to use dataURL method for this chart, pass the URL as this parameter. Else, set it to "" (in case of dataXML method)</param>
        ''' <param name="dataStr">If you intend to use dataXML method for this chart, pass the XML data as this parameter. Else, set it to "" (in case of dataURL method)</param>
        ''' <param name="chartId">Id for the chart, using which it will be recognized in the HTML page. Each chart on the page needs to have a unique Id.</param>
        ''' <param name="chartWidth">Intended width for the chart (in pixels)</param>
        ''' <param name="chartHeight">Intended height for the chart (in pixels)</param>
        ''' <param name="debugMode">Whether to start the chart in debug mode</param>
        ''' <param name="registerWithJS">Whether to ask chart to register itself with JavaScript</param>
        ''' <param name="allowTransparent">Whether allowTransparent chart (true / false)</param>
        ''' <param name="bgColor">Back Ground Color</param>
        ''' <param name="scaleMode">Set Scale Mode</param>
        ''' <param name="language">Set SWF file Language</param>
        ''' <returns></returns>
        <Obsolete("")> _
        Public Shared Function RenderChartHTML(chartSWF As String, dataUrl As String, dataStr As String, chartId As String, chartWidth As String, chartHeight As String, _
            debugMode As Boolean, registerWithJS As Boolean, allowTransparent As Boolean, bgColor As String, scaleMode As String, language As String) As String
            Return RenderChartHTMLALL(chartSWF, dataUrl, dataStr, chartId, chartWidth, chartHeight, _
                debugMode, registerWithJS, allowTransparent, bgColor, scaleMode, language)
        End Function


        ''' <summary>
        ''' encodes the dataURL before it's served to FusionCharts
        ''' If you have parameters in your dataURL, you'll necessarily need to encode it
        ''' </summary>
        ''' <param name="dataUrl">dataURL to be fed to chart</param>
        ''' <param name="noCacheStr">Whether to add aditional string to URL to disable caching of data</param>
        ''' <returns>Encoded dataURL, ready to be consumed by FusionCharts</returns>
        <Obsolete("")> _
        Public Shared Function EncodeDataURL(dataUrl As String, noCacheStr As Boolean) As String

            Dim result As String = dataUrl
            If noCacheStr Then
                result += If((dataUrl.IndexOf("?") <> -1), "&", "?")
                'Replace : in time with _, as FusionCharts cannot handle : in URLs
                result += "FCCurrTime=" + DateTime.Now.ToString().Replace(":", "_")
            End If

            Return System.Web.HttpUtility.UrlEncode(result)
        End Function

        ''' <summary>
        ''' Enables Print Manager for Mozilla browsers
        ''' This function returns a small JavaScript snippet which can be added to ClientScript's RegisterClientScriptBlock method
        ''' </summary>
        ''' <example>ClientScript.RegisterClientScriptBlock(Page.GetType(), "", FusionCharts.enableFCPrintManager());</example>
        ''' <returns>String with the JavaScript code</returns>
        <Obsolete("")> _
        Public Shared Function EnablePrintManager() As String
            Dim strHTML As String = "<script type=""text/javascript""><!--" & vbLf & " if(FusionCharts && FusionCharts.printManager) FusionCharts.printManager.enabled(true);" & vbLf & "// --></script>"
            Return (strHTML)
        End Function


        ''' <summary>
        ''' Enables Print Manager for Mozilla browsers
        ''' </summary>
        ''' <param name="CurrentPage">Current page reference</param>
        <Obsolete("")> _
        Public Shared Sub EnablePrintManager(CurrentPage As Object)
            Dim HostPage As System.Web.UI.Page
            HostPage = DirectCast(CurrentPage, System.Web.UI.Page)
            Dim strHTML As String = "<script type=""text/javascript""><!--" & vbLf & " if(FusionCharts && FusionCharts.printManager) FusionCharts.printManager.enabled(true);" & vbLf & "// --></script>"
            HostPage.ClientScript.RegisterClientScriptBlock(HostPage.[GetType](), "", strHTML)
        End Sub


        Private Shared Sub __INIT()
            If __CONFIG__Initialized = False Then
                __fc__initialize__()
                __fc__initstatic__()
                __CONFIG__Initialized = True
            End If
        End Sub

        ''' <summary>
        ''' Sets the dataformat to be provided to charts (json/xml)
        ''' </summary>
        ''' <param name="format">Data format. Default is 'xml'. Other format is 'json'</param>
        <Obsolete("")> _
        Public Shared Sub SetDataFormat(format As String)
            __INIT()

            If format.Trim().Length = 0 Then
                format = "xml"
            End If
            ' Stores the dataformat in global configuration store
            SetConfiguration("dataFormat", format)
        End Sub

        ''' <summary>
        ''' Sets renderer type (flash/javascript)
        ''' </summary>
        ''' <param name="renderer"> Name of the renderer. Default is 'flash'. Other possibility is 'javascript'</param>
        <Obsolete("")> _
        Public Shared Sub SetRenderer(renderer As String)
            __INIT()

            If renderer.Trim().Length = 0 Then
                renderer = "flash"
            End If
            ' stores the renderer name in global configuration store
            SetConfiguration("renderer", renderer)
        End Sub

        ''' <summary>
        ''' Explicitely sets window mode (window[detault]/transpatent/opaque)
        ''' </summary>
        ''' <param name="mode">Name of the mode. Default is 'window'. Other possibilities are 'transparent'/'opaque'</param>
        <Obsolete("")> _
        Public Shared Sub SetWindowMode(mode As String)
            __INIT()
            SetConfiguration("wMode", mode)
        End Sub

        ''' <summary>
        ''' FC_SetConfiguration sets various configurations of FusionCharts
        ''' It takes configuration names as first parameter and its value a second parameter
        ''' There are config groups which can contain common configuration names. All config names in all groups gets set with this value
        ''' unless group is specified explicitly
        ''' </summary>
        ''' <param name="setting">Name of configuration</param>
        ''' <param name="value">Value of configuration</param>
        <Obsolete("")> _
        Public Shared Sub SetConfiguration(setting As String, value As Object)
            For Each de As DictionaryEntry In __CONFIG__
                If DirectCast(__CONFIG__(de.Key), Hashtable).ContainsKey(setting) Then
                    DirectCast(__CONFIG__(de.Key), Hashtable)(setting) = value
                End If
            Next
        End Sub

        ''' <summary>
        ''' FC_SetConfiguration sets various configurations of FusionCharts
        ''' It takes configuration names as first parameter and its value a second parameter
        ''' There are config groups which can contain common configuration names. All config names in all groups gets set with this value
        ''' unless group is specified explicitly
        ''' </summary>
        ''' <param name="setting">Name of configuration</param>
        ''' <param name="value">Value of configuration</param>
        Private Shared Sub SetConfiguration(ByRef __TEMPHASH__ As Hashtable, setting As String, value As Object)
            For Each de As DictionaryEntry In __TEMPHASH__
                If DirectCast(__TEMPHASH__(de.Key), Hashtable).ContainsKey(setting) Then
                    DirectCast(__TEMPHASH__(de.Key), Hashtable)(setting) = value
                End If
            Next
        End Sub


#Region "Helper Private Methods"
        Private Shared Function GetHTTP() As String
            'Checks for protocol type.
            Dim isHTTPS As String = HttpContext.Current.Request.ServerVariables("HTTPS")
            'Checks browser type.
            Dim isMSIE As Boolean = HttpContext.Current.Request.ServerVariables("HTTP_USER_AGENT").Contains("MSIE")
            'Protocol initially sets to http.
            Dim sHTTP As String = "http"
            If isHTTPS.ToLower() = "on" Then
                sHTTP = "https"
            End If
            Return sHTTP
        End Function

        ''' <summary>
        ''' Transform the meaning of boolean value in integer value
        ''' </summary>
        ''' <param name="value">true/false value to be transformed</param>
        ''' <returns>1 if the value is true, 0 if the value is false</returns>
        Private Shared Function boolToNum(value As Boolean) As Integer
            Return If(value, 1, 0)
        End Function

        Private Shared Sub SetCONSTANTConfiguration(setting As String, value As Object)
            DirectCast(__CONFIG__("constants"), Hashtable)(setting) = value
        End Sub

        Private Shared Function GetConfiguration(setting As String) As String
            For Each de As DictionaryEntry In __CONFIG__
                If DirectCast(__CONFIG__(de.Key), Hashtable).ContainsKey(setting) Then
                    Return DirectCast(__CONFIG__(de.Key), Hashtable)(setting).ToString()
                End If
            Next
            Return Nothing
        End Function

        Private Shared Function GetConfiguration(ByRef __TEMPHASH__ As Hashtable, setting As String) As String
            For Each de As DictionaryEntry In __TEMPHASH__
                If DirectCast(__TEMPHASH__(de.Key), Hashtable).ContainsKey(setting) Then
                    Return DirectCast(__TEMPHASH__(de.Key), Hashtable)(setting).ToString()
                End If
            Next
            Return Nothing
        End Function

        Private Shared Function GetConfigurationGroup(setting As String) As Hashtable
            If __CONFIG__.ContainsKey(setting) Then
                Return DirectCast(__CONFIG__(setting), Hashtable)
            End If
            Return Nothing
        End Function

        Private Shared Function GetConfigurationGroup(ByRef __TEMPHASH__ As Hashtable, setting As String) As Hashtable
            If __TEMPHASH__.ContainsKey(setting) Then
                Return DirectCast(__TEMPHASH__(setting), Hashtable)
            End If
            Return Nothing
        End Function

        Private Shared Function FC_Transform(arr As Hashtable, tFormat As String, ignoreBlankValues As Boolean) As String
            Dim converted As String = ""
            Dim Key As String = "", Value As String = ""
            For Each ds As DictionaryEntry In arr
                If ignoreBlankValues = True AndAlso ds.Value.ToString().Trim() = "" Then
                    Continue For
                End If
                Key = ds.Key.ToString()
                Value = ds.Value.ToString()
                If Key.ToLower().Equals("codebase") Then
                    Value = Value.Replace("http", GetHTTP())
                End If
                Dim TFApplied As String = tFormat.Replace("{key}", Key)
                TFApplied = TFApplied.Replace("{value}", Value)
                converted = converted & TFApplied
            Next
            Return converted
        End Function

        Private Shared Function fc_encodeJSON(json As Hashtable, enclosed As Boolean) As String
            Dim strjson As String = ""
            If enclosed = True Then
                strjson = "{"
            End If

            strjson = strjson & FC_Transform(json, """{key}"" : ""{value}"", ", True)
            strjson = strjson.Trim()

            If strjson.EndsWith(",") Then
                strjson = strjson.Remove(strjson.Length - 1)
            End If

            Return strjson
        End Function

        Private Shared Sub __fc__initstatic__()
            Dim constant As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            constant("scriptbaseUri") = ""
            __CONFIG__("constants") = constant
            constant = Nothing
        End Sub

        Private Shared Sub __fc__initialize__()
            __CONFIG__ = Nothing
            __CONFIG__ = New Hashtable(StringComparer.InvariantCultureIgnoreCase)

            Dim param As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            param("swfUrl") = ""
            param("width") = ""
            param("height") = ""
            param("renderAt") = ""
            param("renderer") = ""
            param("dataSource") = ""
            param("dataFormat") = ""
            param("id") = ""
            param("lang") = ""
            param("debugMode") = ""
            param("registerWithJS") = ""
            param("detectFlashVersion") = ""
            param("autoInstallRedirect") = ""
            param("wMode") = ""
            param("scaleMode") = ""
            param("menu") = ""
            param("bgColor") = ""
            param("quality") = ""


            __CONFIG__("params") = param


            Dim fvar As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            fvar("dataURL") = ""
            fvar("dataXML") = ""
            fvar("chartWidth") = ""
            fvar("chartHeight") = ""
            fvar("DOMId") = ""
            fvar("registerWithJS") = "1"
            fvar("debugMode") = "0"
            fvar("scaleMode") = "noScale"
            fvar("lang") = "EN"
            fvar("animation") = "undefined"
            __CONFIG__("fvars") = fvar

            Dim [oBject] As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            [oBject]("height") = ""
            [oBject]("width") = ""
            [oBject]("id") = ""
            [oBject]("lang") = "EN"
            [oBject]("class") = "FusionCharts"
            [oBject]("data") = ""
            __CONFIG__("object") = [oBject]

            Dim objparam As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            objparam("movie") = "noScale"
            objparam("scaleMode") = "noScale"
            objparam("scale") = ""
            objparam("wMode") = ""
            objparam("allowScriptAccess") = "always"
            objparam("quality") = "best"
            objparam("FlashVars") = ""
            objparam("bgColor") = ""
            objparam("swLiveConnect") = ""
            objparam("base") = ""
            objparam("align") = ""
            objparam("salign") = ""
            objparam("menu") = ""
            __CONFIG__("objparams") = objparam

            Dim embeds As New Hashtable(StringComparer.InvariantCultureIgnoreCase)
            embeds("height") = ""
            embeds("width") = ""
            embeds("id") = ""
            embeds("src") = ""
            embeds("flashvars") = ""
            embeds("name") = ""
            embeds("scaleMode") = "noScale"
            embeds("wMode") = ""
            embeds("bgColor") = ""
            embeds("quality") = "best"
            embeds("allowScriptAccess") = "always"
            embeds("type") = "application/x-shockwave-flash"
            embeds("pluginspage") = "http://www.macromedia.com/go/getflashplayer"
            embeds("swLiveConnect") = ""
            embeds("base") = ""
            embeds("align") = ""
            embeds("salign") = ""
            embeds("scale") = ""
            embeds("menu") = ""
            __CONFIG__("embed") = embeds

            param = Nothing
            fvar = Nothing
            [oBject] = Nothing
            objparam = Nothing
            embeds = Nothing
        End Sub
#End Region
    End Class
End Namespace
