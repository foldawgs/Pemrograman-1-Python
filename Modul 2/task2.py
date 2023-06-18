#mencari volume kerucut
print("\n-----Volume Kerucut-----")
r_kerucut = float(input(f"Masukan jari jari kerucut: "))
t_kerucut = float(input(f"Masukan tinggi kerucut: "))

l_kerucut = 1/3 * 3.14 * r_kerucut * r_kerucut * t_kerucut

print(f"\nVolume kerucutnya : {l_kerucut}")

#mencari volume tabung
print("\n-----Volume Tabung-----")
r_tabung = float(input(f"Masukan jari jari limas: "))
t_tabung = float(input(f"Masukan tinggi limas: "))

l_limas = 3.14 * r_tabung * r_tabung * t_tabung
print(f"\nVolume Limas persegi: ", l_limas)


