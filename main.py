import launch
import data

def test():
    launch.launch_sweep(
        'test_sweep.yaml',
        entity=data.get_settings_value('public.WANDB_DEFAULT_ENTITY'),
        project='uncategorized'
    )

# TODO: Run an experiment on 2D grid using NetworkX lattice package.
# TODO: Change figure rendering so parameter values appear in the title (which makes animations clearer).
# TODO: Use Bayesian updating & conjugate priors for sweep annealing. (Beta & Dirichlet distributions.)
# TODO: Test setting random seed.
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

# TODO NEXT: Use graphviz (already installed) to give better graph visualizations.
# TODO: Edit the names of states in NetworkX graphs to give them significant labels.


'''
launch.launch_sweep(
    'sweep-COMPLETE_GRAPH_8_NODES_MDP_GAMMA_SWEEP-distribution_uniform_0t1-samples_100k.yaml',
    entity=data.get_settings_value('public.WANDB_COLLAB_ENTITY'),
    project='power-project',
    beep_when_done=True
)
'''