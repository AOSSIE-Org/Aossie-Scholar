import pandas as pd



def get_df():	
	if __name__== "__main__":
		df= pd.read_excel("scimagojr.xlsx")
	else:
		df= pd.read_excel("metrics/scimagojr.xlsx")
	return (df)

#df= get_df() print (df.loc[df["Country"]=="United States"]["Citations per document"].iloc[0]) pf= df.loc[df["Country"]=='India']
#a=pf['Citations per document']
#print (a.iloc[0])




