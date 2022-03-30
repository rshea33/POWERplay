from src import test
from src import launch
from src import data

# TODO: Document stochastic wind API and multiagent API and graph formats.
# TODO: More stochastic experiments.
# - Wind, teleporters, irreversible actions / doorways.
# TODO: Refactor codebase to keep all files under 200 lines each.
# TODO: Add policy construction and checking methods onto an existing gridworld. Test & document.
# TODO: Add visualization for gridworld and Agent 2 policy.
# TODO: Add method to save (gridworld, policy, MDP) triple.
# TODO: Do profiling and see which parts are the slowest.
# TODO: Experiment with multiple fixed policies in the 3-cell 2-agent gridworld.
# TODO: (?) Create a state container for training loop with stateless functions underneath.
# TODO: Save with wandb instead of homespun data methods.
# TODO: Investigate writing type hints.
# TODO: Add argparse.ArgumentParser().
# parser = argparse.ArgumentParser()
# parser.add_argument('-b', '--batch-size', type=int, default=8, metavar='N',
#                      help='input batch size for training (default: 8)')
# args = parser.parse_args()
# TODO: Refactor experiment wrapper with https://hydra.cc/ when I understand what experiment configs
# I commonly use.
# TODO: Add ability to run sweep without wandb server access (i.e., offline mode). May be impossible, but
# would be great as it would allow me to run local tests without consuming bandwidth, etc.
# TODO: Add sparse / non-sparse flag to toggle value iteration calculation.
# - "Using a sparse storage format for storing sparse arrays can be advantageous only when the
#   size and sparsity levels of arrays are high. Otherwise, for small-sized or low-sparsity arrays
#   using the contiguous memory storage format is likely the most efficient approach."
#   Source: https://pytorch.org/docs/stable/sparse.html

# TODO NEXT: Do a deep investigation of the multiagent case.
# - We're seeing an error (bug or possible conceptual confusion) in the 1x3 gridworld multiagent case.
# - We can try debugging by making the Agent B policy asymmetrical. (Maybe make it non-stochastic.)
# Improve visualization of the MDP graph for the integrated transition tensor.
# Add sanity checks to policy / MDP inputs for the multiagent case.
# Create gridworld visualizations for the multiagent case.
# TODO NEXT: Convert the reduced agent A tensor to a standard stochastic MDP graph for visualization / debugging.
# - Make sure this is what gets visualized in the experiment pipeline.
# TODO NEXT: Create a test function to run multiagent in a 1x3 gridworld.
# TODO NEXT: Check compatibility of policy and tensor (for multiagent) up front in launch.py param checker.
# TODO NEXT: Document (and refactor?) all relevant policy, multi, and mdp functions.
# TODO NEXT: Test simple 3-cell gridworld with 2 agents and a fixed policy.

if __name__ == '__main__':
    # test.test_vanilla()
    # test.test_gridworld()
    # test.test_stochastic()
    
    pass