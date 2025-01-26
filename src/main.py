from prompt_inputs import accept_scheme_parameters, prompt_pooled_parties
from ssss import generate_polynomial, compute_shares, reconstruct_secret, display_scheme_info

def main():
    # define scheme & compute/distribute shares
    t, n, k = accept_scheme_parameters()
    poly = generate_polynomial(t-1, k)
    shares = compute_shares(poly, n)
    
    display_scheme_info(k, poly, shares)

    # prompt for shares to pool
    pooled_parties = prompt_pooled_parties(t, n)
    pooled_shares = [shares[i-1] for i in pooled_parties]
    
    # reconstruct secret from pooled shares
    reconstruct_secret(pooled_shares, pooled_parties)    

if __name__ == "__main__":
    main()