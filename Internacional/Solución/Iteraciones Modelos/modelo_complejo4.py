import pulp

my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)

# ------------------------- VARIABLES ------------------------- #
# Numero de personas, queremos maximizar
NP = pulp.LpVariable('Numero Personas', lowBound=0, cat='Continuous')


# ------ COMIDA ------ #
# Cantidad de comida que se produce, cal/año
Nc = pulp.LpVariable('Numero Comida', lowBound=0, cat='Continuous')
# Espacio que se ocupa para producir la comida en metros cuadrados
Ec = pulp.LpVariable("Espacio Comida", lowBound=0, cat='Continuous')

# ------ VIVIENDAS ------ #
# Numero de viviendas
Nv = pulp.LpVariable("Numero Viviendas", lowBound=0, cat='Continuous')
# Espacio total que ocupan las viviendas en el area solo habitable en metros cuadrados
Ev1 = pulp.LpVariable("Ev1", lowBound=0, cat='Contirnuous')
# Espacio total que ocupan las viviendas en el area solo cultivable en metros cuadrados
Ev2 = pulp.LpVariable("Ev2", lowBound=0, cat='Contirnuous')
# Espacio total que ocupan las viviendas en total
Ev = pulp.LpVariable("Ev2", lowBound=0, cat='Contirnuous')


# ------ AGUA ------ #
# Cantidad de agua potable producida, lts/año
Nap = pulp.LpVariable("Nap", lowBound=0, cat='Continuous')
# Espacio que se ocupa para procesar el agua en metros cuadrados
Eap = pulp.LpVariable("Eap", lowBound=0, cat='Continuous')


# ------------------------- PARAMETROS ------------------------- #
# Porcentaje cultivable de la superficie terrestre del planeta
Pc = 0.38
# Porcentaje habitable de la superficie terrestre de la tierra, metros cuadrados
Ph = 0.33
# Superficie terrestre del planeta
T = 100
# Kilocalorias que una persona necesita al dia
X1 = 1/1500000
# Espacio de una vivienda
Epv = 1/1
# Rendimiento de la comdia por metro cuadrado, 2743
Rc = 0.7
# espacio habitable de la tierra
Th = T * 0.71
# espacio cultivable del espacio habitable de la tierra
Tc = Th * 0.38
caca = (T*0.71)+(T*0.38*0.71)

T1 = Th - Tc  # el area habitable menos el area cultivable dentro del area habitable
T2 = Tc  # el area cultivable

# ------------------------- FUNCION OBJETIVO ------------------------- #
my_lp_problem += NP, "Z"

# ------------------------- RESTRICCIONES ------------------------- #


my_lp_problem += Ev == Ev1 + Ev2

my_lp_problem += T1 >= Ev1
my_lp_problem += T2 >= Ec + Ev2

# ------ VIVIENDAS ------ #
my_lp_problem += NP <= Nv  # el numero de personas tiene que ser menor o igual a las viviendas (1:1)
my_lp_problem += Ev <= caca  # el area que ocupan las viviendas tiene que ser menor o igual al espacio habitable
my_lp_problem += Nv == Ev*Epv  # espacio que ocupan las casas partido en el numero de casas


# ------ COMIDA ------ #
my_lp_problem += NP <= Nc*X1  # numero de personas tiene que ser menor que la comida que se produce/lo que 1 come
my_lp_problem += Ec <= Tc  # Ec tiene que ser menor al area cultivable
my_lp_problem += Nc == Ec*Rc  # espacio ocupado en comida por lo que produce cada espacio = total comida prod.
my_lp_problem += Ec + Ev <= Th  # suma de areas tiene que ser menor o igual a area habitable
my_lp_problem += Ec <= Tc  # Tc = area cultivable del area habitable (hacen overlap)


# ------ AGUA ------ #



print(my_lp_problem.solve())
print(pulp.LpStatus[my_lp_problem.status])

for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print(T1)
print(T2)
