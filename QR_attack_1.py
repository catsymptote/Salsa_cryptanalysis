from science.cryptography_tools import *
from science.hamming_weight import *
from science.format_tools import *
from science.plot_tools import *
from science.Pearson_correlation import *


def brute_force_QR(Y:tuple):
    crypt = Crypto_Tools()
    size = len(Y[0])
    X = ('0'*size, '0'*size, '0'*size, '0'*size)

    
    while crypt.use_QRF(X) != Y:
        # Count X up one.
        X = increment_QR_X(X)
    
    return X


def get_random_QRF_output(size=128):
    crypt = Crypto_Tools()
    X = generate_random_QR_X(size)
    Y = crypt.use_QRF(X)
    Y_str = list_to_str(Y)
    return X, Y, Y_str


def attack():
    # Setup.
    max_attempts = 50 #32**2
    size = 8
    state_space = size * 4
    crypt = Crypto_Tools()

    # Real value (X) and initial guess (X_guess).
    X, Y, Y_str = get_random_QRF_output(size=size)
    X_str = list_to_str(X)

    X_guess = generate_random_QR_X(bits=size)
    #X_guess = X#[0:30] + list_to_str(X_guess)[30:])
    print(X_guess)
    Y_init = list_to_str(crypt.use_QRF(X_guess))
    HD_init = hamming_distance(Y_init, Y_str)

    HDs = []
    HD_Xs = []
    retake_list = []
    guesses = []

    print('X:\t', X)
    run = 0
    retakes = 0
    finished = False
    while not finished and run < max_attempts:
        run += 1
        unchanged = True

        for j in range(state_space):
            # Get new X and Y.
            X_new = flip_bit_at(X_guess, j)
            Y_new = list_to_str(crypt.use_QRF(X_new))

            # Calc Hamming Distance of new Y vs old Y.
            HD_new = hamming_distance(Y_new, Y_str)

            # If new guess is correct.
            if Y_new == Y_str:
                print('Finished!')
                finished = True
                continue
            
            # If new guess is better than old.
            elif HD_new < HD_init:
                # Set new guess to current guess.
                X_guess = X_new
                Y_init  = Y_new
                HD_init = HD_new
                #print('X_guess:\t', X_guess)
                HDs.append(HD_new)
                HD_X = hamming_distance(X_str, list_to_str(X_new))
                HD_Xs.append(HD_X)
                guesses.append([HD_new, HD_X, Y_new, list_to_str(X_new)])

                unchanged = False
                continue
        
        if unchanged:
            # Found local optima. Restart.
            X_guess = generate_random_QR_X(bits=size)
            Y_init = list_to_str(crypt.use_QRF(X_guess))
            HD_init = hamming_distance(Y_init, Y_str)
            retakes += 1
            #finished = True
            
            retake_list.append(len(HDs) - 1)
        


    
    print('Good guesses:\t', len(guesses))
    
    guesses.sort(reverse=True)
    guesses.append(['0', '0', Y_str, X_str])
    guesses.append(['HD_new', 'HD_x', 'Y_new\t\t\t\t', 'X_new'])
    print_list_of_lists(guesses)
    expected_avg_HD = size*4/2
    print('Expected HD:\t', expected_avg_HD)

    print('Retakes:\t', retakes)
    print('Runs:\t', run)
    print('\n')
    print('X:\t', X)
    print('X_g:\t', X_guess)
    print('\n')

    print('Pearson:\t', Pearson_correlation_coefficient(HDs, HD_Xs))

    lines = [HDs, HD_Xs, [expected_avg_HD]*len(HDs)]

    if len(retake_list) > 50:
        multi_line_chart(lines)
    else:
        multi_line_chart(lines, vertical_lines=retake_list)

    if X == X_guess:
        print('Success! :D')
    else:
        print('Oh well.. :(')
    

if __name__ == '__main__':
    attack()
