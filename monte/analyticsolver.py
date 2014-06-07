from distribution import Distribution
import random

class AnalyticSolver:
    def find_distribution(self,operation, distributions):
        operations = {"+":self.add, "*":self.mul, "/":self.div, '-':self.sub}
        return operation[operations](distributions)

    def has_analytical_solution(operation, distributions):

        def all_are_nums_or_gaussian(distributions):
            def is_num(dis):
                return isinstance(dis, int) or isinstance(dis,float) or isinstance(dis,long)
            def is_gaussian(dis):
                return isinstance(dis, Distribution) and dis.dist == random.gauss
            return all([is_num(d) or is_gaussian(d) for d in distributions])
        return all_are_nums_or_gaussian(distributions)


