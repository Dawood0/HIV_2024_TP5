# print something with red color

# print("\033[91m This is red text \033[0m")
import google.generativeai as genai
from common.llm_test_generator import LLMTestGenerator
from common.prompt_generator import PromptGenerator
from common.abstract_executor import AbstractExecutor
from file_name_check import file_name_check
import importlib
from to_test.number_to_words import number_to_words



import random
# def test_number_to_words(number_to_words):
#     assert number_to_words(123) == "One Hundred Twenty Three"
#     assert number_to_words(12345) == "Twelve Thousand Three Hundred Forty Five"
#     assert number_to_words(123456789) == "One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine"
#     assert number_to_words(0) == "Zero"
#     assert number_to_words(1000000) == "One Million"
#     assert number_to_words(1000000000) == "One Billion"
#     assert number_to_words(1000000000000) == "One Trillion"
#     assert number_to_words(1000000000000000) == "One Quadrillion"
#     assert number_to_words(1000000000000000000) == "One Quintillion"
#     assert number_to_words(1000000000000000000000) == "One Sextillion"
#     assert number_to_words(1000000000000000000000000) == "One Septillion"
#     assert number_to_words(1000000000000000000000000000) == "One Octillion"
#     assert number_to_words(1000000000000000000000000000000) == "One Nonillion"
#     assert number_to_words(1000000000000000000000000000000000) == "One Decillion"

# Initial test function generated by LLM
x='''def test_number_to_words(number_to_words):
    assert number_to_words(123) == "One Hundred Twenty Three"
    assert number_to_words(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert number_to_words(123456789) == "One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine"
    assert number_to_words(0) == "Zero"
    assert number_to_words(1000000) == "One Million"
    assert number_to_words(1000000000) == "One Billion"
    assert number_to_words(1000000000000) == "One Trillion"
    assert number_to_words(1000000000000000) == "One Quadrillion"
    assert number_to_words(1000000000000000000) == "One Quintillion"
    assert number_to_words(1000000000000000000000) == "One Sextillion"
    assert number_to_words(1000000000000000000000000) == "One Septillion"
    assert number_to_words(1000000000000000000000000000) == "One Octillion"
    assert number_to_words(1000000000000000000000000000000) == "One Nonillion"
    assert number_to_words(1000000000000000000000000000000000) == "One Decillion" '''

# Extract assertions from the test function
def extract_assertions(test_function):
    assertions = []
    lines = test_function.split('\n')
    for line in lines:
        if line.strip().startswith('assert'):
            assertions.append(line.strip())
    return assertions

# Genetic Algorithm
def genetic_algorithm(test_function, iterations=100):
    assertions = extract_assertions(test_function)
    num_assertions = len(assertions)
    population_size = 10

    # Initialize population
    population = []
    for _ in range(population_size):
        chromosome = [random.choice(assertions) for _ in range(num_assertions)]
        population.append(chromosome)

    # Genetic algorithm iterations
    for _ in range(iterations):
        # Evaluation
        fitness_scores = []
        for chromosome in population:
            # Evaluate fitness (coverage) of each chromosome (not implemented here)
            # For simplicity, let's assume random fitness scores
            fitness_scores.append(len(chromosome))
        
        # Selection (select top performing chromosomes)
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population), key=lambda pair: pair[0], reverse=True)]
        selected_population = sorted_population[:population_size // 2]

        # Crossover (combine features of selected chromosomes)
        offspring_population = []
        for i in range(population_size // 2):
            parent1 = random.choice(selected_population)
            parent2 = random.choice(selected_population)
            crossover_point = random.randint(1, num_assertions - 1)
            offspring = parent1[:crossover_point] + parent2[crossover_point:]
            offspring_population.append(offspring)

        # Mutation (introduce small changes)
        for chromosome in offspring_population:
            if random.random() < 0.1:  # Mutation rate
                mutation_point = random.randint(0, num_assertions - 1)
                chromosome[mutation_point] = random.choice(assertions)

        # Update population
        population = selected_population + offspring_population

    # Return best performing chromosome
    best_chromosome = max(population, key=lambda x: fitness_scores[population.index(x)])
    return best_chromosome


# executor2 = AbstractExecutor(function)

# # Execute the input function and get the coverage date
# coverage_data = executor2._execute_input(file_name_check)






# Test the genetic algorithm
# initial_coverage = evaluate_coverage(x)
# print("Initial Coverage:", initial_coverage)

function_name = "number_to_words"
# best_chromosome = genetic_algorithm(x)
# print(best_chromosome)
# 
# if not best_chromosome:
#     formatted_assertions = "assert False, 'No assertions generated'"
# else:
#     formatted_assertions = "\n    ".join(best_chromosome)

# # Create the test function with the extracted or placeholder assertions
# test_function_code = (
#     f"def test_{function_name}({function_name}):\n    {formatted_assertions}\n"
# )

# print(test_function_code)
# filename = "test_generated.py"
# with open(filename, "w") as file:
#     file.write(test_function_code)
# print(f"Test function written to {filename}")


# test_name = f"test_{function_name}"
# module_name = filename.split(".")[0]
# function_name = test_name

# # Import the module dynamically
# module = importlib.import_module(module_name)
# function = getattr(module, function_name)
# function=number_to_words

from test_generated import test_number_to_words
executor2 = AbstractExecutor(test_number_to_words)

# Execute the input function and get the coverage date
coverage_data = executor2._execute_input(number_to_words)

# Print the coverage date
print("Coverage data before:")
print(coverage_data)
print('--')


from test_generated1 import test_number_to_words

executor2 = AbstractExecutor(test_number_to_words)

# Execute the input function and get the coverage date
coverage_data = executor2._execute_input(number_to_words)

# Print the coverage date
print("Coverage data before:")
print(coverage_data)
print('--')

# test_name = f"test_{function_name}"
# module_name = filename.split(".")[0]
# function_name = test_name

# # Import the module dynamically
# module = importlib.import_module(module_name)
# function = getattr(module, function_name)


# executor2 = AbstractExecutor(function)

# # Execute the input function and get the coverage date
# coverage_data = executor2._execute_input(number_to_words)

# # Print the coverage date
# print("Coverage data after:")
# print(coverage_data)
# print('--')