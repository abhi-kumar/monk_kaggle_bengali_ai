import os
import sys
sys.path.append("../../../monk/");
import psutil

from keras_prototype import prototype



ktf = prototype(verbose=1);
ktf.Prototype("sample-project-1", "sample-experiment-1");



######################################################Dataset Params #################################################################
ktf.Dataset_Params(dataset_path="../../../monk/system_check_tests/datasets/dataset_cats_dogs_train", split=0.9,
        input_size=224, batch_size=16, shuffle_data=True, num_processors=3);
#################################################################################################################################################








########################################################### Transforms ####################################################
ktf.apply_random_horizontal_flip(train=True, val=True);
ktf.apply_mean_subtraction(mean=[0.485, 0.456, 0.406], train=True, val=True, test=True);
#################################################################################################################################################


############################################ Auxiliary Functions - List all available transforms #########################################
ktf.List_Transforms()
######################################################################################################################################








########################################################## Set Dataset ###################################################################
ktf.Dataset();
##########################################################################################################################################






######################################################Model Params #################################################################
ktf.Model_Params(model_name="resnet50", freeze_base_network=True, use_gpu=True, gpu_memory_fraction=0.7, use_pretrained=True);
##########################################################################################################################################


############################################ Auxiliary Functions - List all available models #########################################
ktf.List_Models();
######################################################################################################################################








#################################################   Apply additional layers to model ####################################################################
ktf.append_dropout(probability=0.1);
ktf.append_linear(final_layer=True);
######################################################################################################################################


############################################ Auxiliary Functions - List all available layers and activations #########################################
ktf.List_Layers();
ktf.List_Activations();
######################################################################################################################################




########################################################## Set Model ###################################################################
ktf.Model();
##########################################################################################################################################


############################################ Auxiliary Functions - Freeze Layers #########################################
ktf.Freeze_Layers(num=10);
######################################################################################################################################





########################################################## Training Params ###################################################################
ktf.Training_Params(num_epochs=2, display_progress=True, display_progress_realtime=True, 
        save_intermediate_models=True, intermediate_model_prefix="intermediate_model_", save_training_logs=True);
######################################################################################################################################





################################################ Set Optimizer #########################################################################
ktf.optimizer_adam(0.0001);
#################################################################################################################################################


############################################ Auxiliary Functions - List all available optimizers #########################################
ktf.List_Optimizers();
######################################################################################################################################







################################################ Set Learning rate schedulers #################################################################
ktf.lr_fixed();
#################################################################################################################################################


############################################ Auxiliary Functions - List all available schedulers #########################################
ktf.List_Schedulers();
######################################################################################################################################








################################################ Set Loss #################################################################
ktf.loss_crossentropy()
#################################################################################################################################################


############################################ Auxiliary Functions - List all available losses #########################################
ktf.List_Losses();
######################################################################################################################################




ktf.Train();