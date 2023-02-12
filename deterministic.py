from tabulate import tabulate
from mutation import mutation,bin2int,int2bin

import random
import statistics as st #To find Variance

import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="genetic",passwd="vibhu")
cur1 = mycon.cursor()


def crossover(bin,n):   
    j = 0
    while(j<6):
        c = []
        d = []
        for k in range(3):
            a = bin[j][k]
            b = bin[j+1][k]
            c.append(a[:28]+b[28:])
            d.append(b[:28]+a[28:])
            
        inte,sp,st = mutation(c[0],c[1],c[2])
        inte,sp,st = bin2int(inte,sp,st)
        insert(n+j,inte,sp,st,str(n+j-6)+' '+str(n+j-5))

        inte,sp,st = mutation(d[0],d[1],d[2])
        inte,sp,st = bin2int(inte,sp,st)
        insert(n+j+1,inte,sp,st,str(n+j-6)+' '+str(n+j-5))
        j+=2

def insert(j,inte,sp,st,p):
    sql = 'insert into same values(%s,%s,%s,%s,%s,%s,%s,%s)'
    data = [j,0,inte,sp,st,inte+sp+st,p,'Alive']
    cur1.execute(sql,data)
    mycon.commit()

    
def aging():

    for i in range(25):
        dead_alive()
        sql = 'select * from same where d_a = "Alive"'
        cur1.execute(sql)
        result = cur1.fetchall()
        n = len(result)
        
        tot = 0
        for j in range(n):
            if(result[j][7] == 'Dead'):
                continue
            
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

            sql = '''update same
                    set age = age + %s,
                    intelligence = intelligence + %s,
                    speed = speed + %s,
                    strength = strength + %s,
                    attractiveness = attractiveness + %s
                    where name = %s'''

            data = [1,inte,sp,st,inte + sp + st,result[j][0]]
            cur1.execute(sql,data)
            mycon.commit()


def display(a):
    sql = 'select * from same'
    cur1.execute(sql)
    result = cur1.fetchall()
    result = result[len(result)-6:]
    

    #Find Sum of variance
    total = []
    for i in result:
        total.append(st.variance([i[2],i[3],i[4]]))

    sum1 = round(sum(total))

    if(a == 0):
        #Find Attractiveness
        total = 0
        for i in result:
            total += i[5]
            
        print("Result Deterministic->\n")
        keys = ['Name','Age','Intelligence','Speed','Strength','Attractive','Parent','Dead/Alive']
        print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))

        print('Attractiveness of Last 6 Children-> ',total)
        print("\n--------------------------------------------\n")
        
        print('Variance in Last 6 Children-> ',sum1)
        print("\n--------------------------------------------\n")
    
    elif(a == 1):
        return sum1

def child(n):
    sql = 'select * from same'
    cur1.execute(sql)
    result = cur1.fetchall()
    result = result[n-6:]
    bin = []
    for i in result:
        bin.append(int2bin(i[2],i[3],i[4]))
    crossover(bin,n)

def dead_alive():
    
    sql = 'select * from same where d_a = "Alive" and age > 70'
    cur1.execute(sql)
    result = cur1.fetchall()
    if(len(result) == 0):
        return
    
    for i in result:
        r = random.randint(1,100)
        if(r<=15):
            sql = '''update same
                     set d_a = %s
                     where name = %s'''
            
            data = ('Dead',i[0])
            cur1.execute(sql,data)
            mycon.commit()
            

