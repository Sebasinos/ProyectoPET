def gen_info(lista2):
    d=1
    a=0
    for i in lista2:
        listadosis=[]
        listadosis.append(str(d))
        c=0
        while c < 3:
            listadosis.append(lista2[a][c])
            c = c+1
    
        listafinal.append(listadosis)
        a=a+1                      
        d=d+1

    print (listafinal)

