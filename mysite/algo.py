import csv
import re
import argparse
parser = argparse.ArgumentParser(description='Process csv files.')
parser.add_argument('csv_file', nargs=2,
                   help='a csv_file for processing')
args = parser.parse_args()
p=True
q=True
branches = []
options=[]
final=[]
inter=[]
branch={}
cpi={}
branch_roll={}
temp={}
temp1={}
temp2={}
with open(args.csv_file[0]) as csvfile:
    t = csv.reader(csvfile, delimiter=',')
    for row in t:
      list3d=[0  for i in range(int(float(row[1])/10+0.5+1)+int(float(row[2])-float(row[1])))]
      list3d[0]=1
      temp[row[0]]=int(float(row[1])/10+0.5)
      temp2[row[0]]=int(float(row[1])*(1/4)+0.5)
      temp1[row[0]]=int(float(row[1])/10+0.5)
      branch_roll[row[0]]=list3d
      cpi[row[0]]=0
      xxx=[]
      xxx.append(int(float(row[2])))
      xxx.append("NA")
      xxx.append(int(float(row[1])))
      xxx.append(int(float(row[2])))
      branch[row[0]]=xxx
      del xxx
      branches.append(row[0])
a=0
with open(args.csv_file[1]) as csvfile:
    t = csv.reader(csvfile, delimiter=',')
    for row in t:
        dabba=[]
        for i in range(len(row)):
           if(i==3):
             row[i]=float(row[i])
           dabba.append(row[i])
        options.append(dabba)
        a=a+1
sorted_list = sorted(options, key=lambda x:x[3],reverse=True)
A=sorted_list
#
bc=a
i=0
while(i<bc):
  b=5
  ab=len(sorted_list[i])
  if(sorted_list[i][4]=='GE' or sorted_list[i][4]=='OBC'):
        if(sorted_list[i][3]<8):
           final1=[]
           final1.append(sorted_list[i][0])
           final1.append(sorted_list[i][1])
           final1.append(sorted_list[i][2])
           final1.append("Ineligible")
           del sorted_list[i]
           bc=bc-1
           final.append(final1)
           continue
  else:
       if(sorted_list[i][3]<7):
           final1=[]
           final1.append(sorted_list[i][0])
           final1.append(sorted_list[i][1])
           final1.append(sorted_list[i][2])
           final1.append("Ineligible")
           del sorted_list[i]
           bc=bc-1
           final.append(final1)
           continue
  while(b<ab):
      if(sorted_list[i][b]!=''):
        if((temp[sorted_list[i][b]]!=0) and cpi[sorted_list[i][b]]<=sorted_list[i][3]):
         branch_roll[sorted_list[i][b]][branch_roll[sorted_list[i][b]][0]]=sorted_list[i][3]
         branch[sorted_list[i][b]][1]=sorted_list[i][3]
         final1=[]
         final1.append(sorted_list[i][0])
         final1.append(sorted_list[i][1])
         final1.append(sorted_list[i][2])
         final1.append(sorted_list[i][b])
         temp[sorted_list[i][b]]=temp[sorted_list[i][b]]-1
         if(temp[sorted_list[i][b]]==0):
           if(cpi[sorted_list[i][b]]==0):
            cpi[sorted_list[i][b]]=sorted_list[i][3]
         branch_roll[sorted_list[i][b]][0]=branch_roll[sorted_list[i][b]][0]+1
         branch_roll[sorted_list[i][2]].append(0)
         temp[sorted_list[i][2]]=temp[sorted_list[i][2]]+1
         if(b==5):
            final.append(final1)
            #print(final1)
            bc=bc-1
            del sorted_list[i]
         else:
            i=i+1
            final1.append(b)
            inter.append(final1)
         break
        if(temp2[sorted_list[i][2]]+temp1[sorted_list[i][2]] == temp[sorted_list[i][2]]):
          if(cpi[sorted_list[i][b]]==0):
           cpi[sorted_list[i][b]]=sorted_list[i][3]
        if(temp[sorted_list[i][b]]==0):
           if(cpi[sorted_list[i][b]]==0):
            cpi[sorted_list[i][b]]=float(sorted_list[i][3])
           if(sorted_list[i][3]==cpi[sorted_list[i][b]]):
                      branch_roll[sorted_list[i][b]].append(0)
                      temp[sorted_list[i][b]]=temp[sorted_list[i][b]]+1
                      temp[sorted_list[i][2]]=temp[sorted_list[i][2]]-1
      b=b+1
  if(b==ab):
         final1=[]
         final1.append(sorted_list[i][0])
         final1.append(sorted_list[i][1])
         final1.append(sorted_list[i][2])
         final1.append("Branch Unchanged")
         final1.append(b)
         inter.append(final1)
         i=i+1
abc=inter+final
while(p and q):
    q=False
    if(a == len(final) ):
        p=False
    i=0
    bc=len(sorted_list)
    while(i<bc):
       b=5
       ab=inter[i][4]
       if(sorted_list[i][3]>=9):
          while(b<ab):
            if(sorted_list[i][b]!=''):
               if(temp2[sorted_list[i][2]]+temp1[sorted_list[i][2]] == temp[sorted_list[i][2]]):
                 temp2[sorted_list[i][2]]=temp2[sorted_list[i][2]]+1
               if((temp[sorted_list[i][b]]!=0)):
                 branch_roll[sorted_list[i][b]][branch_roll[sorted_list[i][b]][0]]=sorted_list[i][3]
                 branch[sorted_list[i][b]][1]=sorted_list[i][3]
                 final1=[]
                 final1.append(sorted_list[i][0])
                 final1.append(sorted_list[i][1])
                 final1.append(sorted_list[i][2])
                 final1.append(sorted_list[i][b])
                 if(inter[i][3]!="Branch Unchanged"):
                    temp[inter[i][3]]=temp[inter[i][3]]+1
                 temp[sorted_list[i][b]]=temp[sorted_list[i][b]]-1
                 branch_roll[sorted_list[i][b]][0]=branch_roll[sorted_list[i][b]][0]+1
                 if(b==5):
                    final.append(final1)
                    #print(final1)
                    bc=bc-1
                    q=True
                    del sorted_list[i]
                    del inter[i]
                 else:
                    final1.append(b)
                    inter[i]=final1
                    i=i+1
                 c=1
                 break
            b=b+1
          if(b==ab):
            i=i+1
       else:
        while(b<ab):
            if(sorted_list[i][b]!=''): 
               if((temp[sorted_list[i][b]]!=0)and cpi[sorted_list[i][b]]<=sorted_list[i][3]):
                 branch_roll[sorted_list[i][b]][branch_roll[sorted_list[i][b]][0]]=sorted_list[i][3]
                 branch[sorted_list[i][b]][1]=sorted_list[i][3]
                 final1=[]
                 final1.append(sorted_list[i][0])
                 final1.append(sorted_list[i][1])
                 final1.append(sorted_list[i][2])
                 final1.append(sorted_list[i][b])
                 if(inter[i][3]!="Branch Unchanged"):
                   temp[inter[i][3]]=temp[inter[i][3]]+1
                 temp[sorted_list[i][b]]=temp[sorted_list[i][b]]-1
                 if(temp[sorted_list[i][b]]==0):
                    cpi[sorted_list[i][b]]=sorted_list[i][3]
                 branch_roll[sorted_list[i][b]][0]=branch_roll[sorted_list[i][b]][0]+1
                 if(b==5):
                    final.append(final1)
                    #print(final1)
                    bc=bc-1
                    q=True
                    del sorted_list[i]
                    del inter[i]
                 else:
                    final1.append(b)
                    q=True
                    inter[i]=final1
                    i=i+1
                 break
               if(temp2[sorted_list[i][2]]+temp1[sorted_list[i][2]] == temp[sorted_list[i][2]]):
                  if(cpi[sorted_list[i][b]]==0):
                    cpi[sorted_list[i][b]]=sorted_list[i][3]
            b=b+1
        if(b==ab):
            i=i+1
          #
#''' 
for i in range(len(inter)):
   del inter[i][4]
final=inter+final
final = sorted(final, key=lambda x:x[0] )
alpha=final[0][0]
xy=[]
allotment=[]
for i in range(len(final)):
  if(final[i][0]==alpha):
    xy.append(final[i])
  else:
    alpha= final[i][0]
    xy=sorted(xy,key=lambda x:x[1].lower())
    for x in range(len(xy)):
     allotment.append(xy[x])
    del xy
    xy=[]
    xy.append(final[i])
xy=sorted(xy,key=lambda x:x[1].lower())
for x in range(len(xy)):
  allotment.append(xy[x])
for i in range(len(allotment)):
   if((str(allotment[i][3]) is "Ineligible") or (str(allotment[i][3]) is "Branch Unchanged")):
      continue
   else:
    branch[allotment[i][2]][0]=branch[allotment[i][2]][0]-1
    branch[allotment[i][3]][0]=branch[allotment[i][3]][0]+1
myfile=open('allotmentstats.csv','w')
myfile.write("Program")
myfile.write(",")
myfile.write("Cut off")
myfile.write(",")
myfile.write("Sanctioned Strength")
myfile.write(",")
myfile.write("Initial Strength")
myfile.write(",")
myfile.write("Final Strength")
myfile.write("\n")
for i in range(len(branches)):
    myfile.write(branches[i])
    myfile.write(",")
    myfile.write(str(branch[branches[i]][1]))
    myfile.write(",")
    myfile.write(str(branch[branches[i]][2]))
    myfile.write(",")
    myfile.write(str(branch[branches[i]][3]))
    myfile.write(",")
    myfile.write(str(branch[branches[i]][0]))
    myfile.write("\n")
myfile=open('allotment3.csv','w')
for i in range(len(allotment)):
    wr=csv.writer(myfile)
    wr.writerow(allotment[i])
