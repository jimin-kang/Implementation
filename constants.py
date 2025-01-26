
# prime number to define the finite field where coefficients will be sampled from
# in practice, FIELD_SIZE > max(n, k)  
FIELD_SIZE = 65521

PROMPT_SCHEME_PARAMTERS = "Enter the threshold (t), number of participating parties (n), and the secret (k) for the (t, n) secret sharing scheme in the following format: t n k\n"

PROMPT_POOLED_PARTIES = '''
Enter the indices of the parties whose shares you wish to pool. 
For example, to pool shares from parties i, j, k, enter 'i j k'. 
To select a random subset of {t} parties, enter 'r'. 
Keep in mind, to reconstruct the secret, you will need to pool shares from {t} parties.
'''

REPROMPT_PARTIES = '''
You requested to pool shares from less than {t} parties. 
Reconstructing the secret requires pooling shares from {t} parties. 
Do you wish to proceed? Enter 'Y' to proceed, and any other key to be reprompted.
'''