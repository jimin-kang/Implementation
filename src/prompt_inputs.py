import random
from constants import FIELD_SIZE, PROMPT_SCHEME_PARAMTERS, PROMPT_POOLED_PARTIES, REPROMPT_PARTIES

def accept_scheme_parameters():
    """
    Description:
        Prompt user for the following relevant parameters for the (t, n) secret sharing scheme:
            Threshold (t)
            Party count (n)
            Secret (k)
        Parameters t, n, k must satisfy the following constraints:
            n >= 1
            1 <= t <= n
            secret, n < FIELD_SIZE
    
    Returns:
        t, n, k
    """
    while True:
        args = input(PROMPT_SCHEME_PARAMTERS)
        try:
            args_list = args.split()
            t = int(args_list[0])
            n = int(args_list[1])
            k = float(args_list[2])

            if t <= 0 or n <= 0:
                print("Threshold (t) & party count (n) must be greater than 0.")
            elif t > n:
                print("Threshold (t) cannot be greater than party count (n) in a (t, n) secret sharing scheme.")
            elif t > FIELD_SIZE or n > FIELD_SIZE or k > FIELD_SIZE:
                print(f"Threshold (t), party count (n), and secret (k) must all be less than {FIELD_SIZE}.")
            else:
                return t, n, k            
        except ValueError:
            print("Threshold (t) & party count (n) must be integers. Secret (k) must be a float.")

def prompt_pooled_parties(t, n):
    """
    Description:
        Prompts user for parties whose shares should be pooled to reconstruct secret.
        Users may specify party indices as space delimited integers (ex: '1 2 3') or enter 'r' to select random subset of t parties.
        User will be warned if they specify fewer number of parties required to reconstruct the secret.
    
    Parameters:
        t: threshold in (t, n) secret sharing scheme
        n: number of participating parties in (t, n) secret sharing scheme
    
    Returns:
        party_indices: list of parties to pool shares from
    """
    while True:
        args = input(PROMPT_POOLED_PARTIES.format(t=t))
        try:
            if args == 'r':
                return random.sample(range(1, n+1), t)
            
            party_indices = list(set([int(x) for x in args.split()]))
            
            if min(party_indices) <= 0 or max(party_indices) > n:
                print(f"Party indices must be integers between 1 and {n}.") 
            else:
                # if selected_parties < t, reprompt OR show failure to reconstruct
                if len(party_indices) < t:
                    proceed = input(REPROMPT_PARTIES.format(t=t))
                    if proceed == "Y":
                        return party_indices
                else:
                    # if selected_parties > t, select t of them
                    if len(party_indices) > t:
                        print(f"You requested to pool shares from more than {t} parties. Only shares from the first {t} parties will be pooled.")
                        return party_indices[:t]
                    
                    return party_indices
        except ValueError:
            print(f"Please specify party indices as integers between 1 and {n}. Or, enter 'r' to select a random subset of {t} parties.")