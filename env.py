import numpy as np
import torch as T

class SimpleBandit:
    # p is tensor[p]
    def __init__(self, p):
        if len(p) == 1:
            self.p_left = p
            self.p_right = 1 - p
        else:
            self.p_left = p[:1]
            self.p_right = p[1:]
    
    # act: 0 for left 1 for right
    def action(self, act):
        if act == 0:
            return T.bernoulli(self.p_left)
        else:
            return T.bernoulli(self.p_right)

def generate_bandit(independent=False):
    return SimpleBandit(T.rand(2)) if independent else SimpleBandit(T.rand(1)) 


    


