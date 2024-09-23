# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
# This is a Python script that converts SEZ to ECEF
#
# Parameters
# o_lat_deg - latitude in degrees
# o_lon_deg - longitude in degrees
# o_hae_km - height above the ellipsoid in kilometers
# s_km - SEZ s-component, kilometers
# e_km - SEZ e-component, kilometers
# z_km - SEZ z-component, kilometers

# Output:
# Print the ECEF x,y,z coordinates in kilometers from SEZ coords
#
# Written by Thomas Turon
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

import sys
import math

r_E_km = 6378.1363
e_E = 0.081819221456

def calc_denom(ecc,latitude_radians):
    return math.sqrt(1.0 - ecc**2 * math.sin(latitude_radians)**2)

o_lat_deg = ''
o_lon_deg = ''
o_hae_km = ''
s_km = ''
e_km = ''
z_km = ''

if len(sys.argv) == 7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km = float(sys.argv[3])
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print( \
        'Usage: ' \
        'python3 sez_to_ecef o_lat_deg o_lon_deg o_hae_km s_km e_km z_km' \
        )
    exit()

#writing the code

latitude_radians = o_lat_deg * (math.pi/180)
longitude_radians = o_lon_deg * (math.pi/180)

#ry matrix
ry_x = math.sin(latitude_radians) * s_km + (math.cos(latitude_radians)) * z_km
ry_y = e_km
ry_z = z_km * math.sin(latitude_radians) - s_km * math.cos(latitude_radians)

#2nd rotation
x_coord = ry_x * math.cos(longitude_radians) - ry_y * math.sin(longitude_radians)
y_coord = ry_x * math.sin(longitude_radians) + ry_y * math.cos(longitude_radians)
z_coord = ry_z

den = calc_denom(e_E,latitude_radians) # denominator

c_E = r_E_km/den
s_E = (r_E_km * (1 - e_E**2)) / den

rx = (o_hae_km + c_E) * math.cos(latitude_radians) * math.cos(longitude_radians)
ry = (o_hae_km + c_E) * math.cos(latitude_radians) * math.sin(longitude_radians)
rz = (o_hae_km + s_E) * math.sin(latitude_radians)

#ecef coord's
ecef_x_km = rx + x_coord
ecef_y_km = ry + y_coord
ecef_z_km = rz + z_coord

#print output
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)