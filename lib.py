import numpy as np
import copy as cp
import sys

import utils

def policy_rollout(policy, reward_function, state_list, starting_state, number_of_steps):
    if len(policy) != len(reward_function):
        raise Exception('The policy must have the same number of rows as the reward_function has entries.')
    
    if len(reward_function) != len(state_list):
        raise Exception('The reward_function and state_list must have the same length.')   

    state_index = state_list.index(starting_state)

    state_history = [starting_state]
    reward_history = [reward_function[state_index]]

    for _ in range(number_of_steps):
        state_index = np.where(policy[state_index] == 1)[0][0]

        state_history += [state_list[state_index]]
        reward_history += [reward_function[state_index]]
    
    return (
        state_history, reward_history
    )

def policy_evaluation(
    policy,
    reward_function,
    discount_rate,
    value_initialization=None,
    convergence_threshold=1e-4
):

    value_function = np.zeros(len(reward_function)) if (
        value_initialization is None
    ) else cp.deepcopy(value_initialization)

    is_first_iteration = True

    while is_first_iteration or (max_value_change > convergence_threshold):

        is_first_iteration = False
        max_value_change = 0
        old_values = cp.deepcopy(value_function)

        for state in range(len(reward_function)):
            value_function[state] = reward_function[state] + np.dot(
                policy[state], discount_rate * value_function
            )
            
        max_value_change = utils.calculate_value_convergence(old_values, value_function)

    return value_function

def get_greedy_policy(value_function, adjacency_matrix):
    policy_actions = np.argmax(utils.mask_adjacency_matrix(adjacency_matrix) * value_function, axis=1)
    policy = np.zeros((len(value_function), len(value_function)))
    policy[np.arange(len(policy)), policy_actions] = 1

    return policy

def policy_iteration(
    reward_function,
    discount_rate,
    adjacency_matrix,
    policy_initialization=None,
    value_initialization=None,
    convergence_threshold=1e-4,
    seed=None,
    tiny_number=utils.TINY_NUMBER
):

    utils.check_adjacency_matrix(adjacency_matrix)
    policy = utils.generate_random_policy(len(reward_function), seed=seed) if (
        policy_initialization is None
    ) else utils.check_policy(policy_initialization)
    value_function = np.zeros(len(reward_function)) if (
        value_initialization is None
    ) else utils.check_value_reward(value_initialization)

    is_first_iteration = True

    while is_first_iteration or (
        max_value_change > convergence_threshold and not (policy == old_policy).all()
    ):

        is_first_iteration = False
        old_policy = cp.deepcopy(policy)
        old_values = cp.deepcopy(value_function)

        value_function = policy_evaluation(
            policy,
            reward_function,
            discount_rate,
            value_initialization=value_function,
            convergence_threshold=convergence_threshold,
            tiny_number=tiny_number
        )
        policy = get_greedy_policy(value_function, adjacency_matrix)

        max_value_change = utils.calculate_value_convergence(old_values, value_function)
    
    return (
        policy,
        value_function
    )

def value_iteration(
    reward_function,
    discount_rate,
    adjacency_matrix,
    value_initialization=None,
    convergence_threshold=1e-4
):

    utils.check_adjacency_matrix(adjacency_matrix)
    value_function = np.zeros(len(reward_function)) if (
        value_initialization is None
    ) else utils.check_value_reward(value_initialization)

    is_first_iteration = True

    while is_first_iteration or (max_value_change > convergence_threshold):

        is_first_iteration = False
        max_value_change = 0
        old_values = cp.deepcopy(value_function)
        
        for state in range(len(reward_function)):
            value_function[state] = reward_function[state] + discount_rate * np.max(
                utils.mask_adjacency_matrix(adjacency_matrix[state]) * value_function
            )

        max_value_change = utils.calculate_value_convergence(old_values, value_function)
    
    return (
        get_greedy_policy(value_function, adjacency_matrix),
        value_function
    )

def calculate_power(
    adjacency_matrix,
    discount_rate,
    num_reward_samples=1000,
    reward_range=(0, 1),
    convergence_threshold=1e-4,
    random_seed=None
):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    all_optimal_values = []
    all_reward_functions = []

    for i in range(num_reward_samples):
        sys.stdout.write('Running samples {0} / {1}'.format(i + 1, num_reward_samples))
        sys.stdout.flush()
        sys.stdout.write('\r')
        sys.stdout.flush()

        all_reward_functions += [utils.generate_random_reward(len(adjacency_matrix), interval=reward_range)]
        all_optimal_values += [
            value_iteration(
                all_reward_functions[-1],
                discount_rate,
                adjacency_matrix,
                convergence_threshold=convergence_threshold
            )[1]
        ]
    
    print() # Jump to newline after stdout.flush()

    power_distribution = ((1 - discount_rate) / discount_rate) * (
        np.stack(all_optimal_values) - np.stack(all_reward_functions)
    )
    power = np.mean(power_distribution, axis=0)

    return (
        power,
        power_distribution
    )
