import numpy as np
from scipy.stats import rv_discrete

class Markov1:
    '''
    1st order Markov chain.
    Predicts opponent's next moves probabilities and generates opposite reaction
    with estimated descrete probabilities distribution.
    '''
    def get_P_mat(self):
        '''
        transition matrix normalization
        It's a helping function and is used within this class
        '''
        row_sums = self.transition_mat.sum(axis=1)
        P_mat = self.transition_mat / row_sums.reshape(-1,1)
        return P_mat

    def __init__(self):
        self.transition_mat = np.ones((3, 3))
        self.actions = [0, 1, 2]
        self.P_mat = self.get_P_mat()
        self.my_history = [] # maybe should be storred in global env

    def update_tr_mat(self, history):
        self.transition_mat[history[-2], history[-1]] += 1
        self.P_mat = self.get_P_mat()

    def react(self, action):
        my_probs = self.P_mat[action]
        my_probs = my_probs[2], my_probs[0], my_probs[1] # opposite actions
        rps_dist = rv_discrete(name='rps_dist', values=(self.actions, my_probs))
        reaction = rps_dist.rvs(size=1)[0]
        self.my_history.append(reaction) # see above
        return reaction
