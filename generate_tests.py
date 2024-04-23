import google.generativeai as genai
from common.llm_test_generator import LLMTestGenerator
from common.prompt_generator import PromptGenerator
from common.abstract_executor import AbstractExecutor
from file_name_check import file_name_check
from to_test.number_to_words import number_to_words
from to_test.strong_password_checker import strong_password_checker
# from to_test.basic_calculator import calculate
import importlib
from genetic_algorithm1 import genetic_algorithm
from genetic_algorithm2 import genetic_algorithm as genetic_algorithm2
from genetic_algorithm1 import extract_assertions
from to_test.strong_password_checker import strong_password_checker 

key = input("Enter your API key: ")
print('\n-\n-\n-\n-\n-\n')
def generate_inital_tests_with_llm(model, function_to_test):
    # Create an LLMTestGenerator object with the generative model and the function to test
    llm_generator = LLMTestGenerator(model, function=function_to_test)

    # Create a PromptGenerator object with the function to test
    prompt_generator = PromptGenerator(function_to_test)

    # Generate a prompt for the function
    prompt = prompt_generator.generate_prompt()

    # Print the prompt
    #print(prompt)

    # Create a test function using the LLMTestGenerator
    test, test_name = llm_generator.create_test_function(prompt)

    print("Tests produced by LLM:")

    print('\n'.join(test.split('\n')[:-4]))

    # Define the filename for the generated test file
    filename = "test_generated.py"

    # Write the test function to the file
    # llm_generator.write_test_to_file(test, filename=filename)
    llm_generator.write_test_to_file('\n'.join(test.split('\n')[:-2]), filename=filename)

    # Get the module name and function name from the filename
    module_name = filename.split(".")[0]
    function_name = test_name

    # Import the module dynamically
    module = importlib.import_module(module_name)

    # Get the function from the module
    function = getattr(module, function_name)

    executor = AbstractExecutor(function)

    # Execute the input function and get the coverage date
    coverage_data = executor._execute_input(input=function_to_test)


    # Print the coverage date
    return function, coverage_data, test
import random 



if __name__ == "__main__":
    # Configure the generative AI with the API key
    genai.configure(api_key=key)

    # Create a generative model
    model = genai.GenerativeModel('gemini-pro')

    # function_to_test = number_to_words #file_name_check
    function_to_test = strong_password_checker

    ######Generate intial tests with LLM

    test, coverage_data,test_text = generate_inital_tests_with_llm(model, function_to_test)

    initial_coverage = coverage_data

    # define the executor to be used with your test generator
    executor = AbstractExecutor(function_to_test)

    try:

        """
        TODO:
        -Insert your code here to improve the initial line and branch coverage
        -Use the "test" returned from the generate_inital_tests_with_llm function to start your generation
        -You can leverage the information about the datatype from the inputs in "test" generated by the LLM
        -You must use the "executor" to evaluate your tests and guide the generation process
        -Your test generator shoud return a list with new inputs to be evaluated
        -You goal is to keep the number of inputs as small as possible and the coverage as high as possible
        """
        
        test2, coverage_data2,test_text2 = generate_inital_tests_with_llm(model, function_to_test)

        if function_to_test.__name__ == 'number_to_words':
            best_chromosome=genetic_algorithm(test_text+test_text2)
        elif function_to_test.__name__ == 'strong_password_checker':
            best_chromosome=genetic_algorithm2(test_text+test_text2)
        if not best_chromosome:
            formatted_assertions = "assert False, 'No assertions generated'"
        else:
            formatted_assertions = "\n    ".join(best_chromosome)

        function_name = function_to_test.__name__ 
        
        test_function_code = (
            f"def test_{function_name}({function_name}):\n    {formatted_assertions}\n"
        )
        
        # print("\033[91m "+test_function_code+ "\033[0m")

        filename = "test_generated1.py"
        with open(filename, "w") as file:
            file.write(test_function_code)
        print(f"Test function written to {filename}")


        test_name = f"test_{function_name}"
        module_name = filename.split(".")[0][:-1]
        function_name = test_name

        # Import the module dynamically
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)

        new_inputs_list = [function]

        executor2 = AbstractExecutor(function)

        # Execute the input function and get the coverage date
        if function_to_test.__name__ == 'number_to_words':
            coverage_data = executor2._execute_input(number_to_words)
        elif function_to_test.__name__ == 'strong_password_checker':
            coverage_data = executor2._execute_input(strong_password_checker)
        
        # print(coverage_data)
        '''
        
        # 
        # make multiple tests at first , then use genetic algorithm (search-based) to get better tests then print the best test
        '''



        
    except Exception as e:
        print(f"Exception occured: {e}")


    coverage__data = executor._execute_input(input_list=new_inputs_list)

    print("\033[93m"+f"Initial coverage: {coverage_data['coverage']}"+"\033[0m")
    print("\033[92m"+f"Final coverage: {initial_coverage['coverage']}"+"\033[0m")
    

    line_coverage_improment = coverage_data["coverage"]["percent_covered"] - initial_coverage["coverage"]["percent_covered"]
    branch_coverage_improment = coverage_data["coverage"]["covered_branches"]/coverage_data["coverage"]["num_branches"] - initial_coverage["coverage"]["covered_branches"]/initial_coverage["coverage"]["num_branches"]
    total_tests = len(new_inputs_list)
    final_score = (line_coverage_improment + branch_coverage_improment) / -total_tests
    print(f"Final score: {final_score}")





    




    