from Singleton import Singleton

instancia_a = Singleton.get_instance()
instancia_b = Singleton.get_instance()

if (instancia_a is instancia_b):
    print("instancia_a e instancia_b são a mesma instância")
else:
    print("instancia_a e instancia_b não são a mesma instância")