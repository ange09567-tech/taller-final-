class Producto:

  def __init__(self, nombre: str):
    # Atributos privados (ocultos al exterior usando doble guion bajo)
    self.__nombre = nombre
    self.__precios_historicos = []

  # Getter para consultar el nombre del producto
  @property
  def nombre(self):
    return self.__nombre

  # Getter para consultar el historial de precios
  @property
  def precios_historicos(self):
    return self.__precios_historicos

  # Propiedad 'precio' con su respectivo Setter para actualizar y validar
  @property
  def precio(self):
    if not self.__precios_historicos:
      return 0
    return self.__precios_historicos[-1]  # Retorna el precio más reciente

  @precio.setter
  def precio(self, nuevo_precio: float):
    # Validación: impide valores negativos o mayores a $10,000
    if 0 <= nuevo_precio <= 10000:
      self.__precios_historicos.append(nuevo_precio)
      print(f"✅ Precio ${nuevo_precio:,.2f} registrado con éxito.")
    else:
      print(
          f"⚠️ Advertencia: El precio ${nuevo_precio:,.2f} está fuera del rango"
          " permitido (0 - $10,000). No se registró."
      )

  # Propiedad para calcular el precio promedio automáticamente
  @property
  def precio_promedio(self) -> float:
    if not self.__precios_historicos:
      return 0.0
    return sum(self.__precios_historicos) / len(self.__precios_historicos)


# --- PRUEBA DEL PROGRAMA ---
if __name__ == "__main__":
  # Creamos un producto
  mi_producto = Producto("Camisa deportiva")

  print(f"Producto creado: {mi_producto.nombre}\n")

  # Intentamos registrar precios válidos
  mi_producto.precio = 1500.0
  mi_producto.precio = 2000.0

  # Intentamos registrar precios inválidos (para probar el filtro del setter)
  mi_producto.precio = -500.0  # Negativo (Debe fallar)
  mi_producto.precio = 15000.0  # Mayor a $10,000 (Debe fallar)

  # Mostramos resultados
  print(f"\nHistorial de precios: {mi_producto.precios_historicos}")
  print(f"Precio promedio: ${mi_producto.precio_promedio:,.2f}")