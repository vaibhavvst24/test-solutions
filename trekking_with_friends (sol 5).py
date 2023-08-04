def total_length_of_trek(A, B, C):
    # distance traveled by each person
    distance_suman = B + C
    distance_amit = A + C
    distance_ravi = A + B

    # slowest and fastest person's distance
    slowest_distance = min(distance_suman, distance_amit, distance_ravi)
    fastest_distance = max(distance_suman, distance_amit, distance_ravi)

    # total length of the trek
    total_length = slowest_distance + (fastest_distance - slowest_distance)

    return total_length

if __name__ == "__main__":
    try:
        A = int(input("Enter the distance Amit beats Suman (in meters),'A': "))
        B = int(input("Enter the distance Amit beats Ravi (in meters),'B': "))
        C = int(input("Enter the distance Suman beats Ravi (in meters),'C': "))

        total_length = total_length_of_trek(A, B, C)
        print("Total length of the Track =", total_length, "m")

    except ValueError as e:
        print("Error:", e)
