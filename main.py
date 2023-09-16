# def num_in_sequences(sequence):
#     list = []
#     count = 1
#     current = sequence[0]
#     for num in sequence[1:]:
#         if current == num:
#             count += 1
#         else:
#             list.append(count)
#             count = 1
#             current = num
#     list.append(count)
#     return list
#
# print(num_in_sequences([1, 1, 1, 2, 2, 2, 2, 3, 5, 5]))

# go through each bag and check for letters
# split list and turn into set
# turn back into a list
# count each
# tally up letters and compare to see who has the most
# return the ones with the most

# def bags_of_skittles(skittles):
#     colors_count = {"O": 0, "G": 0, "Y": 0, "R": 0, "P": 0}
#     for bag in skittles:
#         for color in colors_count:
#             if color in bag:
#                 colors_count[color] += 1
#     return [color for color, count in colors_count.items() if count == max(colors_count.values())]
#

# print(bags_of_skittles(["PYYPR", "GRPYY", "OPOOP", "GOOGR", "OYYGO"]))

#
# def encode(password):
#     password = [[], []]
#     for i, num in enumerate(password):
#         if i % 2 == 0:
#             password[0].append(int(num))
#         else:
#             password[1].append(int(num))
#     return password
#
# print(encode(["16024583"]))

#
# class Calculator:
#     def __init__(self):
#         self.value = 0.0
#
#     def add(self, num):
#         self.value += num
#     def subtract(self, num):
#         self.value -= num
#     def divide(self, num):
#         self.value /= num
#     def multiply(self, num):
#         self.value *= num
#     def clear(self):
#         self.value = 0.0
#     def get_value(self):
#         return self.value
#     def set_value(self, num):
#         self.value = num

class Gradebook:
    def __init__(self, grades):
        self.grade = grade

    def averages(self):
        divisor = len(self.grades)
        sum = 0
        for i in grades:
            sum += i
        average = sum/divisor


        if len(self.grades) % 2 == 0:
            med_idx = len(self.grades) / 2
            median = self.grades[med_idx]
        else:
            idx1 = len(self.grades) // 2
            idx2 = idx1 + 1
            median = (self.grades[idx1] + self.grades[idx2]) / 2

        return (average, median)

grades1 = [88, 80, 90]
print(grades1.averages())



