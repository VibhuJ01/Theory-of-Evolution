from tabulate import tabulate
from mutation import mutation,bin2int,int2bin
import random

import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="genetic",passwd="vibhu")
cur1 = mycon.cursor()


def crossoverDiff(bin,n):   
    j = []
    while(len(j)<6):
        while(True):
            r1 = random.randint(0,5)
            if(r1 not in j):
                j.append(r1)
                break

        while(True):
            r2 = random.randint(0,5)
            if(r2 not in j):
                j.append(r2)
                break
         
        c = []
        d = []
        for k in range(3):
            a = bin[r1][k]
            b = bin[r2][k]
            c.append(a[:14]+b[14:])
            d.append(b[:14]+a[14:])
            
        inte,sp,st = mutation(c[0],c[1],c[2])
        inte,sp,st = bin2int(inte,sp,st)
        insert(n+len(j)-2,inte,sp,st,str(n-6+r1)+' '+str(n-6+r2))

        inte,sp,st = mutation(d[0],d[1],d[2])
        inte,sp,st = bin2int(inte,sp,st)
        insert(n+len(j)-1,inte,sp,st,str(n-6+r1)+' '+str(n-6+r2))

def insert(j,inte,sp,st,p):
    sql = 'insert into different values(%s,%s,%s,%s,%s,%s,%s)'
    data = [j,0,inte,sp,st,p,inte+sp+st]
    cur1.execute(sql,data)
    mycon.commit()

    
def updateDiff(n):
    for i in range(25):
        tot = 0
        for j in range(n):
            if(j%6 == 0 or j%6 == 1):
                inte= random.randint(1,2)
                sp = random.randint(0,1)
                st = random.randint(0,1)
            
            elif(j%6 == 2 or j%6 == 3):
                sp= random.randint(1,2)
                inte = random.randint(0,1)
                st = random.randint(0,1)
                
            else:
                st= random.randint(1,2)
                sp = random.randint(0,1)
                inte = random.randint(0,1)

            sql = '''update different
                    set age = age + %s,
                    intelligence = intelligence + %s,
                    speed = speed + %s,
                    strength = strength + %s
                    where name = %s'''
        
            data = [1,inte,sp,st,j]
            cur1.execute(sql,data)
            mycon.commit()

#Calculte Total
    sql = 'select * from different'
    cur1.execute(sql)
    result = cur1.fetchall()
    j = 0
    for i in result:
        total = 0
        total = i[2]+i[3]+i[4]
        sql = '''update different
                set total = %s
                where name = %s'''
        data = [total,j]
        cur1.execute(sql,data)
        mycon.commit()
        j+=1

def displayDiff():
    print("Result Different->\n")
    sql = 'select * from different'
    cur1.execute(sql)
    result = cur1.fetchall()
    total = 0
    for i in result:
        total += i[6]
        
    keys = ['Name','Age','Intelligence','Speed','Strength','Parent','Total']
    print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))
    print('Total-> ',total)
    print("\n--------------------------------------------\n")

def childDiff(n):
    sql = 'select * from different'
    cur1.execute(sql)
    result = cur1.fetchall()
    result = result[n-6:]
    bin = []
    for i in result:
        bin.append(int2bin(i[2],i[3],i[4]))
    crossoverDiff(bin,n)
