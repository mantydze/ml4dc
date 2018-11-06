Genetic algorithm for NN hyper-parameter optimization

* Create #POPULATION_SIZE networks with random parameters
* Train, calculate fitness, sort by AUC score
* Crossover best networks(parents) to create offspring network
* Repeat for #N_GENERATIONS times
