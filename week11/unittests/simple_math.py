__author__ = 'kevin'
class SimpleMath():

    def add(self, a, b):
        return a + b

    def total(self,number_list):
        return sum(number_list)

if __name__ == '__main__':
    print SimpleMath.add(2, 5)
