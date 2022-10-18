from utils.abilities import Ability, new_surv_abilities


class SurvSim:
    def __init__(self):
        self.t = 0
        self.sim_time = 0
        self.dt = 0.001

        self.abilities = new_surv_abilities()

        self.serpent_sting = 0
        self.explosive_trap = 0

        self.gcd = 0
        self.castbar = 0
        self.timeline = []

    def sim(self, sim_time):
        self.sim_time = sim_time
        while self.t <= self.sim_time:
            self.update(self.dt)

    def update(self, dt):
        self.t += dt
        self.update_abilities(dt)
        self.update_gcd(dt)
        self.update_debuffs(dt)
        self.rotation()

    def update_gcd(self, dt):
        self.gcd -= dt
        self.castbar -= dt

    def update_abilities(self, dt):
        for ab in self.abilities.values():
            ab.update(dt)

    def update_debuffs(self, dt):
        self.serpent_sting -= dt
        self.explosive_trap -= dt

    def cast(self, name):
        self.abilities[name].cast()
        self.timeline.append((self.t, name))
        self.gcd = 1.5 if name == 'ext' else 1.5
        if name == 'ses':
            self.serpent_sting = 15
        if name == 'ext':
            self.explosive_trap = 20
        if name == 'sts':
            self.castbar = 1.7

    def rotation(self):
        if self.gcd > 0:
            return
        if self.castbar > 0:
            return

        if self.abilities['exs'].is_ready():
            self.cast('exs')
            return

        if self.serpent_sting <= 0:
            self.cast('ses')
            return

        if self.abilities['ext'].is_ready():
            self.cast('ext')
            return

        if self.abilities['mus'].is_ready():
            self.cast('mus')
            return

        self.cast('sts')

    def report(self):
        print('sim %i seconds' % self.sim_time)
        print('timeline:')
        for t in self.timeline:
            print('%.3f - %s' % (t[0], t[1]))
