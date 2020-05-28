import csv
import matplotlib.pyplot as plt

# Obtener datos de archivo csv.
nomarch = "mercadolibreFinal.csv"
with open(nomarch, encoding="utf-8") as arch:  # iso8859-1, latin1, latin-1
    arch_csv = csv.reader(arch)
    datos = list(arch_csv)

# Datos eje x
# Datos eje y
x = []
y = []
for i, fila in enumerate(datos):  # 0, ["prod1", "precio1", "desc", "nuevo"]
    x.append(i)
    y.append(fila[-1])

# Construir la grafica
plt.plot(x, y)
# Mostrar la grafica
plt.show()
