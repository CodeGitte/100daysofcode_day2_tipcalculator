# Define opposite directions as a dictionary 
OPPOSITES = {"NORDEN":"SÜDEN", "SÜDEN":"NORDEN", "WESTEN":"OSTEN" , "OSTEN":"WESTEN"}

def solve(directions):
    """
    Given a list of directions, remove any pairs of opposite directions
    that are adjacent to each other, and return the resulting list.

    Args:
    directions (list): A list of strings representing the directions,
    which can be 'NORDEN', 'SÜDEN', 'WESTEN', or 'OSTEN'.

    Returns:
    list: A new list of strings representing the directions with any
    opposite directions removed.
    """
    # Value error handling for invalid input directions
    valid_directions = {'NORDEN', 'SÜDEN', 'WESTEN', 'OSTEN'}
    if not all(direction in valid_directions for direction in directions):
        raise ValueError("In der Liste wurde ein ungültiger Wert entdeckt. Bitte folgende Richtungen nur so angeben: NORDEN, SÜDEN, WESTEN, OSTEN")

    # Create an empty list for the filtered directions
    filtered_directions = []

    # Loop through the input list directions in order to detect opposite directions (e.g. NORDEN and SÜDEN)
    for direction in directions:
        # Iterate over each direction in the input list and check if it is opposite to the last added direction in the filtered list filtered_directions
        if filtered_directions and OPPOSITES[direction] == filtered_directions[-1]:
            # If direction is opposite, the last direction is removed from the list filtered_directions and the new direction is not appended to the list filtered_directions
            filtered_directions.pop(-1)
        # If not opposite, the new direction is appended to the list filtered_directions
        else:
            filtered_directions.append(direction)

    return filtered_directions

