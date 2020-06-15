import simpy
def cuarentena(env):
    print('Es lunes!')
    while True:

        print('las Mujeres salen en %d horas ' % env.now)
        tiempo_salida = 24
        yield env.timeout(tiempo_salida)

        print('Los Hombres salen en %d horas' % env.now)
        tiempo_salida = 24
        yield env.timeout(tiempo_salida)

# Creamos nuestro Entorno
env = simpy.Environment()
# Lo agregamos la función Cuarentena, al Proceso del Entorno
env.process(cuarentena(env))
# Ejecutamos agregando el tiempo de 144 Minutos
env.run(until=144)

print('ES DOMINGO SALEN AMBOS GENEROS')