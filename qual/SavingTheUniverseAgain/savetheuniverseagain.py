def calculate_damage(program):
    current_strength = 1
    total_damage = 0
    for instruction in program:
        if instruction == 'C':
            current_strength *= 2
        elif instruction == 'S':
            total_damage += current_strength
    return total_damage

def find_best_hack(program):
    for position in range(len(program) - 2, -1, -1):
        # The best hack is a shoot after a charge
        if program[position + 1] == 'S' and program[position] == 'C':
            return position
    return None

def perform_hack(program, position):
    return ''.join((program[:position], program[position + 1], program[position], program[position + 2:]))

def find_smallest_number_of_hacks(damage, program):
    current_program = program
    number_of_hacks = 0
    while calculate_damage(current_program) > damage:
        position = find_best_hack(current_program)
        if position is not None:
            current_program = perform_hack(current_program, position)
            number_of_hacks += 1
        else :
            return "IMPOSSIBLE"
    return number_of_hacks

def main():
    num_tests = int(input())
    for test in range(1, num_tests + 1):
        damage, program = input().split()
        result = find_smallest_number_of_hacks(int(damage), program)
        print("Case #{}: {}".format(test, result))

if __name__ == "__main__":
    main()
