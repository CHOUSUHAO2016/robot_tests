import csv
import subprocess
import os
import re

from datetime import datetime,timedelta
serialNo = "2cda42095d1d7ece"
cmd = "adb -s "+serialNo+ " shell dumpsys package packages | grep -E 'Package \[|version'"
with open("output.txt","w") as output:
	subprocess.call(cmd,stdout=output);
versionCode = []
package = []
versionName = []
content = []
var1 = []
var2 = []
output.close()
with open("output.txt","r+") as f:
    for line in f:
        line = line.strip()
        if (line.find('versionCode') != -1):
            str = line.split(" ")
            for i in range (len(str)):
                if (str[i].find('versionCode=') != -1):
                    s = str[i].strip('versionCode=')
                    versionCode.append(s)
        elif (line.find('Package [') != -1):
            str = line.strip('Package')
            str = str.replace(":","")
            package.append(str)
        elif (line.find('versionName') != -1):
            str = line.split(" ")
            for i in range (len(str)):
                if (str[i].find('versionName=') != -1):
                    s = str[i].strip('versionName=')
                    versionName.append(s)
f.close()
# os.remove("output.txt")
now = datetime.now()
dt_str= now.strftime("%d/%m/%Y_%H:%M:%S")
dt = dt_str.replace("/","")
dt = dt.replace(":","")
fileName = "APK_Version_List_"+dt+".csv"
print(fileName)


pattern = re.compile( r"[a-z A-Z 0-9\.\_]+\]")
for str in package:
    m=[]
    strs=[]
    m = pattern.findall(str) 
    m_len = len(m)

    if(m_len > 0):
        str = m[0].replace("]", "")
        strs = (str.split('.')) 
        strs_len = len(strs)
        try:
            var1.append(strs[strs_len-2])
        except:
            var1.append("")
        try:
            var2.append(strs[strs_len-1])
        except:
            var2.append("")
    else:
        var1.append("")
        var2.append("")
with open(fileName,'w') as file:
    writer = csv.writer(file)
    writer.writerow(["SN","Package Name","Var1","Var2","Version Code","Version Name"])
    for i in range (len(package)) :
        writer.writerow([(i+1),package[i],var1[i],var2[i],versionCode[i],versionName[i]])
file.close()