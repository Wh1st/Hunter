

def calc_haste():

    speed = 2 / (1 + 15/100)
    return speed


class Sim:

    def __init__(self, st_ct=1.7):
        self.st_ct = st_ct
        self.casts = []

        self.esp = 0
        self.asp = 0
        self.etp = 0
        self.ssp = 0
        self.gcd = 0
        self.st_c = 0
        self.lnl_icd = 0
        self.lnl = 0

        self.t = 0
        self.dt = 0.001

    def sim(self, sim_time=100):
        print('start sim: %.2f' % sim_time)
        self.t = -self.dt
        while self.t < sim_time:
            self.time_step()
            if self.gcd > 0 or self.st_c > 0:
                continue
            if self.esp <= 0:
                self.cast_ability('es')
            elif self.ssp <= 0:
                self.cast_ability('ss')
            elif self.etp <= 0:
                self.cast_ability('et')
            elif self.asp <= 0:
                self.cast_ability('as')

    def cast_ability(self, name):
        self.casts.append((name, self.t))
        self.gcd = 1.5

        if name == 'es':
            self.esp = 6
        elif name == 'as':
            self.asp = 10
        elif name == 'ss':
            self.ssp = 15
        elif name == 'et':
            self.etp = 24

    def time_step(self):
        self.t += self.dt
        self.esp -= self.dt
        self.asp -= self.dt
        self.ssp -= self.dt
        self.etp -= self.dt
        self.gcd -= self.dt
        self.st_ct -= self.dt
        self.lnl_icd -= self.dt

    def report(self):
        esc = 0
        ssc = 0
        etc = 0
        asc = 0
        stc = 0
        for c in self.casts:
            if c[0] == 'es':
                esc += 1
            elif c[0] == 'ss':
                ssc += 1
            elif c[0] == 'et':
                etc += 1
            elif c[0] == 'as':
                asc += 1
            elif c[0] == 'st':
                stc += 1

        print('casts:')
        print('es: %i' % esc)
        print('ss: %i' % ssc)
        print('et: %i' % etc)
        print('as: %i' % asc)
        print('st: %i' % stc)


if __name__ == '__main__':
    sim = Sim()
    sim.sim()
    sim.report()
    print(sim.casts)


