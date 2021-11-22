import launch
import data
import check

# Ensure all our adjacency matrices pass sanity checks on startup.
# TODO: Save these in dill by default and sanitize on saving rather than on loading.

if __name__ == '__main__':
    for _, adjacency_matrix in data.ADJACENCY_MATRIX_DICT.items():
         check.check_adjacency_matrix(adjacency_matrix)

# TODO: Build state_list into the program itself since we shouldn't assume a list format.
# TODO: Test setting random seed.
# TODO NEXT: Create src directory and update filepaths.
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


# TODO NEXT: Create directory for sweep yaml files and update filepaths.
# TODO NEXT: Document API for the sweep function.
# TODO NEXT: Use networkx to construct graph rather than manually writing the adjacency matrix.
# Refactor this when we start investigating new topologies.

launch.launch_sweep(
    'test_sweep_prod.yaml',
    entity=data.get_settings_value('public.WANDB_COLLAB_ENTITY'),
    project='power-project'
)
