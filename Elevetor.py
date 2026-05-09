import time

def elevator():
    
    print("---------- Welcome to Gemini Lift ---------------")
    max_floor = 10
    min_floor = 0
    current_floor = 0
    
    while True:
        print(f"You are currently on {current_floor} floor.")
        print(f"The building has floors from {min_floor} to {max_floor}.")
        
        destination = input("Which floor you want to go to? - ")
        
        if destination.lower() == 'exit':
            print("Bye bye. Have a great time!")
            break
        
        if not destination.isdigit():
            print("Please input a number")
            continue
        
        destination = int(destination)
        
        if destination > max_floor or destination < min_floor:
            print(f"This building has only floors from {min_floor} to {max_floor}.")
            continue
        
        while True:
            if current_floor == destination:
                print(f"Ding! You have arrived on {destination} floor.")
                break
            
            print(f"Floor: {current_floor}")
            if current_floor < destination:
                current_floor += 1
            else:
                current_floor -= 1
            
            time.sleep(1)
            

elevator()