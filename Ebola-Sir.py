import numpy as np
import matplotlib.pyplot as plt

def SEIR(duration, h, beta, sigma, gamma, initial_population):
    N = int(duration / h)
    susceptibles, exposed, infected, recovered = [], [], [], []

    for i in range(N):
        # Calcular as taxas de transição entre os estados (S->E, E->I, I->R)
        SEIR_rates = [
            -beta * initial_population[0] * initial_population[2] / sum(initial_population),
            beta * initial_population[0] * initial_population[2] / sum(initial_population) - sigma * initial_population[1],
            sigma * initial_population[1] - gamma * initial_population[2],
            gamma * initial_population[2]
        ]

        # Atualizar a população com base nas taxas de transição
        for j in range(len(initial_population)):
            initial_population[j] += SEIR_rates[j] * h

        # Adicionar os valores atualizados de S, E, I e R às listas
        susceptibles.append(initial_population[0])
        exposed.append(initial_population[1])
        infected.append(initial_population[2])
        recovered.append(initial_population[3])

        # Imprimir os valores a cada iteração
        print(f"Iteração {i + 1}: S={initial_population[0]}, E={initial_population[1]}, I={initial_population[2]}, R={initial_population[3]}")

    return susceptibles, exposed, infected, recovered

# Parâmetros do modelo SEIR
duration = 36
h = 2
beta = 0.30
sigma = 0.34
gamma = 0.13
initial_population = [100, 2, 0, 0]  # [Suscetíveis, Expostos, Infectados, Recuperados]

# Simulação do modelo SEIR
susceptibles, exposed, infected, recovered = SEIR(duration, h, beta, sigma, gamma, initial_population)

# Criar pontos de tempo com base no número de pontos em suscetíveis
time_points = np.linspace(0, duration, len(susceptibles))

# Plotar os resultados
plt.plot(time_points, susceptibles, label='Suscetíveis')
plt.plot(time_points, exposed, label='Expostos')
plt.plot(time_points, infected, label='Infectados')
plt.plot(time_points, recovered, label='Recuperados')

plt.title('Modelo SEIR de Epidemias')
plt.xlabel('Tempo (dias)')
plt.ylabel('População')
plt.legend()
plt.show()
