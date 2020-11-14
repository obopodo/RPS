import numpy as np
from  scipy import stats

rock, paper, scissors = 0, 1, 2

X = np.array([0, 1, 2]) # actions

# not normalized transition matrix initialization:
transition_mat = np.ones((3,3))

def get_P(transition_mat):
    # transition matrix normalization
    row_sums = transition_mat.sum(axis=1)
    P = transition_mat / row_sums.reshape(-1,1)
    return P

# def react(action, p_trans):

def markov_actor(action):
    '''
    1st order Markov chain.
    Predicts opponent's next moves probabilities and generates opposite reaction
    with estimated descrete probabilities distribution.
    '''
    global transition_mat
    P = get_P(transition_mat)
    my_probs = P[action]
    my_probs = my_probs[2], my_probs[0], my_probs[1] # opposite actions
    rps_dist = stats.rv_discrete(name='rps_dist', values=(X, my_probs))
    reaction = rps_dist.rvs(size=1)[0]
    return reaction

def update_tr_mat(prev_action, action):
    # transition matrix updation
    global transition_mat
    transition_mat[prev_action][action] += 1

# let's start the game!
score = 0 # PC`s score
reaction = 0 # initial reaction - just the rock
for i in range(10):

    # check if action is 0, 1 or 2
    appropriate = False
    while not appropriate:
        action = int(input(f'Your move {i}:  '))
        if action in [0, 1, 2]:
            appropriate = True
        else:
            print('Action should be 0 (rock), 1 (paper) or 2 (scissors)')
            print('Please, enter your action again')

    print(f'PC`s move {i}: ', reaction)

    # update the score:
    if (action, reaction) in [(0,1), (1,2), (2,0)]:
        score += 1
    elif action == reaction:
        pass
    else:
        score -= 1
    print(f'Your score {-1*score}')

    reaction = markov_actor(action)

    # transition matrix can be updated only if we have at least 2 opponent's actions:
    if i > 1:
        update_tr_mat(prev_action, action)

    prev_action = action # remember the action

# print the score:
if score > 0:
    print(f'PC score with score {score}')
elif score == 0:
    print('Tie!')
else:
    print(f'You win with score {abs(score)}!')

# take a look at transition matrix
print(get_P(transition_mat))
