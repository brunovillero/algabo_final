def gale_shapley(FamiliasPorDepartamento , CentrosPorDepartamento):

    FamiliasResidual = []

    a = FamiliasPorDepartamento["RIVERA"][1]


    print(a)


    #for departamento_centros in CentrosPorDepartamento:
    for centro in CentrosPorDepartamento["RIVERA"]:
        contador = 0
        for familia in centro.familias_preferenciales:
            contador += familia.id
            print(contador, centro.departamento)

"""
    for departamento_familias in FamiliasPorDepartamento:           #iterar por departamento
        Familias = FamiliasPorDepartamento[departamento_familias]   #array de familias en el departamento
        Centros = CentrosPorDepartamento[departamento_familias]     #array de centros en el departamento

        FamiliasMatch = {}         #key familia valor centro
        CentrosMatch = {}          #key centro  valor familias
        
        while Familias:
            Familia = Familias.pop()                          #saca una familia de la lista

            preferencias = Familia.centros_preferenciales

            asignado = False

            for FPR in Centros[0].familias_preferenciales:
                print(FPR.id)
            break
            for centro in preferencias:
                i = 0                       #indice centro
                for Centroi in Centros:
                    if (Centroi.nombre == centro):
                        break
                    i +=1
                Centro = Centros[i]
                esta = False
                iF = 0

                #print(centro, Centro.nombre)

                for FPR in Centro.familias_preferenciales:
                    if (FPR.id == Familia):
                        print("llego")
                        esta = True
                    #print(FPR.id, Familia,departamento_familias, FPR.departamento)
                    iF +=1
                if esta:
                    Familia = Centro.familias_preferenciales[iF]
                    print(Familia)
                    if (Centro.capacidad_max >= Familia.cantidad_hijos):
                        FamiliasMatch[Familia.id] = Centro
                        if Centros[Centro]:
                            Centros[Centro] = []
                        Centros[Centro].appdend(Familia.id)
                        Centros[i].capacidad_max -= Familia.cantidad_hijos
                        asignado = True
                        print("llego1")
                        break
                    else:
                        mayor = 0
                        for FamiliaPref in Centros[Centro]:
                            if (Centrofamilias_preferenciales.index(FamiliaPref) > mayor):
                                mayor = Centrofamilias_preferenciales.index(Familia)
                        if (Centrofamilias_preferenciales.index(FamiliaPref) < mayor):
                            FASacar = Centrofamilias_preferenciales[mayor]
                            FamiliasMatch.pop(FASacar.id)
                            FamiliasMatch[Familia.id] = Centro
                            Centros[Centro].remove(FASacar.id)
                            Centro[Centro].append(Familia.id)
                            Centros[i].capacidad_max += FASacar.cantidad_hijos
                            Centros[i].capacidad_max -= Familia.cantidad_hijos
                        asignado = True
                        print("llego2")
                        break

            if (asignado == True):
                FamiliasResidual.append(Familia)

    # se terminan las familias de los departamentos
    for FamiliaR in FamiliasResidual:
        print(FamiliaR.id)
    print("largo",len(FamiliasResidual))

    '''
    # Obtener el número de hombres y mujeres
    n = len(men_preferences)
    
    # Crear arrays para almacenar a las parejas asignadas
    men_matched = [-1] * n
    women_matched = [-1] * n
    
    # Crear una cola de hombres no emparejados
    free_men = list(range(n))
    
    # Mientras todavía haya hombres sin emparejar
    while free_men:
        # Obtener al próximo hombre sin emparejar
        man = free_men.pop(0)
        
        # Obtener las preferencias de ese hombre
        preferences = men_preferences[man]
        
        # Recorrer las mujeres de sus preferencias
        for i in range(n):
            woman = preferences[i]
            
            # Verificar si la mujer está libre
            if women_matched[woman] == -1:
                # Hacer el emparejamiento
                men_matched[man] = woman
                women_matched[woman] = man
                break
            else:
                # Obtener al hombre con el que está emparejada
                current_man = women_matched[woman]
                
                # Verificar si la mujer prefiere al nuevo hombre
                if women_preferences[woman].index(current_man) > women_preferences[woman].index(man):
                    # Hacer el nuevo emparejamiento
                    men_matched[man] = woman
                    women_matched[woman] = man
                    
                    # Agregar al antiguo hombre a la lista de hombres libres
                    free_men.append(current_man)
                    break
    
    # Retornar los emparejamientos
    return men_matched

'''
"""