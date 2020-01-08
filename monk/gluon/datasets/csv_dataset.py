from gluon.datasets.imports import *
from system.imports import *



class DatasetCustom(Dataset):
    @accepts("self", list, list, str, post_trace=True)
    @TraceFunction(trace_args=False, trace_rv=False)
    def __init__(self, img_list, label_list, prefix):
        self.img_list = img_list;
        self.label_list = label_list;
        self.prefix = prefix;
    
    @accepts("self", post_trace=True)
    @TraceFunction(trace_args=False, trace_rv=False)    
    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, index):
        image_name = self.prefix + "/" + self.img_list[index];
        img = image.imread(image_name);
        label = int(self.label_list[index]);       
        return img, label



class DatasetCustomKaggleBengaliAI(Dataset):
    def __init__(self, dataset_parquet_files, img_list, label_list, read):
        self.label_list = [];
        self.img_list = [];
        self.parquet_list = [0 ,0, 0, 0];
        dataset_parquet_files = sorted(dataset_parquet_files);
        if(0 in read):
            print("reading {}".format(dataset_parquet_files[0]))
            self.label_list += label_list[:50210]
            self.img_list += img_list[:50210]
            self.parquet_list[0] = pd.read_parquet(dataset_parquet_files[0]);
        if(1 in read):
            print("reading {}".format(dataset_parquet_files[1]))
            self.label_list += label_list[50210:100420]
            self.img_list += img_list[50210:100420]
            self.parquet_list[1] = pd.read_parquet(dataset_parquet_files[1]);
        if(2 in read):
            print("reading {}".format(dataset_parquet_files[2]))
            self.label_list += label_list[100420:150630]
            self.img_list += img_list[100420:150630]
            self.parquet_list[2] = pd.read_parquet(dataset_parquet_files[2]);
        if(3 in read):
            print("reading {}".format(dataset_parquet_files[3]))
            self.label_list += label_list[150630:]
            self.img_list += img_list[150630:]
            self.parquet_list[3] = pd.read_parquet(dataset_parquet_files[3]);

        print("Done\n");

    def __len__(self):
        return len(self.img_list);

    
    def __getitem__(self, index):
        if(index >= 0 and index < 50210):
            row = np.array(self.parquet_list[0].iloc[index][1:])
            row = np.reshape(row, (137, 236, 1))
            img = mx.nd.array(row);
            label = int(self.label_list[index]);
        elif(index >= 50210 and index <= 100420):
            row = np.array(self.parquet_list[1].iloc[50210-index][1:])
            row = np.reshape(row, (137, 236, 1))
            img = mx.nd.array(row);
            label = int(self.label_list[index]);
        elif(index >= 100420 and index <= 150630):
            row = np.array(self.parquet_list[2].iloc[100420-index][1:])
            row = np.reshape(row, (137, 236, 1))
            img = mx.nd.array(row);
            label = int(self.label_list[index]);
        elif(index >= 150630):
            row = np.array(self.parquet_list[3].iloc[150630-index][1:])
            row = np.reshape(row, (137, 236, 1))
            img = mx.nd.array(row);
            label = int(self.label_list[index]);
        

        return img, label