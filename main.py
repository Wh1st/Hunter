from sim.sim_surv import SurvSim


sim = SurvSim()


if __name__ == '__main__':
    sim.sim(50)
    sim.report()
