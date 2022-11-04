from crossover import crossover,update,display,child,dead_alive
from crossoverDiff import crossoverDiff,updateDiff,displayDiff
from crossoverDiff import childDiff,dead_alive_Diff
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

    #Insert new data
    print("\n--------------------------------------------\n")
    insert()
    display()
    displayDiff()
    update(6)
    updateDiff(6)
    
    years = 1000
    for i in range(years//25):  
        child(6*(i+1))
        update(6*(i+2))
        childDiff(6*(i+1))
        updateDiff(6*(i+2))
        print(i)
    display()
    displayDiff()
    
        
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
        sql = 'insert into same values (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [i,0,inte,sp,st,'God','Alive',inte+sp+st]
        cur1.execute(sql,data)
        mycon.commit()

        # For Different Tribes
        sql = 'insert into different values (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [i,0,inte,sp,st,'God','Alive',inte+sp+st]
        cur1.execute(sql,data)
        mycon.commit()

    
if(__name__=='__main__'):
    main()
