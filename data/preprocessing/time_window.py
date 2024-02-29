import numpy as np
import pandas as pd

def time_window(data, window_size, overlapping=0.5, u=0):
    """
    param data: DataFrame of shape (n_records, dim), where the headers are: "sensor names" + "Subject" + "Activity_Number"
    param window_size: Size of the time windows
    param overlapping: % of records (0-1) included from the previous time window in the current window
    return: Numpy array of shape (n_windows, size, dim), Numpy array of labels of each window
    WARNINGS:
    * If the data is not size-compatible with the desired time window size, the last records will be omitted.
    * If the overlapping is not compatible with the window_size parameter, then the least integer will be considered.
        For instance: Given window_size=3 and overlapping=0.5, the number of records from the previous window will be 1.
    """

    headers = data.columns.to_list() 
    label_index = headers.index("Activity_Number")
    subject_index = headers.index("Subject")

    data = np.array(data)

    feature_index = [i for i in range(data.shape[1]) if i != label_index and i != subject_index]

    sensor_names = [headers[i] for i in feature_index]

    windows = []
    window_labels = []
    #u=0.5 #Solo se aceptan ventanas si no tienen ningún nulo en ninguna de sus columnas, 
        #si colocas u=0 , no va a aceptar ventanas que tengan nulos

    classes = np.unique(data[:, label_index])
    prev_rec = int(overlapping * window_size)

    for given_class in classes:
        sub_data = data[data[:, label_index] == given_class]
        c = 0
        while c+window_size < sub_data.shape[0]:
            window = sub_data[c:c + window_size, feature_index]
            max_NaN=np.max(np.sum(pd.isnull(window), axis=0))
            if max_NaN<=u*window_size:
               
                windows.append(window)
                window_labels.append(sub_data[c+window_size-1, label_index])
                
            else:
                pass
            c += window_size - prev_rec

    return np.array(windows), np.array(window_labels), sensor_names


def handcrafted_features(windows, functions, function_names, sensor_names):
    """
    param windows: Numpy array of shape (n_windows, size, dim)
    param functions: List of functions to be applied along "size" for each window.
    return: Numpy array of shape (n_windows, len(functions)*dim)
    """
    n_windows = windows.shape[0]
    dim = windows.shape[2]
    features = np.zeros((n_windows, len(functions)*dim))
    d = 0
    for function in functions:
        for i in range(n_windows):
            window = windows[i]
            feature = np.apply_along_axis(function, 0, window)
            features[i][d:d+dim] = feature
        d += dim
    column_names = []
    for function_name in function_names:
      for sensor_name in sensor_names:
        column_names.append(function_name+"_"+sensor_name)
    return features, column_names
