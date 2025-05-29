def square_number(num):

    if not isinstance(num, (int, float)):
        raise ValueError("Input must be an integer or float.")

    return num **2
