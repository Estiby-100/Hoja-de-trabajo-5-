import random

class Job:

    def __init__(self, job_id, env, ram, cpu, results, instructions_per_cycle=3):

        self.job_id = job_id
        self.env = env
        self.ram = ram
        self.cpu = cpu
        self.results = results
        self.instructions_per_cycle = instructions_per_cycle

        self.memory_required = random.randint(1, 10)
        self.instructions_left = random.randint(1, 10)

        self.start_time = 0


    def lifecycle(self):

        self.start_time = self.env.now

        
        yield self.ram.get(self.memory_required)

        while self.instructions_left > 0:

            
            with self.cpu.request() as req:
                yield req

                
                yield self.env.timeout(1)

                self.instructions_left -= self.instructions_per_cycle

                if self.instructions_left < 0:
                    self.instructions_left = 0

            if self.instructions_left == 0:
                break

            
            if random.random() < (1.0 / 21.0):
                wait_time = random.randint(1, 5)
                yield self.env.timeout(wait_time)

       
        yield self.ram.put(self.memory_required)

        total_time = self.env.now - self.start_time
        self.results.append(total_time)