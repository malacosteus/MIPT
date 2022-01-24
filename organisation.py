class Organisation(object):

    def __init__(self, dep_nmbr):

        self.dep_nmbr = dep_nmbr
        self.org = {}
        for i in range(self.dep_nmbr):
            self.org.update({'Department'+str(i+1):{'employees':{}, 'units':{}}})

    def show_all_deps(self):
        return self.org.keys()

    def get_nmbr_deps(self):
        return len(self.org)

    def add_empl(self, dep_n, name, pos, sal, unt, hst, chief):
        self.org['Department'+str(dep_n)]['employees'].update({name:{'position': pos, 'salary': sal, 'unit': unt, 'history': hst, 'chief': chief}})

    def fire_empl(self, dep_n, name):
        del self.org['Department'+str(dep_n)]['employees'][name]

    def get_all_employees_of_dep(self, dep_n):
        return self.org['Department'+str(dep_n)]['employees']

    def chg_sl(self, dep_n, name, new_sl):
        self.org['Department' + str(dep_n)]['employees'][name]['salary'] = new_sl

    def show_all_pos(self, pos):
        ls = []
        for dp in self.org.keys():
            for prsn in self.org[dp]['employees'].keys():
                if self.org[dp]['employees'][prsn]['position'] == pos:
                    ls.append([dp, prsn])
        return ls


if __name__ == "__main__":
    org1 = Organisation(2)
    print(org1.show_all_deps())
    org1.add_empl(1, 'Ann', 'manager', 25000, 'unitname1', [('trainee', '2020, 28, 9'), ('manager', '2020, 28, 12')], 'Lynn')
    org1.add_empl(1, 'Helen', 'manager', 25000, 'unitname2', [('trainee', '2020, 28, 9'), ('manager', '2020, 28, 12')], 'Lynn')
    print(org1.get_all_employees_of_dep(1))
    #org1.fire_empl(1, 'Helen')
    #print(org1.get_all_employees_of_dep(1))
    print(org1.show_all_pos('manager'))