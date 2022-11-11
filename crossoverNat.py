from tabulate import tabulate
from mutation import mutation,bin2int,int2bin
import random

import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="genetic",passwd="vibhu")
cur1 = mycon.cursor()


def childNat(n):
    sql = 'select * from nat_select'
    cur1.execute(sql)
    result = cur1.fetchall()
    result = result[n-6:]

    l = []
    for i in result:
        l.append(i[5])
        
    l.sort()
    ind = {}
    
    for i in range(len(result)):
        if(result[i][5] == l[0]):
            ind['low1'] = i

        elif(result[i][5] == l[1]):
            ind['low2'] = i
            
        elif(result[i][5] == l[-1]):
            ind['high1'] = i
            
        elif(result[i][5] == l[-2]):
            ind['high2'] = i

    result[ind['low1']] = result[ind['high1']]
    result[ind['low2']] = result[ind['high2']]
    
    bin = []
    for i in result:
        bin.append(int2bin(i[2],i[3],i[4]))
    crossoverNat(bin,n)

def crossoverNat(bin,n):   
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
    sql = 'insert into nat_select values(%s,%s,%s,%s,%s,%s,%s,%s)'
    data = [j,0,inte,sp,st,inte+sp+st,p,'Alive']
    cur1.execute(sql,data)
    mycon.commit()

    
def updateNat():
    for i in range(25):
        dead_alive_Nat()
        sql = 'select * from nat_select where d_a = "Alive"'
        cur1.execute(sql)
        result = cur1.fetchall()
        n = len(result)
        
        tot = 0
        for j in range(n):
            if(result[j][7] == 'Dead'):
                continue
            
            r = random.randint(0,2)
            if(r == 0):
                inte= random.randint(1,2)
                sp = random.randint(0,1)
                st = random.randint(0,1)
            
            elif(r == 1):
                sp= random.randint(1,2)
                inte = random.randint(0,1)
                st = random.randint(0,1)
                
            else:
                st= random.randint(1,2)
                sp = random.randint(0,1)
                inte = random.randint(0,1)

            sql = '''update nat_select
                    set age = age + %s,
                    intelligence = intelligence + %s,
                    speed = speed + %s,
                    strength = strength + %s,
                    attractiveness = attractiveness + %s
                    where name = %s'''

            data = [1,inte,sp,st,inte + sp + st,result[j][0]]
            cur1.execute(sql,data)
            mycon.commit()

def displayNat():
    print("Result Natural Selection->\n")
    sql = 'select * from nat_select'
    cur1.execute(sql)
    result = cur1.fetchall()
    
    keys = ['Name','Age','Intelligence','Speed','Strength','Attractive','Parent','Dead/Alive']
    print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))

    total = 0
    result = result[len(result)-6:]
    for i in result:
        total += i[5]
    print('Attractiveness of Last 6 Children-> ',total)
    print("\n--------------------------------------------\n")




def dead_alive_Nat():
    sql = 'select * from nat_select where d_a = "Alive" and age > 70'
    cur1.execute(sql)
    result = cur1.fetchall()
    if(len(result) == 0):
        return
    
    for i in result:
        r = random.randint(1,100)
        if(r<=15):
            sql = '''update nat_select
                     set d_a = %s
                     where name = %s'''
            
            data = ('Dead',i[0])
            cur1.execute(sql,data)
            mycon.commit()
            


