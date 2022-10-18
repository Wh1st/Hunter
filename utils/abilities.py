

class Ability:
    def __init__(self, name, cd):
        self.name = name
        self.p = cd
        self.cd = cd

    def update(self, dt):
        self.p += dt

    def cast(self):
        self.p = 0

    def is_ready(self):
        return self.p >= self.cd


def new_surv_abilities():
    return {
        'exs': Ability('exs', 6),
        'ses': Ability('ses', 0),
        'ext': Ability('ext', 24),
        'mus': Ability('mus', 10),
        'sts': Ability('sts', 0),
    }


class Debuff:
    def __init__(self, name, duration, tick_rate):
        self.name = name
        self.p = 0
        self.duration = duration
        self.tick_rate = tick_rate

    def update(self, dt):
        self.p += dt

    def is_over(self):
        return self.p >= self.duration


class ExplosiveTrap:

    def __init__(self, lnl_proc_chance=0.2, arm_interval=(1, 2.2)):
        self.state = 0
        self.lnl_proc_chance = lnl_proc_chance
        self.arm_interval = arm_interval
        self.p = 0
        self.tick_rate = 2

    def update(self, dt):
        if self.state == 2:
            return
        if self.state == 0:
            self.p += dt
            if self.p > 1.5:
                self.state = 1
                self.p = 0

