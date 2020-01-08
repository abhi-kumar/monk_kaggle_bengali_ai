from gluon.datasets.imports import *
from system.imports import *


@accepts([int, tuple], dict, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def set_input_size(input_size, system_dict):
    system_dict["dataset"]["params"]["input_size"] = input_size;
    return system_dict;

@accepts(int, dict, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def set_batch_size(batch_size, system_dict):
    system_dict["dataset"]["params"]["batch_size"] = batch_size;
    return system_dict;
    
@accepts(bool, dict, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def set_data_shuffle(value, system_dict):
    train_shuffle = value;
    val_shuffle = value;
    system_dict["dataset"]["params"]["train_shuffle"] = train_shuffle;
    system_dict["dataset"]["params"]["val_shuffle"] = val_shuffle;
    return system_dict;
    
@accepts(int, dict, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def set_num_processors(num_workers, system_dict):
    system_dict["dataset"]["params"]["num_workers"] = num_workers;
    return system_dict;

@accepts(bool, dict, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def set_weighted_sampling(sample, system_dict):
    system_dict["dataset"]["params"]["weighted_sample"] = sample;
    return system_dict;

def set_competition_name(competition, system_dict):
    system_dict["kaggle"]["competition"] = competition;
    return system_dict;

def set_data_root(data_root, system_dict):
    system_dict["kaggle"]["dataset"]["data_root"] = data_root;
    return system_dict;

def set_target(target, system_dict):
    system_dict["kaggle"]["dataset"]["target"] = target;
    return system_dict;

def set_read(read, system_dict):
    system_dict["kaggle"]["dataset"]["read"] = read;
    return system_dict;

def set_percent_data(percent_data, system_dict):
    system_dict["kaggle"]["dataset"]["percent_data"] = percent_data;
    return system_dict;

def set_trainval_split(split, system_dict):
    system_dict["dataset"]["params"]["train_val_split"] = split;
    return system_dict;



def set_kaggle_dataset_params(system_dict):
    files = os.listdir(system_dict["kaggle"]["dataset"]["data_root"]);
    parquet = [];
    parquet_train = [];
    parquet_test = [];
    csv = [];
    csv_train = [];
    csv_test = [];
    for i in range(len(files)):
        ext = files[i].split(".")[-1];
        if(ext == "csv"):
            csv.append(files[i]);
        elif(ext == "parquet"):
            parquet.append(files[i]);

    if(system_dict["states"]["eval_infer"]):
        for i in range(len(parquet)):
            if("test" in parquet[i].split(".")[0]):
                parquet_test.append(system_dict["kaggle"]["dataset"]["data_root"] + "/" + parquet[i]);
        for i in range(len(csv)):
            if("test" in csv[i].split(".")[0]):
                csv_test.append(system_dict["kaggle"]["dataset"]["data_root"] + "/" + csv[i]);
        system_dict["kaggle"]["dataset"]["parquet_files_test"] = parquet_test;
        system_dict["kaggle"]["dataset"]["csv_test"] = csv_test;
    else:
        for i in range(len(parquet)):
            if("train" in parquet[i].split(".")[0]):
                parquet_train.append(system_dict["kaggle"]["dataset"]["data_root"] + "/" + parquet[i]);
        for i in range(len(csv)):
            if("train" in csv[i].split(".")[0]):
                csv_train.append(system_dict["kaggle"]["dataset"]["data_root"] + "/" + csv[i]);
        system_dict["kaggle"]["dataset"]["parquet_files_train"] = parquet_train;
        system_dict["kaggle"]["dataset"]["csv_train"] = csv_train;

    return system_dict;