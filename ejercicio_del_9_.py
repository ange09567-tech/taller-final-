from abc import ABC, abstractmethod


# --- CLASE BASE (Abstracta) ---
class Envio(ABC):

  def __init__(self, peso_kg: float, distancia_km: float):
    self.peso_kg = peso_kg
    self.distancia_km = distancia_km

  # Método abstracto que las subclases están obligadas a implementar (Polimorfismo)
  @abstractmethod
  def calcular_costo(self, monto_base: float) -> float:
    pass


# --- SUBCLASE: Envío Estándar ---
class EnvioEstandar(Envio):

  def calcular_costo(self, monto_base: float) -> float:
    # Aplica un recargo del 5% sobre el monto base
    recargo = monto_base * 0.05
    return monto_base + recargo


# --- SUBCLASE: Envío Express ---
class EnvioExpress(Envio):

  def calcular_costo(self, monto_base: float) -> float:
    # Aplica un recargo del 15% por servicio prioritario
    recargo = monto_base * 0.15
    return monto_base + recargo


# --- PRUEBA DEL PROGRAMA (Lista mixta y polimorfismo) ---
if __name__ == "__main__":
  # Creamos una lista mixta con diferentes tipos de envío
  envios = [
      EnvioEstandar(peso_kg=5.0, distancia_km=50.0),
      EnvioExpress(peso_kg=2.0, distancia_km=100.0),
      EnvioEstandar(peso_kg=10.0, distancia_km=25.0),
      EnvioExpress(peso_kg=4.5, distancia_km=200.0),
  ]

  monto_base_general = 50000.0  # Monto base de ejemplo en pesos

  print(
      f"--- COTIZACIONES DE ENVÍO (Monto Base: ${monto_base_general:,.2f}) ---"
      "\n"
  )

  # Recorremos la colección ejecutando el método calcular_costo de forma polimórfica
  for i, envio in enumerate(envios, start=1):
    tipo = (
        "Envío Estándar (+5%)"
        if isinstance(envio, EnvioEstandar)
        else "Envío Express (+15%)"
    )
    costo_total = envio.calcular_costo(monto_base_general)

    print(f"{i}. Tipo: {tipo}")
    print(f"   - Peso: {envio.peso_kg} kg | Distancia: {envio.distancia_km} km")
    print(f"   - Costo Final Calculado: ${costo_total:,.2f}\n")