from skimage import io
import os
import numpy as np
import pandas as pd

class Rectangle:
    def __init__(self, x, y, w, h):
        self.xmin = x
        self.ymin = y
        self.w = w
        self.h = h
        self.xmax = x+w
        self.ymax = y+h
        self.area = w*h

def get_intersection(rect1: Rectangle, rect2: Rectangle):
    x_dist = (min(rect1.xmax, rect2.xmax) - max(rect1.xmin, rect2.xmin))
    y_dist = (min(rect1.ymax, rect2.ymax) - max(rect1.ymin, rect2.ymin))

    intersection = 0

    if x_dist > 0 and y_dist > 0:
        intersection = x_dist * y_dist

    return intersection

def get_metrics(path_csv_test, path_csv_val):
    columns = ['name', 'i', 'j', 'w', 'h', 'score']

    try:
        test_df = pd.read_csv(path_csv_test, header=None)
        val_df = pd.read_csv(path_csv_val, header=None)

        test_df.columns = columns
        val_df.columns = columns

        test_list = test_df.values.tolist()
        val_list = val_df.values.tolist()

        matches = []

        for index_test, test in enumerate(test_list):
            name_t, x_t, y_t, w_t, h_t, _ = test
            rect1 = Rectangle(x_t, y_t, w_t, h_t)
            for index_val, val in enumerate(val_list):
                name_v, x_v, y_v, w_v, h_v, _ = val
                if name_t == name_v:
                    rect2 = Rectangle(x_v, y_v, w_v, h_v)
                    intersection = get_intersection(rect1, rect2)
                    if intersection != 0 and rect1.area / intersection > 0.5:
                        del val_list[index_val]
                        matches.append(index_test)
                        break

        true_positive = len(matches)
        false_positive = len(test_list) - true_positive
        false_negative = len(val_list)

        precision = true_positive / (true_positive + false_positive)
        recall = true_positive / (true_positive + false_negative)
        f1 = 2 / (1 / precision + 1 / recall)

        return {
            'precision': precision,
            'recall': recall,
            'f1': f1
        }
    except Exception:
        return {
            'precision': 0,
            'recall': 0,
            'f1': 0
        }

def generate_csv_from_label_list(label_path, img_path, save_file, is_not_scored=False):
    labels_list = []

    labels = os.listdir(label_path)

    for lbl in sorted(labels):
        detect = np.loadtxt(os.path.join(label_path, lbl), ndmin=2)

        filename = lbl[:-4]

        img = io.imread(os.path.join(img_path, filename+'.jpg'))
        shape_y, shape_x, _ = img.shape

        for d in detect:
            if is_not_scored:
                _, i, j, w, h = d
                score = 1
            else:
                _, i, j, w, h, score = d

            i = (i - w / 2) * shape_x
            j = (j - h / 2) * shape_y

            w *= shape_x
            h *= shape_y

            labels_list.append([filename+'.jpg',int(j), int(i), int(h), int(w), score])

    labels_df = pd.DataFrame(labels_list)
    labels_df.to_csv(save_file, header=False, index=False)

    return save_file