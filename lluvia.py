import xlrd
from arrays import Array3D

def main():
    a3 = Array3D(34,33,14)
    for anio in range(1985,2019,1):
        ruta = './Precipitacion/'+str(anio)+'Precip.xls'
        archivo = xlrd.open_workbook(filename=ruta)
        hoja = archivo.sheet_by_index(0)
        for r in range(1,34,1):
            for c in range(0,14,1):
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))
                

    estados = ["ENTIDAD","AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR","CAMPECHE","COAHUILA","COLIMA","CHIAPAS","CHIHUAHUA","DISTRITO FEDERAL","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO","ESTADO DE MEXICO","MICHOACAN","MORELOS","NAYARIT","NUEVO LEON","OAXACA","PUEBLA","QUERETARO","QUINTANA ROO","SAN LUIS POTOSI","SINALOA","SONORA","TABASCO","TAMAULIPAS","TLAXCALA","VERACRUZ","YUCATAN","ZACATECAS"]  
    
    mes = ["MES","ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]

    print("+----------------------------------+\n \t1")
    a = int(input("Año(1985-2019):"))
    e = int(input("Estado(1-32):"))
    m = int(input("Mes(1-12):"))
    x = a3.get_item(a-1985,e,m)
    
   
    print("\nEn el estado de ",estados[e],"llovio un promedio de",x,"centimetros cubicos en el mes de",mes[m],"de",a,"\n")

    print("\n------------\n")
    sums = 0
    e2 = int(input("Estado(1-32):"))
    m2 = int(input("Mes(1-12):"))
    for g in range(1985,2019,1):
        a2 = a3.get_item(g-1985,e2,m2)
        suma = a2 + suma
        #print(a2)
    print("\n",estados[e2],"Promedio(1985-2018)","Mes de:",mes[m2],"\n")    
    print(suma/(g-1985))
    print("\n--------------\n")
    
    promedioTotal = 0
    e3 = int(input("Estado (1-32):"))
    for z in range(0,12,1):
        z+=1
        for g in range(1985,2019,1):
            v2 = a3.get_item(g-1985,e3,z)
            #print(v2)
            promedioTotal = v2 +promedioTotal
    print("\n",estados[e3],"\n")
    print(promedioTotal/(z*34))
    print("\n")
    
    promedioTotal = 0
    for c in range(0,32,1):
        c += 1
        for s in range(12,13,1):
            s+=1
            for g in range(1985,2019,1):
                s2 = a3.get_item(g-1985,r,t)
                promedioTotal = s2 + promedioTotal
                #print(s2)
    print("\n--------------\n")
    print("El promedio general es: ",promedioTotal/(c*(g-1984)))
    
main()
