def main():
    print("==============================")
    print("       JARVIS AUTO CORE")
    print("==============================")

    name = input("Please enter your name: ")
    print(f"Hello, {name}! I am JARVIS.")
    print("I am here to help with car troubles.")
    print()

    problem = input("What car problem can I help with? ")
    check_problem(problem)

    print()
    print("JARVIS is analysing your request...")
    print(f"Your question: {problem}")
    print("==============================")
def check_problem(problem):
    if problem.strip()=="":
        problem=(" Please enter the issues you are facing with your car: ")
        check_enginecheck=input(" Do you see any warning lights in your car(Yes/No):  ")
        if check_enginecheck.upper()="Yes":
            print(" Ok affirmative fetching possible issues to find solution ")
            check_enginefix()
def check_enginefix():
    
        
        
if __name__ == "__main__":
    main()
    


