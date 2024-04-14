# -*- coding: utf-8 -*-
"""EXPT7_KMC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sxe6BBciuXDvm3bLoA-DKoOh2xm0t5LJ
"""

import random
import math

def assign_clusters(x, y, l, dict_vals_c):

    # Find distance from Centroid 1, Centroid 2 and Centroid k for each value of Height and Weight and also assign Cluster for each
    dict_dst_c = dict()
    asgn_c = list()

    # Get list of indices for each assigned cluster
    dict_idcs_c = dict()

    for centroid, values in dict_vals_c.items():
        list_dst_c = list()
        for i in range(l):
            # print(x[i], y[i])
            d_c = math.sqrt((values[0] - x[i])**2 + (values[1] - y[i])**2)
            list_dst_c.append(round(d_c, 2))
        print(list_dst_c)
        dict_dst_c[f'{centroid}'] = list_dst_c

    print(dict_dst_c)

    for i in range(l):
        for centroid, distances in dict_dst_c.items():
            for other_centroid, other_distances in dict_dst_c.items():
                if centroid != other_centroid:
                    if distances[i] < other_distances[i]:
                        if centroid not in dict_idcs_c:
                            dict_idcs_c[centroid] = [i]
                            asgn_c.append(centroid)
                        else:
                            dict_idcs_c[centroid].append(i)
                            asgn_c.append(centroid)

    print(dict_idcs_c)
    print(asgn_c)

    return (dict_dst_c, asgn_c, dict_idcs_c)

# Get new Centroids
# dict_idcs_c = {'C1': [1, 2], 'C2': [0, 3, 4, 5, 6, 7, 8, 9, 10, 11]}
def calculate_centroid(x, y, dict_idcs_c):
    new_c = dict()
    for cluster, idcs in dict_idcs_c.items():
        new_h = new_w = 0
        for idx in idcs:
            new_h += x[idx]
            new_w += y[idx]
        new_h /= len(idcs)
        new_w /= len(idcs)
        new_c[f'{cluster}'] = (new_h, new_w)

    print(new_c)
    return new_c

def main():
    # Height
    x = [185, 170, 168, 179, 182, 188, 180, 180, 183, 180, 180, 177]
    # Weight
    y = [72, 56, 60, 68, 72, 77, 71, 70, 84, 88, 67, 76]

    l = len(x)

    k = int(input('Enter the value of \'k\': '))

    # Generate the indices of Centroid 1, Centroid 2 and Centroid k randomly and get the corresponding values of Weight and Height
    # Dictionary of indices of Centroids
    '''dict_vals_c = dict()
    for i in range(k):
        idx_c = random.randint(0, l)
        h_c = x[idx_c]
        w_c = y[idx_c]
        dict_vals_c[f'C{i+1}'] = (h_c, w_c)'''

    dict_vals_c = {'C1': (170, 56), 'C2': (182, 72)}

    print(f'Centroid with corresponding Height and Weight values: {dict_vals_c}')

    print(dict_vals_c)

    for centroid, values in dict_vals_c.items():
        print(centroid, values[0], values[1])
    stop_condition = False
    iteration = 0
    while not stop_condition:

        iteration += 1
        print(f'Iteration: {iteration}')

        dict_dst_c, asgn_c, dict_idcs_c = assign_clusters(x, y, l, dict_vals_c)
        dict_vals_c_new = calculate_centroid(x, y, dict_idcs_c)
        print(f'Assigned Cluster: {asgn_c}')

        if dict_vals_c == dict_vals_c_new:
            stop_condition = True
            print('No change in clusters.')
        else:
            dict_vals_c = dict_vals_c_new
            print('Clusters change')

if __name__ == "__main__":
    main()