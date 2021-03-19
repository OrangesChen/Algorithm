# 1603. 设计停车系统
# 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
#
# 请你实现 ParkingSystem 类：
#
# ParkingSystem(int big, int medium, int small)初始化ParkingSystem类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType)检查是否有carType对应的停车位。carType有三种类型：大，中，小，分别用数字1，2和3表示。
# 一辆车只能停在carType对应尺寸的停车位中。如果没有空车位，请返回false，否则将该车停入车位并返回true。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/design-parking-system


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # 解决方法1：
        # self.big = big
        # self.medium = medium
        # self.small = small
        # 解决方法2：
        self.park = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        # if carType == 1 and self.big > 0:
        #     self.big -= 1
        #     return True
        # elif carType == 2 and self.medium > 0:
        #     self.medium -= 1
        #     return True
        # elif carType == 3 and self.small > 0:
        #     self.small -= 1
        #     return True
        # else:
        #     return False
        if self.park[carType] == 0:
            return False
        self.park[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
