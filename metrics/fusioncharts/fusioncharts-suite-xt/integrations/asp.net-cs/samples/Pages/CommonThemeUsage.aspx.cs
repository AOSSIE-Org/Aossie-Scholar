using System;
using FusionCharts.Charts;


public partial class CommonThemeUsage : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        // store chart data as json string
        string jsonDataFirstChart, jsonDataSecondChart;
        jsonDataFirstChart = "{                      'chart': {                    'caption': 'Split of Sales by Product Category',                    'subCaption': '5 top performing stores  - last month',                    'plotToolText': '<div><b>\\$label</b><br/>Product : <b>\\$seriesname</b><br/>Sales : <b>\\$\\$value</b></div>',                    'theme': 'fusion'                    },                    'categories': [{                      'category': [{                        'label': 'Garden Groove harbour'                      }, {                        'label': 'Bakersfield Central'                      }, {                        'label': 'Los Angeles Topanga'                      }, {                        'label': 'Compton-Rancho Dom'                      }, {                        'label': 'Daly City Serramonte'                      }]                    }],                    'dataset': [{                      'seriesname': 'Non-Food Products',                      'data': [{                        'value': '28800'                      }, {                        'value': '25400'                      }, {                        'value': '21800'                      }, {                        'value': '19500'                      }, {                        'value': '11500'                      }]                    }, {                      'seriesname': 'Food Products',                      'data': [{                        'value': '17000'                      }, {                        'value': '19500'                      }, {                        'value': '12500'                      }, {                        'value': '14500'                      }, {                        'value': '17500'                      }]                    }]                }";
        jsonDataSecondChart = "{                    'chart': {                    'caption': 'Harry\\'s SuperMart',                  'subCaption': 'Top 5 stores in last month by revenue',                  'theme': 'fusion'                  },                  'data':[                    {                        'label': 'Bakersfield Central',                      'value': '880000'                  },                  {                        'label': 'Garden Groove harbour',                      'value': '730000'                  },                  {                        'label': 'Los Angeles Topanga',                      'value': '590000'                  },                  {                        'label': 'Compton-Rancho Dom',                      'value': '520000'                  },                  {                        'label': 'Daly City Serramonte',                      'value': '330000'                  }                  ]              }";
      
        // Create chart instance for first chart
        Chart overlappedColumnChart = new Chart("overlappedcolumn2d", "first_chart", "600", "300", "json", jsonDataFirstChart);
        // create chart instance for second chart
        Chart columnChart = new Chart("column2d","second_chart","600","300","json", jsonDataSecondChart);
        // render first chart
        Literal1.Text = overlappedColumnChart.Render();
        // render second chart
        Literal2.Text = columnChart.Render();
    }

}