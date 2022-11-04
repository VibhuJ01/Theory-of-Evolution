import random

def mutation(inte,sp,st):
    a = ''
    b = ''
    c = ''
    inte = inte[::-1]
    sp = sp[::-1]
    st = st[::-1]
    l = []
    for i in range(len(inte)):
        if(inte[i] == '0'):
            l.append(i)
            if(len(l) == 3):
                break
    i = random.randint(0,2) 
    a = inte[:l[i]] + '1' + inte[l[i]+1:]

    l = []
    for i in range(len(sp)):
        if(sp[i] == '0'):
            l.append(i)
            if(len(l) == 3):
                break
            
    i = random.randint(0,2)      
    b = sp[:l[i]]+ '1'+ sp[l[i]+1:]
            
    l = []
    for i in range(len(st)):
        if(st[i] == '0'):
            l.append(i)
            if(len(l) == 3):
                break
            
    i = random.randint(0,2)   
    c = st[:l[i]] + '1' + st[l[i]+1:]
           

    return a[::-1],b[::-1],c[::-1]

def bin2int(binte,bsp,bst):
    
    binte = binte[::-1]
    bsp = bsp[::-1]
    bst = bst[::-1]
    x=0
    y=0
    z=0
    
    for i in range(len(binte)):
        x+=int(binte[i])*pow(2,i)
        
    for i in range(len(bsp)):
        y+=int(bsp[i])*pow(2,i)
        
    for i in range(len(bst)):
        z+=int(bst[i])*pow(2,i)
        
    return x,y,z

def int2bin(binte,bsp,bst):
    x = ''
    y = ''
    z = ''
    
    while(binte>0 or len(x)<16):
        x+=str(binte%2)
        binte//=2
        
    while(bsp>0 or len(y)<16):
        y+=str(bsp%2)
        bsp//=2
        
    while(bst>0 or len(z)<16):
        z+=str(bst%2)
        bst//=2
    
    x = x[::-1]
    y = y[::-1]
    z = z[::-1]
    
    return x,y,z
