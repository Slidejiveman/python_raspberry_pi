#4_9_stats
def stats(numbers):
    numbers.sort()
    # the negative index counts backwards from
    # the end of the array! way to go Python!
    return (numbers[0], numbers[-1])

list = [5, 45, 12, 1, 78]
min, max = stats(list)
print(min)
print(max)
