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
# Cantidad de oxigeno que se produce, litros/año
No = pulp.LpVariable("No", lowBound=0, cat='Contirnuous')
# Espacio para produccion de oxigeno
Eo = pulp.LpVariable("Eo", lowBound=0, cat='Contirnuous')

######### -------- PARAMETROS -------- ########
# Porcentaje cultivable de la superficie terrestre del planeta
Pc = 0.37
# Porcentaje habitable de la superficie terrestre de la tierra, metros cuadrados
Ph = 0.33
# Porcentaje no habitable de la superficie terrestre de la tierra, metros cuadrados
Pnh = 0.67
# Superficie terrestre del planeta
T = 100000000
# Espacio no habitable de la tierra, metros cuadrados
Enh = T * Pnh
# Kilocalorias que una persona necesita al año
Ckcal = 1/547500
# Litros de oxigeno que una persona necesita al año
Co2 = 1/2883500
# Espacio de una vivienda
Ev = 1/1
# Rendimiento de la comdia por metro cuadrado 2743
Rc = 100
# Rendimiento del oxigeno por metro cuadrad
Ro2 = 7

Th = T * 0.71
Tc = Th * 0.38



######### -------- FUNCION OBJETIVO -------- ########
my_lp_problem += NP, "Z"

######### -------- RESTRICCIONES -------- ########


#### ---- RESTRICCIONES GENERALES ---- ####
my_lp_problem += Ec + ETV + Eo <= Th  # suma de areas tiene que ser menor o igual a area habitable
my_lp_problem += Ec + Eo <= Tc

#### ---- RESTRICCIONES PARA LAS VIVIENDAS ---- ####
my_lp_problem += NP <= Nv  # el numero de personas tiene que ser menor o igual a las viviendas (1:1)
my_lp_problem += ETV <= Ph*T  # el area que ocupan las viviendas tiene que ser menor o igual al espacio habitable
my_lp_problem += Nv == ETV*Ev  # espacio que ocupan las casas partido en el numero de casas

#### ---- RESTRICCIONES PARA LA COMIDA ---- ####
my_lp_problem += NP <= Nc*Ckcal  # numero de personas tiene que ser menor que la comida que se produce/lo que 1 come
#my_lp_problem += Ec <= Tc  # Ec tiene que ser menor al area cultivable
my_lp_problem += Nc == Ec*Rc  # espacio ocupado en comida por lo que produce cada espacio = total comida prod.

#### ---- RESTRICCIONES PARA EL OXIGENO ---- ####
my_lp_problem += NP <= No*Co2
my_lp_problem += No <= Eo*


#Cantidad de litros producidos por m² al año (Ro) * Cantidad de m² dedicados a producir oxígeno (Eo).

print(my_lp_problem.solve())
print(pulp.LpStatus[my_lp_problem.status])

for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))
