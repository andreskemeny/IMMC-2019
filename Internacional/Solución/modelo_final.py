import pulp

my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)

######### -------- VARIABLES -------- ########
# Numero de personas, queremos maximizar
NP = pulp.LpVariable('NP', lowBound=0, cat='Continuous')
# Cantidad de comida que se produce, cal/año
Nkcal = pulp.LpVariable('Nkcal', lowBound=0, cat='Continuous')
# Espacio que se ocupa para producir la comida en metros cuadrados
Ekcal = pulp.LpVariable("Ekcal", lowBound=0, cat='Continuous')
# Numero de viviendas
Nv = pulp.LpVariable("Nv", lowBound=0, cat='Continuous')
# Espacio total que ocupan las viviendas en metros cuadrados
Ev = pulp.LpVariable("Ev", lowBound=0, cat='Continuous')
# Cantidad de oxigeno que se produce, litros/año
No2 = pulp.LpVariable("No2", lowBound=0, cat='Continuous')
# Espacio para produccion de oxigeno
Eo2 = pulp.LpVariable("Eo2", lowBound=0, cat='Continuous')
# Cantidad de agua producida litros/año
Nap = pulp.LpVariable("Nap", lowBound=0, cat='Continuous')
# Espacio que se usa para procesar/tratar el agua
Eap = pulp.LpVariable("Eap", lowBound=0, cat='Continuous')
# Cantidad de ropa producida al año
Nr = pulp.LpVariable("Nr", lowBound=0, cat='Continuous')
# espacio ocupado para producir ropa
Er = pulp.LpVariable("Er", lowBound=0, cat='Continuous')
# energia necesaria para satisfacer lo neesario
Ne = pulp.LpVariable("Ne", lowBound=0, cat='Continuous')
# espacio ocupado para producir la energia
Ee = pulp.LpVariable("Ee", lowBound=0, cat='Continuous')

######### -------- PARAMETROS -------- ########
# Superficie terrestre del planeta
T = 148940000000000
# Kilocalorias que una persona necesita al año547500
Ckcal = 1/912500
# Litros de oxigeno que una persona necesita al año, solo 28% porque el otro 72 viene de algas marinas
Co2 = 1/56210
# Espacio de una vivienda, 4.5 = tamaño de una celda de la carcel
Mv = 1/25
# Cantidad de ropa que una persona necesita al año en m2
Cr = 1/(56)
# Cantidad de agua que una persona necesita al año en litros
Cap = 1/54750
# energia necesitada por persona en m^2
Ce = 1/8875469
# Rendimiento de la comdia por metro cuadrado, en el año 2743
Rkcal = 2743
# Rendimiento del oxigeno por metro cuadrado, en el año
Ro2 = 162
# Rendimiento del agua potablo por metro cuadrado, en el año
Rap = 321064
# rendimiento de la ropa por metro cuadrado, en el año
Rr = 100000
# rendimiento de energia, watts que se producen al año por m^2
Ren = 4.7125
# tierra habitable (71% de la superficie terrestre)
Th = T * 0.71
# tierra cultivable (37% de la superficie terrestre)
Tc = T * 0.37

# -------- FUNCION OBJETIVO -------- #
my_lp_problem += NP, "Z"

# -------- RESTRICCIONES -------- #

# ---- RESTRICCIONES GENERALES ---- #
# suma de areas que van en espacio habitable tiene que ser menor o igual a Th
my_lp_problem += Ev + Eo2 + Eap <= Th
# suma de areas que van en espacio cultivable tienen que ser menor o igual a Tc
my_lp_problem += Ekcal <= Tc
# suma de todas las areas tiene que ser menor o igual a la superficie
my_lp_problem += Eo2 + Ekcal + Ev + Eap <= T

# ---- RESTRICCIONES PARA LAS VIVIENDAS ---- #
# el numero de personas tiene que ser menor o igual a las viviendas (1:1)
my_lp_problem += NP <= Nv
# espacio que ocupan las casas partido en el numero de casas
my_lp_problem += Nv == Ev*Mv

# ---- RESTRICCIONES PARA LA COMIDA ---- #
# numero de personas tiene que ser menor que la comida que se produce/lo que 1 come
my_lp_problem += NP <= Nkcal*Ckcal
# espacio ocupado en comida por lo que produce cada espacio = total comida prod.
my_lp_problem += Nkcal == Ekcal*Rkcal

# ---- RESTRICCIONES PARA EL OXIGENO ---- #
# numero de personas es dependiente de la cantidad de oxigeno que se produce necesa
my_lp_problem += NP <= No2*Co2
# cantidad de ixgeno producido es igual al espacio que usa por el rendimiento
my_lp_problem += No2 == Eo2*Ro2

# ---- RESTRICCIONES PARA EL AGUA ---- #
# numero de personas tiene que ser menor que el agua que se produce/lo que 1 toma
my_lp_problem += NP <= Nap*Cap
# cantidad de agua producida es igual al espacio que usa por el rendimiento
my_lp_problem += Nap == Eap*Rap

# ---- RESTRICCIONES PARA LA ROPA ---- #
# numero de personas tiene que ser menor que la ropa que se produce/lo que 1 necesita
my_lp_problem += NP <= Nr*Cr
# cantidad de ropa producida es igual al espacio que usa por el rendimiento
my_lp_problem += Nr == Er*Rr

# ---- RESTRICCIONES PARA LA ENERGIA ---- #
# numero de personas tiene que ser menor que la energia que se produce/energia necesaria por persona
my_lp_problem += NP <= Ne*Ce
# cantidad de energia producida es igual al espacio que usa por el rendimiento
my_lp_problem += Ne == Ee*Ren

print(my_lp_problem.solve())
print(pulp.LpStatus[my_lp_problem.status])

for variable in my_lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))
