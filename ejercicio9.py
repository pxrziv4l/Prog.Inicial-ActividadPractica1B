print("\nCalculador de promedio estudiantil.\n")
nombre_alumno = input("Nombre del alumno:")
primer_nota = float(input("Primer trimestre:"))
segunda_nota = float(input("Segundo trimestre:"))
tercer_nota = float(input("Tercer trimestre:"))
promedio = (primer_nota + segunda_nota + tercer_nota) / 3
print("\nPromedio del alumno",nombre_alumno)
print("\nNotas:",primer_nota,",",segunda_nota,",",tercer_nota)
print("Nota Final: {:.2f}".format(promedio))