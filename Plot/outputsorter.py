import pandas as pd


def main():
    siggendata = pd.read_csv('siggen.csv', encoding='utf-8').fillna(0)
    mavgdata = pd.read_csv('mavg.csv', encoding='utf-8').fillna(0)
    funcdata = pd.read_csv('func.csv', encoding='utf-8').fillna(0)
    clientdata = pd.read_csv('client.csv', encoding='utf-8').fillna(0)


    siggentimes = siggendata['# timestamp'].iloc[0:].values
    mavgtimes = mavgdata['# timestamp'].iloc[0:].values
    functimes = funcdata['# timestamp'].iloc[0:].values
    clienttimes = clientdata['# timestamp'].iloc[0:].values

    siggenlines = siggendata['line'].iloc[0:].values
    mavglines = mavgdata['line'].iloc[0:].values
    funclines = funcdata['line'].iloc[0:].values
    clientlines = clientdata['line'].iloc[0:].values

    make_Header("csv/siggenroom1temp.csv")
    make_Header("csv/siggenroom1rhum.csv")
    make_Header("csv/siggenroom2temp.csv")
    make_Header("csv/siggenroom2rhum.csv")

    make_Header("csv/mavgroom1temprec.csv")
    make_Header("csv/mavgroom1rhumrec.csv")
    make_Header("csv/mavgroom2temprec.csv")
    make_Header("csv/mavgroom2rhumrec.csv")
    make_Header("csv/mavgroom1temppub.csv")
    make_Header("csv/mavgroom1rhumpub.csv")
    make_Header("csv/mavgroom2temppub.csv")
    make_Header("csv/mavgroom2rhumpub.csv")

    make_Header("csv/funcroom1temp.csv")
    make_Header("csv/funcroom1rhum.csv")
    make_Header("csv/funcroom2temp.csv")
    make_Header("csv/funcroom2rhum.csv")
    make_Header("csv/funcroom1ahum.csv")
    make_Header("csv/funcroom2ahum.csv")

    ycounter = 0
    for x in siggenlines:
        if "room1/temp" in x:
            f = open("csv/siggenroom1temp.csv", "a")
            f.write(str(siggentimes[ycounter]-siggentimes[0]) + ', ' + x.replace("Produced value to siggen/room1/temp value: ","")+'\n')
            f.close()
        elif "room1/rhum" in x:
            f = open("csv/siggenroom1rhum.csv", "a")
            f.write(str(siggentimes[ycounter]-siggentimes[0]) + ', ' + x.replace("Produced value to siggen/room1/rhum value: ","")+'\n')
            f.close()
        elif "room2/temp" in x:
            f = open("csv/siggenroom2temp.csv", "a")
            f.write(str(siggentimes[ycounter]-siggentimes[0])+', '+x.replace("Produced value to siggen/room2/temp value: ","")+'\n')
            f.close()
        elif "room2/rhum" in x:
            f = open("csv/siggenroom2rhum.csv", "a")
            f.write(str(siggentimes[ycounter]-siggentimes[0])+', '+x.replace("Produced value to siggen/room2/rhum value: ","")+'\n')
            f.close()

        ycounter += 1

    ycounter = 0
    for x in mavglines:
        if "room1/temp" in x and "Receiving" in x:
            f = open("csv/mavgroom1temprec.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Receiving value from siggen/room1/temp value: ","")+"\n")
            f.close()
        elif "room1/temp" in x and "Publishing" in x:
            f = open("csv/mavgroom1temppub.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Publishing value to mavg/room1/temp value: ","")+"\n")
            f.close()
        elif "room1/rhum" in x and "Receiving" in x:
            f = open("csv/mavgroom1rhumrec.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Receiving value from siggen/room1/rhum value: ","")+"\n")
            f.close()
        elif "room1/rhum" in x and "Publishing" in x:
            f = open("csv/mavgroom1rhumpub.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Publishing value to mavg/room1/rhum value: ","")+"\n")
            f.close()
        elif "room2/temp" in x and "Receiving" in x:
            f = open("csv/mavgroom2temprec.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Receiving value from siggen/room2/temp value: ","")+"\n")
            f.close()
        elif "room2/temp" in x and "Publishing" in x:
            f = open("csv/mavgroom2temppub.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Publishing value to mavg/room2/temp value: ","")+"\n")
            f.close()
        elif "room2/rhum" in x and "Receiving" in x:
            f = open("csv/mavgroom2rhumrec.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Receiving value from siggen/room2/rhum value: ","")+"\n")
            f.close()
        elif "room2/rhum" in x and "Publishing" in x:
            f = open("csv/mavgroom2rhumpub.csv", "a")
            f.write(str(mavgtimes[ycounter]-siggentimes[0])+', '+x.replace("Publishing value to mavg/room2/rhum value: ","")+"\n")
            f.close()
        ycounter += 1

    ycounter = 0
    for x in funclines:
        if "room1/temp" in x:
            f = open("csv/funcroom1temp.csv", "a")
            f.write(str(functimes[ycounter]-siggentimes[0])+', '+x.replace("Received value from mavg/room1/temp value ","")+"\n")
            f.close()
        elif "room1/rhum" in x:
            f = open("csv/funcroom1rhum.csv", "a")
            f.write(str(functimes[ycounter]-siggentimes[0])+', '+x.replace("Received value from mavg/room1/rhum value ","")+"\n")
            f.close()
        elif "room2/temp" in x:
            f = open("csv/funcroom2temp.csv", "a")
            f.write(str(functimes[ycounter]-siggentimes[0])+', '+x.replace("Received value from mavg/room2/temp value ","")+"\n")
            f.close()
        elif "room2/rhum" in x:
            f = open("csv/funcroom2rhum.csv", "a")
            f.write(str(functimes[ycounter]-siggentimes[0])+', '+x.replace("Received value from mavg/room2/rhum value ","")+"\n")
            f.close()
        elif "room1/ahum" in x:
            f = open("csv/funcroom1ahum.csv", "a")
            f.write(str(functimes[ycounter]-siggentimes[0])+', '+x.replace("Publishing value to func/room1/ahum value: ", "")+"\n")
            f.close()
        elif "room2/ahum" in x:
            f = open("csv/funcroom2ahum.csv", "a")
            f.write(str(functimes[ycounter]-siggentimes[0])+', '+x.replace("Publishing value to func/room2/ahum value: ","")+"\n")
            f.close()
        ycounter += 1

    ycounter = 0
    for x in clientlines:
        if "room1/ahum" in x:
            f = open("csv/clientroom1ahum.csv", "a")
            f.write(str(clienttimes[ycounter])+', '+x+"\n")
            f.close()
        elif "room2/ahum" in x:
            f = open("csv/clientroom2ahum.csv", "a")
            f.write(str(clienttimes[ycounter])+', '+x+"\n")
            f.close()

        ycounter += 1

def make_Header(path):
    f = open(path, "a")
    f.write("timestamp,value"+'\n')
    f.close()

if __name__ == '__main__':
    main()
