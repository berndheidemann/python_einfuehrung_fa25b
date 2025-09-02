import math

g = 9.81
s= 80
t_squared = 2 * s / g
t = math.sqrt(t_squared)      # math.sqrt zieht die Wurzel einer Zahl

print("Zeit bis Aufprall: ", t)

speed_m_s=t*g
print("Aufprallgeschwindigkeit in m/s: ", speed_m_s)

speed_kmh=speed_m_s*3.6
print("Aufprallgeschwindigkeit in kmh: ", speed_kmh)
