import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="genetic",passwd="vibhu")
cur1 = mycon.cursor()

def same():
    sql = '''create table same
            (name INT not null primary key,
            age int not null,
            intelligence INT not null,
            speed INT not null,
            strength INT not null,
            attractiveness int not null,
            parent varchar(10) not null,
            d_a varchar(10) not null,
            total INT not null
            );'''
    cur1.execute(sql)
    mycon.commit()
    
def different():
    sql = '''create table different
            (name INT not null primary key,
            age int not null,
            intelligence INT not null,
            speed INT not null,
            strength INT not null,
            attractiveness int not null,
            parent varchar(10) not null,
            d_a varchar(10) not null,
            total INT not null
            );'''
    cur1.execute(sql)
    mycon.commit()

def nat_select():
    sql = '''create table nat_select
            (name INT not null primary key,
            age int not null,
            intelligence INT not null,
            speed INT not null,
            strength INT not null,
            attractiveness int not null,
            parent varchar(10) not null,
            d_a varchar(10) not null,
            total INT not null
            );'''
    cur1.execute(sql)
    mycon.commit()


nat_select()
##same()
##different()

cur1.close()
mycon.close()
print("Done")


