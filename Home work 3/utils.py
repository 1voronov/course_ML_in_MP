import pandas as pd
import matplotlib.pyplot as plt

def get_train_RMSE_and_MaxAE(paths, path_prefix):
    RMSE_dict = {}
    MaxAE_dict = {}

    for path_ in paths:
        fin = open(path_prefix+path_+'SISSO.out', 'r')
        fin_lines = fin.readlines()
        errors_line_idxs = []
        for line_idx, line in enumerate(fin_lines):
            if line.startswith('Total LS_RMSE,LS_MaxAE:'):
                errors_line_idxs.append(line_idx)
        path_RMSE_ = []
        path_MaxAE_ = []
        for i in errors_line_idxs:
            dim = int(fin_lines[i-1].strip().split()[0][:-1])
            RMSE = float(fin_lines[i].strip().split()[-2])
            MaxAE = float(fin_lines[i].strip().split()[-1])
            path_RMSE_.append(RMSE)
            path_MaxAE_.append(MaxAE)
        RMSE_dict[path_] = path_RMSE_
        MaxAE_dict[path_] = path_MaxAE_
    return RMSE_dict, MaxAE_dict


def get_validation_RMSE_and_MaxAE(paths, path_prefix, number_of_descriptors):
    RMSE_dict = {}
    MaxAE_dict = {}

    for path_ in paths:
        fin = open(path_prefix+path_+'predict_Y.out', 'r')
        fin_lines = fin.readlines()
        path_RMSE_ = []
        path_MaxAE_ = []
        for i in range(number_of_descriptors):
            dim = int(fin_lines[4*i].strip().split()[-1])
            RMSE = float(fin_lines[4*i+3].strip().split()[-2])
            MaxAE = float(fin_lines[4*i+3].strip().split()[-1])
            path_RMSE_.append(RMSE)
            path_MaxAE_.append(MaxAE)
        RMSE_dict[path_] = path_RMSE_
        MaxAE_dict[path_] = path_MaxAE_
    return RMSE_dict, MaxAE_dict


def get_dataframe_from_dict(errors_dict: dict) -> pd.DataFrame:
    errors = pd.DataFrame.from_dict(errors_dict, orient='index', columns=(1, 2, 3, 4, 5, 6))
    errors.loc['mean'] = errors.mean()
    return errors


def get_full_set_desc_dat(path_prefix: str, max_dim: int) -> pd.DataFrame:
    fin = open(path_prefix+f'desc_00{max_dim}d_p001.dat', 'r')
    fin_lines = fin.readlines()
    full_set_desc_columns = fin_lines[0].strip().split()[1:3]
    full_set_desc = {int(line.strip().split()[0]): (float(line.strip().split()[1]), float(line.strip().split()[2])) for line in fin_lines[1:]}
    full_set_desc = pd.DataFrame.from_dict(full_set_desc, orient='index', columns=full_set_desc_columns)

    return full_set_desc


def plot_energy_vs_configuration(full_set_desc) -> None:
    plt.plot(full_set_desc['y_measurement'], 'o', label='measurement')
    plt.plot(full_set_desc['y_fitting'], 's', label='prediction')
    plt.legend()
    plt.xlabel('Index of configuration')
    plt.ylabel('Energy')
    plt.show()


def get_full_set_desc_dat_errors(full_set_desc):
    RMSE, MaxAE = (full_set_desc['y_measurement'] - full_set_desc['y_fitting']).std(), (full_set_desc['y_measurement'] - full_set_desc['y_fitting']).max()
    return RMSE, MaxAE