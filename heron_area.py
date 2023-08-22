def heron_area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.
    
    Parameters:
    a (float): Length of the first side of the triangle.
    b (float): Length of the second side of the triangle.
    c (float): Length of the third side of the triangle.
    
    Returns:
    float: Area of the triangle.
    """
    # Check if the given side lengths form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter of the triangle
        s = (a + b + c) / 2
        
        # Calculate the area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        raise ValueError("Invalid side lengths. They do not form a valid triangle.")