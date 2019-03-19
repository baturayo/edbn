from Utils import Uncertainty_Coefficient as uc
from sklearn import preprocessing
from Utils.LogFile import LogFile
import pandas as pd

if __name__ == "__main__":
    # Import Data
    data_path = "../Data/bpic15_1_train.csv"  # "../Data/BPIC15_train_1.csv"
    # data = data.dropna(axis=1)
    # data = data.dropna(axis=0)

    # # Convert data to numeric values
    #data = data.apply(preprocessing.LabelEncoder().fit_transform)
    #N = 50000
    #data = data.sample(N)
    #data.columns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    #data_out_path = '/Users/baturay/courses/UA-Master/Thesis/Metanome/deployment/target/deployment-1.2-SNAPSHOT-package_with_tomcat/backend/WEB-INF/classes/inputData/'
    #data.to_csv(data_out_path +'/BPIC_R_%s.csv' % N, index=False)
    #
    # fname = '../Data/test_.csv'
    # data = read_all_raw_file(data_path)
    # print(data.head(100))
    train_data = LogFile(filename=data_path, delim=",", header=0, rows=500000, time_attr=None, trace_attr="Case ID")
    train_data.remove_attributes(["Anomaly"])

    # train_data.keep_attributes(["Case_ID", "Complete_Timestamp", "Activity", "Resource", "case_termName"])
    train_data.remove_attributes(["planned"])
    train_data.remove_attributes(["dueDate"])
    train_data.remove_attributes(["dateFinished"])
    # # # Train the model
    #train_data.create_k_context()

    # # train_data.contextdata =
    #train_data.contextdata.sample(10000).to_csv('BPIC_1_k_0_10000.csv', index=False)
    train_data.data.sample(10000).to_csv('BPIC_1_k_0_10000.csv', index=False)
    # # Calculate Mappings
    # mappings = uc.calculate_mappings(data, data.columns, 0, 0.99)
    # print(mappings)