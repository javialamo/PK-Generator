
f = open("object.scad","w")

Tipo = input("Choose pendant/keychain\n")
Forma = input("Choose circle/square/rounded square\n")
Diameter = input("Write desired diameter/side in milimeters\n")
Decision = input("Do you want to import a relief? (yes/no)\n")

if Decision.lower()=='yes' or Decision.lower()=='y':
	print()
	print('Reliefs should be stl files')
	Relief = input("What relief do you want to import\n")
	Folder = input("In which folder is this relief\n")
f.write ('diam=')
f.write (Diameter)
f.write (';')
f.write ('\n')
f.write ('alt=2*(diam+15)/50;\n')

if Forma.lower()=='circle':
	f.write ('cylinder(r=diam/2, h=alt);\n')
elif Forma.lower()=='square':
	f.write ('translate([0,0,alt/2])\n')
	f.write ('cube([diam,diam,alt],center=true);\n')
else:
	f.write ('translate([0,0,alt/2])\n')
	f.write ('minkowski(){\n')
	f.write ('cube([diam-4*alt,diam-4*alt,alt],center=true);\n')
	f.write ('cylinder(r=2*alt,h=alt/20);\n')
	f.write ('}\n')

f.write ('translate([0,-diam/2,alt/2])\n')

if Tipo.lower()=='pendant':
	f.write ('difference(){\n')
	f.write ('union(){\n')
	f.write ('cube([diam/5,diam/5,alt],center=true);\n')
	f.write ('translate([0,-diam/20,alt])\n')
	f.write ('cube([diam/5,diam/10,alt],center=true);\n')
	f.write ('}\n')
	f.write ('translate([-4*alt,-alt+(8/diam),alt/2])\n')
	f.write ('rotate([0,90,0])\n')
	f.write ('cylinder(r=alt/2,h=diam/2);\n')
	f.write ('}\n')
else:
	f.write ('difference(){\n')
	f.write ('cube([diam/5,diam/5,alt],center=true);\n')
	f.write ('translate([0,0,0])\n')
	f.write ('cube([diam/10,diam/10,2*alt],center=true);\n')
	f.write ('}\n')

if Decision.lower()=='yes' or Decision.lower()=='y':
	f.write ('translate([0,0,alt])\n')
	f.write ('rotate([0,0,0])\n')
	f.write ('scale([0.6,0.6,1])\n')
	f.write ('import("../')
	f.write (Folder)
	f.write ('/')
	f.write (Relief)
	f.write ('");\n')

f.close()

print('All ok, your file is object.scad')
print('If you import a relief you can easily scale, rotate or translate it')
