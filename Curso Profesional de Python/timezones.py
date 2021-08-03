from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico__date = datetime.now(mexico_timezone)
print("Ciudad de México_: ", mexico__date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas__date = datetime.now(caracas_timezone)
print("Caracas: ", caracas__date.strftime("%d/%m/%Y, %H:%M:%S"))