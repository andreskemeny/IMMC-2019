import pulp

my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)

######### -------- VARIABLES -------- ########
# Numero de personas, queremos maximizar
NP = pulp.LpVariable('Numero Personas', lowBound=0, cat='Continuous')
# Cantidad de comida que se produce, cal/año
Nc = pulp.LpVariable('Numero Comida', lowBound=0, cat='Continuous')
# Espacio que se ocupa para producir la comida en metros cuadrados
Ec = pulp.LpVariable("Espacio Comida", lowBound=0, cat='Continuous')
# Numero de viviendas
Nv = pulp.LpVariable("Numero Viviendas", lowBound=0, cat='Continuous')
# Espacio total que ocupan las viviendas en metros cuadrados
ETV = pulp.LpVariable("ETV", lowBound=0, cat='Contirnuous')

######### -------- PARAMETROS -------- ########
# Porcentaje cultivable de la superficie terrestre del planeta
Pc = 0.37
# Porcentaje habitable de la superficie terrestre de la tierra, metros cuadrados
Ph = 0.33
# Porcentaje no habitable de la superficie terrestre de la tierra, metros cuadrados
Pnh = 0.67
# Superficie terrestre del planeta
T = 148940000000000
# Espacio no habitable de la tierra, metros cuadrados
Enh = T * Pnh
# Kilocalorias que una persona necesita al dia
X1 = 1500000
# Espacio de una vivienda
Ev = 37
# Rendimiento de la comdia por metro cuadrado
Rc = 2743

Th = T * 0.71
Tc = Th * 0.38



######### -------- FUNCION OBJETIVO -------- ########
my_lp_problem += NP, "Z"


# el espacio que ocupan las viviendas tiene que ser igual al espacio que ocupa 1 vivienda por la cantidad de personas
#my_lp_problem += ETV <= Ev*NP

######### -------- RESTRICCIONES -------- ########

#### ---- RESTRICCIONES GENERALES ---- ####
#my_lp_problem += T - Enh >= Ec + ETV
#my_lp_problem += NP*1 != 0  # numero de personas tiene que ser distinto de 0


#### ---- RESTRICCIONES PARA LAS VIVIENDAS ---- ####
my_lp_problem += NP <= Nv  # el numero de personas tiene que ser menor o igual a las viviendas (1:1)
my_lp_problem += ETV <= Ph*T  # el area que ocupan las viviendas tiene que ser menor o igual al espacio habitable
my_lp_problem += Nv == ETV/Ev  # espacio que ocupan las casas partido en el numero de casas

#### ---- RESTRICCIONES PARA LA COMIDA ---- ####
my_lp_problem += NP <= Nc*1/X1  # numero de personas tiene que ser menor que la comida que se produce/lo que 1 come
#my_lp_problem += Ec <= Pc*T  # Ec tiene que ser menor al area cultivable
#my_lp_problem += Ec*1 != 0  # Ec tiene que ser distinto de 0 (si te da negativo hiciste algo como el hoyo)
my_lp_problem += Nc == Ec*Rc  # espacio ocupado en comida por lo que produce cada espacio = total comida prod.
my_lp_problem += Ec == (547500000*NP)/274300000000  #
my_lp_problem += Ec + ETV <= Th  # suma de areas tiene que ser menor o igual a area habitable
my_lp_problem += Ec <= Tc  # Tc = area cultivable del area habitable (hacen overlap)


print(my_lp_problem.solve())
print(pulp.LpStatus[my_lp_problem.status])

for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))
