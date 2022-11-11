from crossover import crossover,update,display,child,dead_alive
from crossoverDiff import crossoverDiff,updateDiff,displayDiff
from crossoverDiff import childDiff,dead_alive_Diff

from crossoverNat import crossoverNat,updateNat,displayNat
from crossoverNat import childNat,dead_alive_Nat

import random

import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="genetic",passwd="vibhu")
cur1 = mycon.cursor()


def main():

    #Delete old Data from Same
    sql = 'delete from same'
    cur1.execute(sql)
    mycon.commit()
    
    #Delete old Data from Different
    sql = 'delete from different'
    cur1.execute(sql)
    mycon.commit()

    #Delete old Data from Nat_Select
    sql = 'delete from nat_select'
    cur1.execute(sql)
    mycon.commit()

    #Insert new data
    print("\n--------------------------------------------\n")
    insert()
    display()
    displayDiff()
    displayNat()
    
    update()
    updateDiff()
    updateNat()

    #Run the program for n years
    years = 500
    for i in range(years//25):  
        child(6*(i+1))
        update()
        childDiff(6*(i+1))
        updateDiff()
        childNat(6*(i+1))
        updateNat()
        print(i+1)
        
    print("\n--------------------------------------------\n")
    display()
    displayDiff()
    displayNat()
    

#Insert first 6 babies       
def insert():
    for i in range(6):
        if(i<2):
            inte= random.randint(10,20)
            sp = random.randint(1,10)
            st = random.randint(1,10)
        elif(i<4):
            inte= random.randint(1,10)
            sp = random.randint(10,20)
            st = random.randint(1,10)
        else:
            inte= random.randint(1,10)
            sp = random.randint(1,10)
            st = random.randint(10,20)

        # For Same Tribe
        sql = 'insert into same values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        attract = inte + 2*sp + 2*st
        data = [i,0,inte,sp,st,attract,'God','Alive',inte+sp+st]
        cur1.execute(sql,data)
        mycon.commit()

        # For Different Tribes
        sql = 'insert into different values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        attract = inte + 2*sp + 2*st
        data = [i,0,inte,sp,st,attract,'God','Alive',inte+sp+st]
        cur1.execute(sql,data)
        mycon.commit()

        # For Natural Selection
        sql = 'insert into nat_select values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        attract = inte + 2*sp + 2*st
        data = [i,0,inte,sp,st,attract,'God','Alive',inte+sp+st]
        cur1.execute(sql,data)
        mycon.commit()

    
if(__name__=='__main__'):
    main()
