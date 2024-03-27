def calcular_temperatura_promedio(ciudades, semanas, temperaturas):
  temperaturas_promedio = {}
  for ciudad in ciudades:
    temperaturas_promedio[ciudad] = []
    for semana in semanas:
      # Obtener las temperaturas de la ciudad y semana actual
      temperaturas_semana = temperaturas[ciudad][semana]

      # Calcular la temperatura promedio de la semana
      temperatura_promedio_semana = sum(temperaturas_semana) / len(temperaturas_semana)

      # Agregar la temperatura promedio a la lista
      temperaturas_promedio[ciudad].append(temperatura_promedio_semana)

  return temperaturas_promedio

# Ejemplo de uso
ciudades = ["Ciudad Puyo", "Ciudad Shell", "Ciudad Mera"]
semanas = [1, 2, 3, 4]
temperaturas = {
  "Ciudad Puyo": {
    1: [20, 21, 22, 23],
    2: [24, 25, 26, 27],
    3: [28, 29, 30, 31],
    4: [32, 33, 34, 35],
  },
  "Ciudad Shell": {
    1: [18, 19, 20, 21],
    2: [22, 23, 24, 25],
    3: [26, 27, 28, 29],
    4: [30, 31, 32, 33],
  },
  "Ciudad Mera": {
    1: [16, 17, 18, 19],
    2: [20, 21, 22, 23],
    3: [24, 25, 26, 27],
    4: [28, 29, 30, 31],
  },
}

temperaturas_promedio = calcular_temperatura_promedio(ciudades, semanas, temperaturas)

for ciudad, temperaturas_promedio_ciudad in temperaturas_promedio.items():
  print(f"Ciudad: {ciudad}")
  for semana, temperatura_promedio in enumerate(temperaturas_promedio_ciudad):
    print(f"Semana {semana + 1}: {temperatura_promedio}")


