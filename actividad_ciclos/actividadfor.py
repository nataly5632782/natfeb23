Vuelo={
    
   'Aereolinea': 'Avianca',
   'vuelo': 'Avi989',
   'origen': 'ctg',
   'Destino':'MDE',
 
   'tipomaleta':['cabina','mano','bodega']}   


for id,value, in Vuelo.items():
    print(f"{id}:{value}")
    
    print("\nvalores del tipo de maleta")
for maleta in Vuelo["tipomaleta"]:
    print(maleta)
    