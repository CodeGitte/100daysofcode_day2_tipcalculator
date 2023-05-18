# just for demonstration purposes I wanted to include this file as well, this shows my first idea of solving the problem (which did not work obviously)
# instead of looping through every single word, I wanted to define pairs of words and iterate over the given list
# however, of course it depends on which pair of words is deleted first, and wrong combinations could be removed from the modified list

# also, in the first draft I also wanted to include this: directions = [direction.upper().replace("UE", "Ü") for direction in directions]
# in case that someone entered a direction including spelling errors like norden or sueden, but then I decided to be more general and include value error handling

OPPOSITES = [["NORDEN", "SÜDEN"], ["SÜDEN", "NORDEN"], ["WESTEN", "OSTEN"], ["OSTEN", "WESTEN"]]
  
def solve(directions):
    # Capitalize the list and replace "UE" with "Ü", just in case 
    directions = [direction.upper().replace("UE", "Ü") for direction in directions]

    # Loop until there are no more pairs of opposites
    for pair in OPPOSITES:
        if pair[0] in directions and pair[1] in directions and directions.index(pair[0]) == directions.index(pair[1]) - 1:
                directions.remove(pair[0])
                directions.remove(pair[1])
                
    # Return the updated list of directions
    return directions
