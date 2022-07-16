import json
class SatData:
    def __init__(self):
        #Read the json file
        with open('sat.json', 'r') as f:
            self.data = json.load(f)['data']
    def save_as_csv(self,dbns):
        resData=[]#to store the required dbns data
        #Fetch the data of the required dbns
        for data in self.data:
            if data[8] in dbns: #8assuming dbns is located at position 8
                resData.append(data)
        #Sorting the dbns data based upon the dbns
        resData = sorted(resData, key=lambda x:x[8])

        #Create output.csv to store the reult
        with open('output.csv', 'a+') as f:
            #Add the row of column header
            header = [str(i) for i in range(len(resData[0]))]
            f.write(','.join(header))
            #Create new row
            f.write('\n')
            #Add the remaining data
            for row in resData:
                rowData=[]
                for item in row:
                    #To handle the entry which has , in between
                    if ',' in str(item):
                        rowData.append("\""+item+"\"")
                    else:
                        rowData.append(str(item))
                f.write(','.join(rowData))
                #Create new row
                f.write('\n')

sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
