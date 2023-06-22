# play russian roulette with a 6 shooter
# 6 chambers in the gun, 1 bullet   1/6 chance of dying each time you pull the trigger  5/6 chance of living
# 1/6 * 1/6 * 1/6 * 1/6 * 1/6 * 1/6 = 1/46656 chance of dying
# 46656/46657 chance of living
# 99.9981% chance of living
death_count = 0
lived_count = 0
round_count = 0
red = "\033[1;31;40m"
green = "\033[1;32;40m"
blue = "\033[1;34;40m"
while round_count < 6:
    import random
    chambers = [1, 2, 3, 4, 5, 6]
    people = ["alex", "marcel", "fred", "toby", "florim", "mirco"]
    active_membr = random.choice(people)
    bullet = random.choice(chambers)
    # print(bullet)
    if bullet == 1:
        print(red, "go down", active_membr, "you died")
        round_count += 1
        death_count += 1
    else:
        print(green, "hello", active_membr, "you lived")
        round_count += 1
        lived_count += 1
print(blue, "you died", death_count, "times")
print(blue, "you lived", lived_count, "times")