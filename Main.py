from system import JobSimulator

TOTAL_JOBS = 100
ARRIVAL_RATE = 10
MEMORY_SIZE = 100
CPU_UNITS = 1
INSTRUCTIONS_PER_CYCLE = 3


if __name__ == "__main__":

    simulator = JobSimulator(
        total_jobs=TOTAL_JOBS,
        arrival_rate=ARRIVAL_RATE,
        memory_size=MEMORY_SIZE,
        cpu_units=CPU_UNITS,
        instructions_per_cycle=INSTRUCTIONS_PER_CYCLE
    )

    simulator.run()

    avg, std = simulator.calculate_results()

    print("Jobs: " + str(TOTAL_JOBS))
    print("Arrival rate: " + str(ARRIVAL_RATE))
    print("Memory: " + str(MEMORY_SIZE))
    print("CPU units: " + str(CPU_UNITS))
    print("Instructions per cycle: " + str(INSTRUCTIONS_PER_CYCLE))
    print("Average time: " + str(round(avg, 2)))
    print("Std deviation: " + str(round(std, 2)))