directions = {"N":1, "E": 2, "S": 3, "W": 4}                   
directions_list=['N','E','S','W']
def turn_left(x: int, y: int, direction: int) -> tuple:
    """
    Turns the Rover to the left
    Parameters:
    - x: The X axis 
    - y: The Y axis
    - direction: A number representing a direction from the directions dictionary above

    Returns:
    - A tuple with the actual values of the axis X and Y and the direction of the rover 
    """

    drc = direction - 1
    if drc < directions["N"]:
        drc = directions["W"]    

    return x, y, drc

def turn_right(x: int, y:int, direction: int) -> tuple:
    """
    Turns the Rover to the right 
    Parameters:
    - x: The X axis 
    - y: The Y axis
    - direction: A number representing a direction from the directions dictionary above

    Returns:
    - A tuple with the actual values of the axis X and Y and the direction of the rover 
    """
    
    drc = direction + 1
    if drc > directions["W"]:
        drc = directions["N"]  

    return x, y, drc
 
def move(x: int, y: int, direction: int) -> tuple:
    """
    Moves the rover according to the coordenates:

    Parameters:
    - x: The X axis 
    - y: The Y axis
    - direction: A number representing a direction from the directions dictionary above

    Returns:
    - A tuple with the actual values of the axis X and Y and the direction of the rover 
    """
    m = {   
            1: lambda x,y,d: (x, y+1, d), 
            2: lambda x,y,d: (x+1, y, d),
            3: lambda x,y,d: (x, y-1, d),
            4: lambda x,y,d: (x-1, y, d)
        }

    return m[direction](x, y, direction)

def define_plateau(user_input: str) -> list:
    """
    Set the coordinates of the plateau

    Parameters:
    - user_input: The command center input of the plateau upper-right

    Returns:
    - A list with the upper right values of the plateau
    """

    plateau_coords = list(user_input)        
    if len(plateau_coords) != 2:
        raise Exception("plateau must have 2 values")
    
    return list(map(int, plateau_coords))

movements = {"R": turn_right, "L": turn_left, "M": move}

def exec(landing: str, instructions: "str"):
    """
    Executes the Rover commands based on the landing parameters and instructions
    
    Parameters:
    - landing: The Rover landing parameters
    """
    parameters = list(landing)
    x, y = (int(parameters[0]), int(parameters[1]))
    where_to = parameters[2].upper()
    direction = directions[where_to]
    instructions = list(instructions)
    for i in instructions: 
        x, y, direction = movements[i](x, y, direction)
    
    return x, y, directions_list[direction-1]

def main():
    """
    Starts the Rover app
    """
    try:
        upper_right = define_plateau(user_input = input("Plateau size: "))
        while True:
            parameters = input("Landing: ") 
            instructions = input("Instructions: ") 
            x, y, _ = exec(parameters, instructions)
            print("{0} {1} {2}".format(x, y, _))
    except Exception as ex:
        print(ex)
    

if __name__ == '__main__':
    main()