import random


def file_length(file_name):
    lines = 0
    with open(file_name) as file:
        for line in file:
            if line != '\n':
                lines += 1
    return lines


def get_word(file_name, line_number):
    file = open(file_name)
    line = file.readlines()
    return line[line_number]


def random_idea(noun, verb, noun2):
    print("A(n) " + noun + " that " + verb + "s", noun2)


rand_n_list = random.sample(range(0, file_length("nouns.txt")), 10)
rand_v_list = random.sample(range(0, file_length("verbs.txt")), 10)
rand_n2_list = random.sample(range(0, file_length("nouns.txt")), 10)

print("Here are your ideas:")
print("")

for i in range(10):
    noun = get_word("nouns.txt", rand_n_list[i]).rstrip("\n")
    verb = get_word("verbs.txt", rand_v_list[i]).rstrip("\n")
    noun2 = get_word("nouns.txt", rand_n2_list[i]).rstrip("\n")
    random_idea(noun, verb, noun2)
