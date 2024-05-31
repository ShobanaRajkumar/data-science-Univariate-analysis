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
        return quanqual
    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cusum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable
    def Univariate(dataset,quan):
        descriptive_stats=pd.DataFrame(index["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
	        descriptive_stats[columnName]["Mean"]=dataset[columnName].mean()
	        descriptive_stats[columnName]["Median"]=dataset[columnName].median()
            descriptive_stats[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive_stats[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive_stats[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive_stats[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive_stats[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive_stats[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive_stats[columnName]["IQR"]=descriptive_stats[columnName]["Q3:75"]-descriptive_stats[columnName]["Q1:25%"]
            descriptive_stats[columnName]["1.5rule"]=1.5*descriptive_stats[columnName]["IQR"]
            descriptive_stats[columnName]["Lesser"]=descriptive_stats[columnName]["Q1:25%"]-descriptive_stats[columnName]["1.5rule"]
            descriptive_stats[columnName]["Greater"]=descriptive_stats[columnName]["Q3:75%"]+descriptive_stats[columnName]["1.5rule"]                                                          
            descriptive_stats[columnName]["Min"]=dataset[columnName].min()
            descriptive_stats[columnName]["Max"]=dataset[columnName].max()
        return descriptive_stats
    def replacementoutlayer_lesser(dataset,lesser):
		for columnName in lesser:
			dataset[[columnName][dataset][columnName]<descriptive_stats[columnName]["lesser"]]
		return replacementoutlayer_lesser
	def replacementoutlayer_Greater(dataset,Greater):
		for columnName in Greater:
			dataset[[columnName][dataset][columnName]>descriptive_stats[columnName]["Greater"]]
		return replacementoutlayer_Greater		    
                  
        
        
        