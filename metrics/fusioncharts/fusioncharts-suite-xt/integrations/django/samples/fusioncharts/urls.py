"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from fusioncharts.views import catalogue

from fusioncharts import datahandler
from fusioncharts.samples import rendering_angular_gauge_using_dictionary_example, rendering_column2d_chart_using_dictionary_example
from fusioncharts.samples import rendering_map_using_dictionary_example, rendering_multiseries_column2d_chart_using_json_example
from fusioncharts.samples import rendering_multiseries_StackedColumn2dline_using_json_example, rendering_pie3d_using_json_example
from fusioncharts.samples import rendering_column_line_area_combi_using_json_example, rendering_map_using_json_example
from fusioncharts.samples import rendering_angular_gauge_using_json_example, client_side_chart_export
from fusioncharts.samples import fetching_json_data_from_url, fetching_xml_data_from_url, fetching_data_from_database
from fusioncharts.samples import drilldown_from_database_example, rendering_charts_by_common_theme
from fusioncharts.samples import export_chart_using_export_handler
from fusioncharts.samples import dynamic_chart_resize, dynamic_chart_type, chart_annotation, chart_update_onclick
from fusioncharts.samples import chart_tooltip, rendering_chart_with_different_language, chart_special_chart
from fusioncharts.samples import product_life_cycle_event, special_event, chart_message, interactive_event, number_format_module
from fusioncharts.samples import special_chart_type_api, chart_instance_level_api, chart_product_level_api
from fusioncharts.samples import updating_chart_properties, highlight_specific_data_points, update_data_runtime
from fusioncharts.samples import get_data_from_scatter_chart
from fusioncharts.samples import Line_Chart_With_Time_Axis, Plotting_Multiple_Series_On_Time_Axis
from fusioncharts.samples import Column_and_line_combination_on_time_axis, Plotting_Two_Variables
from fusioncharts.samples import Different_Plot_Type_Chart, ColumnChart_With_Time_Axis
from fusioncharts.samples import AreaChart_With_Time_Axis, Interactive_candlestick_chart
from fusioncharts.samples import Annotating_single_data_point, Single_Event_Overlay
from fusioncharts.samples import Date_range_event_overlay, Adding_Reference_Line


urlpatterns = [
    url(r'^$', catalogue),
    url(r'^admin/', admin.site.urls),
    url(r'^datahandler', datahandler.getdata),
    url(r'^rendering-angular-gauge-using-dictionary-example', rendering_angular_gauge_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-angular-gauge-using-json-example', rendering_angular_gauge_using_json_example.chart, name='chart'),
    url(r'^rendering-column2d-chart-using-dictionary-example', rendering_column2d_chart_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-map-using-dictionary-example', rendering_map_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-map-using-json-example', rendering_map_using_json_example.chart, name='chart'),
    url(r'^rendering-multiseries-column2d-chart-using-json-example', rendering_multiseries_column2d_chart_using_json_example.chart, name='chart'),
    url(r'^rendering-multiseries-StackedColumn2dline-using-json-example', rendering_multiseries_StackedColumn2dline_using_json_example.chart, name='chart'),
    url(r'^rendering-pie3d-using-json-example', rendering_pie3d_using_json_example.chart, name='chart'),
    url(r'^rendering-column-line-area-combi-using-json-example', rendering_column_line_area_combi_using_json_example.chart, name='chart'),
    url(r'^client-side-chart-export', client_side_chart_export.chart, name='chart'),
    url(r'^fetching-json-data-from-url', fetching_json_data_from_url.chart, name='chart'),
    url(r'^fetching-xml-data-from-url', fetching_xml_data_from_url.chart, name='chart'),
    url(r'^fetching-data-from-database', fetching_data_from_database.chart, name='chart'),
    url(r'^drilldown-from-database-example', drilldown_from_database_example.chart, name='chart'),
    url(r'^rendering-charts-by-common-theme', rendering_charts_by_common_theme.chart, name='chart'),
    url(r'^export-chart-using-export-handler', export_chart_using_export_handler.chart, name='chart'),
    url(r'^dynamic-chart-resize', dynamic_chart_resize.chart, name='chart'),
    url(r'^dynamic-chart-type', dynamic_chart_type.chart, name='chart'),
    url(r'^chart-annotation', chart_annotation.chart, name='chart'),
    url(r'^chart-update-onclick', chart_update_onclick.chart, name='chart'),
    url(r'^rendering-chart-with-different-language', rendering_chart_with_different_language.chart, name='chart'),
    url(r'^chart-special-chart', chart_special_chart.chart, name='chart'),
    url(r'^chart-tooltip', chart_tooltip.chart, name='chart'),
    url(r'^product-life-cycle-event', product_life_cycle_event.chart, name='chart'),
    url(r'^special-event', special_event.chart, name='chart'),
    url(r'^chart-message', chart_message.chart, name='chart'),
    url(r'^interactive-event', interactive_event.chart, name='chart'),
    url(r'^number-format-module', number_format_module.chart, name='chart'),
    url(r'^special-chart-type-api', special_chart_type_api.chart, name='chart'),
    url(r'^chart-instance-level-api', chart_instance_level_api.chart, name='chart'),
    url(r'^chart-product-level-api', chart_product_level_api.chart, name='chart'),
    url(r'^updating-chart-properties', updating_chart_properties.chart, name='chart'),
    url(r'^highlight-specific-data-points', highlight_specific_data_points.chart, name='chart'),
    url(r'^update-data-runtime', update_data_runtime.chart, name='chart'),
    url(r'^get-data-from-scatter-chart', get_data_from_scatter_chart.chart, name='chart'),
    url(r'^Line-Chart-With-Time-Axis', Line_Chart_With_Time_Axis.chart, name='chart'),
    url(r'^Plotting-Multiple-Series-On-Time-Axis', Plotting_Multiple_Series_On_Time_Axis.chart, name='chart'),
    url(r'^Column-and-line-combination-on-time-axis', Column_and_line_combination_on_time_axis.chart, name='chart'),
    url(r'^Plotting-Two-Variables', Plotting_Two_Variables.chart, name='chart'),
    url(r'^Different-Plot-Type-Chart', Different_Plot_Type_Chart.chart, name='chart'),
    url(r'^ColumnChart-With-Time-Axis', ColumnChart_With_Time_Axis.chart, name='chart'),
    url(r'^AreaChart-With-Time-Axis', AreaChart_With_Time_Axis.chart, name='chart'),
    url(r'^Interactive-candlestick-chart', Interactive_candlestick_chart.chart, name='chart'),
    url(r'^Annotating-single-data-point', Annotating_single_data_point.chart, name='chart'),
    url(r'^Single-Event-Overlay', Single_Event_Overlay.chart, name='chart'),
    url(r'^Date-range-event-overlay', Date_range_event_overlay.chart, name='chart'),
    url(r'^Adding-Reference-Line', Adding_Reference_Line.chart, name='chart') 
]