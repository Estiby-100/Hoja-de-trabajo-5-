import simpy
import random
import statistics
from process import Job

RANDOM_SEED = 42

class JobSimulator:

    def __init__(self, total_jobs, arrival_rate,
                 memory_size=100,
                 cpu_units=1,
                 instructions_per_cycle=3):

        self.total_jobs = total_jobs
        self.arrival_rate = arrival_rate
        self.memory_size = memory_size
        self.cpu_units = cpu_units
        self.instructions_per_cycle = instructions_per_cycle

        self.env = simpy.Environment()

        self.memory = simpy.Container(
            self.env,
            init=memory_size,
            capacity=memory_size
        )
        self.cpu = simpy.Resource(
            self.env,
            capacity=cpu_units
        )

        self.results = []


    def generate_jobs(self):

        for i in range(self.total_jobs):

            wait = random.expovariate(1.0 / self.arrival_rate)
            yield self.env.timeout(wait)

            job = Job(
                job_id=i,
                env=self.env,
                ram=self.memory,
                cpu=self.cpu,
                results=self.results,
                instructions_per_cycle=self.instructions_per_cycle
            )

            self.env.process(job.lifecycle())


    def run(self):

        random.seed(RANDOM_SEED)

        self.env.process(self.generate_jobs())
        self.env.run()


    def calculate_results(self):

        average = statistics.mean(self.results)

        if len(self.results) > 1:
            std_dev = statistics.stdev(self.results)
        else:
            std_dev = 0

        return average, std_dev