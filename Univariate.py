class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
               # print("quan")
                quan.append(columnName)
        return quan,qual
    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cusum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable
    def Univariate(dataset,quan):                                                        
		  descriptive_stats=pd.DataFrame(index["Mean","Median","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%",                                               "IQR","1.5rule","lesser","Greater","Min","Max"],columns=quan)
          for columnName in quan:
            desctriptive_stats[columnName]["Mean"]=dataset[columnName].mean()
	        desctriptive_stats[columnName]["Median"]=dataset[columnName].median()
            desctriptive_statsd[columnName]["Mode"]=dataset[columnName].mode()[0]
            desctriptive_stats[columnName]["Q1:25%"]=dataset.describe_stats()[columnName]["25%"]
            desctriptive_stats[columnName]["Q2:50%"]=dataset.describe_stats()[columnName]["50%"]
            desctriptive_stats[columnName]["Q3:75%"]=dataset.describe_stats()[columnName]["75%"]
            desctriptive_stats[columnName]["99%"]=np.percentile(dataset[columnName],99)
            desctriptive_stats[columnName]["Q4:100%"]=dataset.describe_stats()[columnName]["max"]
			descriptive_stats[columnName]"IQR"]=descriptive_stats
                                  [columnName][Q3:75%"]descriptive_stats[columName]["Q1:25%"]
            descriptive_stats[columnName]["1.5rule"]=1.5*descriptive_stats[columnName]["IQR"]
            descriptive_stats[columnName]["Lesser"]=descriptive_stats[columnName]["Q1:25%"]- 
                                          descriptive_stats[columnName]["1.5rule"]
            descriptive_stats[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]                                                                                                     ["1.5rule"]
            descriptive_stats[columnName]["Min"]=dataset[columnNamee].min()
            descriptive_stats[columnName]["Max"]=dataset[columnName].max()
        return descriptive_stats
	def replacementoutlayer_lesser(dataset,lesser):
		for columnName in lesser:
			dataset [columnName][dataset[columnName]<descriptive_stats[columnName]["lesser"]]
		return replacementoutlayer_lesser
	def replacementoutlayer_Greater(dataset,Greater):
		for columnName in Greater:
			dataset[columnName][dataset[columnName]>descriptive_stats[columnName]["Greater"]]
		return replacementoutlayer_Greater		    
                  
        
        
        