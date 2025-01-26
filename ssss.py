import random # in practice, this should be cryptographically secure
import numpy as np
from numpy.polynomial import polynomial as P
from constants import FIELD_SIZE

def generate_polynomial(d, k):
    """
    Parameters:
        d: degree of polynomial to be generated
        k: secret to define polynomial y-intercept
    Returns:
        poly: vector of polynomial coefficients & intercept
               ordered from intercept term to largest degree term i.e. [k, a_{1}, a_{2},..., a_{t-1}]
    """
    # generate random coeffcients from {0,...,p-1}
    poly = [random.randint(0, FIELD_SIZE-1) for _ in range(d)]

    # coefficient of largest degree term must be non-zero
    poly[-1] = random.randint(1, FIELD_SIZE-1)

    # place secret at y-intercept i.e. p(0) = k
    poly.insert(0, k)

    return poly

def compute_shares(poly, n):
    """
    Parameters:
        coeff: polynomial coefficients ordered from intercept term to largest degree term i.e. [k, a_{1}, a_{2},..., a_{t-1}]
        n: number of parties to distribute secret shares to
    Returns:
        shares: vector of computed shares
                ordered by ascending order of party index i.e. [s_{1}, s_{2},..., s_{n}]
    """
    # evaluate polynomial at x in {1, 2,..., n}
    x = np.arange(1, n + 1, 1)

    # Generate the Vandermonde matrix
    vandermonde = P.polyvander(x=x, deg=len(poly)-1)

    # shares = vandermonde * poly
    shares = vandermonde @ poly
    
    return shares

def reconstruct_secret(shares, indices):
    """
    Parameters:
        shares: pooled share values 
        indices: parties corresponding to pooled share values
    Returns:
        secret & vector containing polynomial coefficients and secret
    """
    # Vandermonde matrix for pooled parties
    vandermonde = P.polyvander(x=indices, deg=len(indices)-1)

    # coeff = inv(Vandermonde) * shares
    poly = np.linalg.inv(vandermonde) @ np.array(shares)

    # rounding to deal w/ floating pt. precision errors: wrapping integer lists into numpy arrays may promote integers into floats
    # polynomial coefficients are integers in {0,...,p-1}
    poly = [float(poly[0])] + [round(x) for x in poly[1:]]
    
    print(f"Reconstructed Secret: {poly[0]}")
    print(f"Reconstructed Polynomial: {poly}")

def display_scheme_info(k, poly, shares):
    """
    Display secret (k), polynomial, and shares for the participating parties in the (t, n) secret sharing scheme.
    """
    print(f"Secret: {k}")
    print(f"Polynomial: {poly}")
    print("Shares:")
    for i, share in enumerate(shares):
        print(f"  Party {i+1}: {share}")