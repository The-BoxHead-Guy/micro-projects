class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = nueva_edad

    def hablar(self):
        return "..."

    def info(self):
        return f"Nombre Animal: {self.nombre}, Edad Animal: {self.edad}"


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"

    def atacar(self):
        print("El perro muerde")

    def info(self):
        return f"{super().info()}, Raza: {self.raza}"


# Uso
perro = Perro("Rex", 5, "Labrador")

# Acceso normal (parece atributo, pero está controlado)
perro.nombre = "Max"

print(f"Mi perro se llama {perro.nombre}")
print(f"Mi perro es de raza {perro.raza}")
print(f"Mi perro tiene {perro.edad} años")
print(f"\nEsta es la información de mi perro \n{perro.info()}")
