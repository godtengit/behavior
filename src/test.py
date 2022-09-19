from HX711 import AdvancedHX711, Rate

with AdvancedHX711(2, 3, -370, -367471, Rate.HZ_80) as hx:
    while True:
        print(hx.weight(1))
