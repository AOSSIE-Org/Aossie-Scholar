package fusioncharts;

import java.util.*;

public class FusionCharts {
	private String constructorTemplate = "<script type=\"text/javascript\">\nFusionCharts.ready(function () {\n\tvar fc_chart = new FusionCharts(%s);\n%sfc_chart.render();\n});\n</script>";
	private String constructorTimeSeriesTemplate = "<script type=\"text/javascript\">\nFusionCharts.ready(function () {\n\t%s\nvar fc_chart = new FusionCharts(%s);\nfc_chart.render();\n});\n</script>";
	
	private String eventTemplate = "    fc_chart.addEventListener(\"%s\",%s);\n";
	private String messageTemplate = ",%s:\"%s\"";
	private String[] chartOptions = new String[10];
    private String chartDataSource = "";
    private TimeSeries timeSeriesDataSource = null;    
    private String fusionChartsEvents = "";
    private String fusionChartsMessages = "";
    
    public FusionCharts(String type, String id, String width, String height, String renderAt, String dataFormat, String dataSource) {    	
        this.chartOptions[0] = id;
        this.chartOptions[1] = width;
        this.chartOptions[2] = height;
        this.chartOptions[3] = renderAt;
        this.chartOptions[4] = type;
        this.chartOptions[5] = dataFormat;
        //this.chartOptions[6] = "%s"; 
        if(this.chartOptions[5].contains("url")) {
            this.chartOptions[7] = "\""+dataSource+"\"";
        } else {
        	this.chartOptions[7] = "%s";
            this.chartDataSource = this.addSlashes(dataSource.replaceAll("\n", ""));
        }        
    }
    
    public FusionCharts(String type, String id, String width, String height, String renderAt, String dataFormat, TimeSeries timeSeries) {    	
        this.chartOptions[0] = id;
        this.chartOptions[1] = width;
        this.chartOptions[2] = height;
        this.chartOptions[3] = renderAt;
        this.chartOptions[4] = type;
        this.chartOptions[5] = dataFormat;

        if(this.chartOptions[5].toLowerCase().contains("json")) {
        	this.chartOptions[7] = "%s";
        	this.timeSeriesDataSource = timeSeries;
        }        
    }
    
    private String addSlashes(String str) {
        str = str.replaceAll("\\\\", "\\\\\\\\");
        str = str.replaceAll("\\n", "\\\\n");
        str = str.replaceAll("\\r", "\\\\r");
        str = str.replaceAll("\\00", "\\\\0");
        str = str.replaceAll("u003d", "=");
        str = str.replaceAll("'", "\\\\'");
        str = str.replaceAll("\\\\", "");
        str = str.replaceAll("\"\\{", "{");
        str = str.replaceAll("\"\\[", "[");
        str = str.replaceAll("\\}\\]\"", "}]");
        str = str.replaceAll("\"\\}\"", "\"}");
        str = str.replaceAll("\\}\"\\}", "}}");
        return str;
    }
    
    private String jsonEncode(String[] data){
        String json = "{type: \""+this.chartOptions[4]+"\",renderAt: \""+this.chartOptions[3]+"\",width: \""+this.chartOptions[1]+"\",height: \""+this.chartOptions[2]+"\",dataFormat: \""+this.chartOptions[5] + "\"," + 
        				"id:\"" + this.chartOptions[0] + "\"" + this.fusionChartsMessages + ",dataSource: "+this.chartOptions[7]+"}";
        return json;
    }
    
    public String render() {
        String outputHTML;
        outputHTML="";
        if (this.timeSeriesDataSource == null)
        {
	        if(this.chartOptions[5].contains("url")) {
	            outputHTML = String.format(this.constructorTemplate, this.jsonEncode(this.chartOptions));
	            
	        } else {
	            if("json".equals(this.chartOptions[5])) {
	            	this.chartOptions[7] = String.format(this.chartOptions[7], this.chartDataSource);
	            	outputHTML = String.format(this.constructorTemplate, this.jsonEncode(this.chartOptions), fusionChartsEvents);
	            } else {
	            	this.chartOptions[7] = String.format(this.chartOptions[7], "\'"+ this.chartDataSource + "\'");
	            	outputHTML = String.format(this.constructorTemplate, this.jsonEncode(this.chartOptions), fusionChartsEvents);
	            }
	        }
        }else{
        	this.chartOptions[7] = String.format(this.chartOptions[7], this.timeSeriesDataSource.GetDataSource());
        	outputHTML = String.format(this.constructorTimeSeriesTemplate, this.timeSeriesDataSource.GetDataStore(), this.jsonEncode(this.chartOptions));       	
        }
        return outputHTML;
    }
    
    public void addEvent(String eventName, String funcName){
    	String eventHTML;
    	eventHTML = String.format(this.eventTemplate, eventName, funcName);
    	this.fusionChartsEvents += eventHTML;
    }
    
    public void addMessage(String messageName, String messageText){
    	String messageString;
    	messageString = String.format(this.messageTemplate, messageName, messageText);
    	this.fusionChartsMessages += messageString;
    }
    
    public static class TimeSeries {
    	
    	private List<KeyValuePair> attributes = new ArrayList<KeyValuePair>();
    	
    	private FusionTable fusionTableObject = null;
    	
    	public TimeSeries(FusionTable fusionTable){
    		this.fusionTableObject = fusionTable;
    	}
    	
    	public void AddAttribute(String Key, String Value){    		
    		this.attributes.add(new KeyValuePair(Key, Value));
    	}
    	
    	public String GetDataSource(){
    		
    		StringBuilder sb = new StringBuilder();

    		for (KeyValuePair attrib : this.attributes){    			
                sb.append(String.format("%s:%s,%s", attrib.key, attrib.value, System.getProperty("line.separator")));
            }
            sb.append(String.format("%s:%s%s", "data", "fusionTable", System.getProperty("line.separator")));

            return "{" + System.getProperty("line.separator") + sb.toString() + System.getProperty("line.separator") + "}";
    	}
    	
    	public String GetDataStore() {
    		return this.fusionTableObject.GetDataTable();
        }
    	
        protected class KeyValuePair {
            private String key;
            private String value;
            public KeyValuePair(String key, String value) {
                this.key = key;
                this.value = value;
            }
        }
    	
    }
    
    public static class FusionTable {
    	
    	public enum OrderBy
        {
            ASC, DESC
        }
    	
    	public enum FilterType
        {
            Equals, Greater,
            GreaterEquals, Less,
            LessEquals, Between
        }
    	
    	private StringBuilder stringBuilder = null;
    	
    	public FusionTable(String schema, String data){
    		this.stringBuilder = new StringBuilder();
    		this.stringBuilder.append("let schema = " + schema + ";" + System.getProperty("line.separator"));
    		this.stringBuilder.append("let data = " + data + ";" + System.getProperty("line.separator"));
    		this.stringBuilder.append("let fusionDataStore = new FusionCharts.DataStore();" + System.getProperty("line.separator"));
    		this.stringBuilder.append("let fusionTable = fusionDataStore.createDataTable(data, schema);" + System.getProperty("line.separator"));
    	}
    	
    	public void Select(String... columnName){
    		if (columnName.length > 0) {
                String columns = String.format("'%s'", String.join("', '", columnName));
                this.stringBuilder.append("fusionTable = fusionTable.query(FusionCharts.DataStore.Operators.select([" + columns + "]));" + System.getProperty("line.separator"));
            }
    	}
    	
    	public void Sort(String columnName, OrderBy columnOrderBy){
    		String data = String.format("{column: '%s', order: '%s'}", columnName, columnOrderBy.equals(OrderBy.ASC) ? "asc" : "desc");            
            String sortedData = String.format("sort([%s])", data);
            this.stringBuilder.append("fusionTable = fusionTable.query(" + sortedData + ");" + System.getProperty("line.separator"));
    	}
    	
    	public String CreateFilter(FilterType filterType, String columnName, Object... values){
    		String fx = filterType.toString();
            fx = fx.substring(0, 1).toLowerCase() + fx.substring(1);

            String filter = null; 

            switch(filterType)
            {
                case Equals:
                    filter = String.format("FusionCharts.DataStore.Operators.%s('%s', '%s')", fx, columnName, values[0].toString());
                    break;
                case Between:
                    if (values.length > 1)
                    {
                        filter = String.format("FusionCharts.DataStore.Operators.%s('%s', %s, %s)", fx, columnName, values[0], values[1]);
                    }
                    break;
                default:
                    filter = String.format("FusionCharts.DataStore.Operators.%s('%s', %s)", fx, columnName, values[0]);
                    break;
            }

            return filter;
    	}
    	
    	public void ApplyFilter(String filter){
    		 if (filter != null && !filter.isEmpty()) {
    			 this.stringBuilder.append("fusionTable = fusionTable.query(" + filter + ");" + System.getProperty("line.separator"));
             }
    	}
    	
    	public void ApplyFilterByCondition(String filter){
    		if (filter != null && !filter.isEmpty()) {
    			this.stringBuilder.append("fusionTable = fusionTable.query(" + filter + ");" + System.getProperty("line.separator"));
            }
    	}
    	
    	public void Pipe(String... filters){
    		if (filters.length > 0) {
                String columns = String.format("'%s'", String.join(", ", filters));
                this.stringBuilder.append("fusionTable = fusionTable.query(FusionCharts.DataStore.Operators.pipe(" + columns + "));" + System.getProperty("line.separator"));
            }
    	}
    	
    	public String GetDataTable(){
    		return this.stringBuilder.toString();
    	}
    	
    }
    
}

