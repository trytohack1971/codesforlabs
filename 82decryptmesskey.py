def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_primitive_root(g, p):
    if not is_prime(p):
        return False
    roots = {pow(g, i, p) for i in range(1, p)}
    return len(roots) == p - 1

def generate_keys(p, g, x1, x2):
    if x1 >= p or x2 >= p:
        return None
    y1 = pow(g, x1, p)
    y2 = pow(g, x2, p)
    k1 = pow(y2, x1, p)
    k2 = pow(y1, x2, p)
    return k1, k2

def main():
    p = int(input("Enter a prime number (P): "))
    g = int(input(f"Enter a primitive root modulo {p} (G): "))
    x1 = int(input("Enter the private key of User 1: "))
    x2 = int(input("Enter the private key of User 2: "))
    
    if not is_primitive_root(g, p):
        print(f"{g} is not a primitive root modulo {p}. Please try again.")
        return
    
    keys = generate_keys(p, g, x1, x2)
    if keys:
        k1, k2 = keys
        print(f"Secret Key for User 1: {k1}")
        print(f"Secret Key for User 2: {k2}")
        if k1 == k2:
            print("Keys have been exchanged successfully.")
        else:
            print("Keys have not been exchanged successfully.")
    else:
        print(f"Private keys must be less than {p}. Please try again.")

if __name__ == "__main__":
    main()

