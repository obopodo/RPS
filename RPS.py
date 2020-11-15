from actors.Markov1 import Markov1

score = 0 # PC`s score
reaction = 0 # initial reaction - just the rock
history = []

def your_action():
    '''
    Takes action from stdin
    checks if action is 0, 1 or 2
    '''
    action = int(input(f'Your move {i}:  '))
    if action in [0, 1, 2]:
        appropriate = True
    else:
        print('Action should be 0 (rock), 1 (paper) or 2 (scissors)')
        print('Please, enter your action again')

    return action

def update_score(action, reaction):
    global score

    if (action, reaction) in [(0,1), (1,2), (2,0)]:
        score += 1
    elif action == reaction:
        pass
    else:
        score -= 1
    print(f'Your score {-1*score}')

# let's start the game!
for i in range(5):
    action = your_action()
    history.append(action)
    print(f'PC`s move {i}: ', reaction)

    # update the score:
    update_score(action, reaction)

    markov_actor = Markov1()
    reaction = markov_actor.react(action)

    # transition matrix can be updated only if we have at least 2 opponent's actions:
    if i > 1:
        markov_actor.update_tr_mat(history)

# print the score:
if score > 0:
    print(f'PC score with score {score}')
elif score == 0:
    print('Tie!')
else:
    print(f'You win with score {abs(score)}!')

# take a look at transition matrix
print(markov_actor.transition_mat)
print(markov_actor.P_mat)
