import os
import re
import subprocess


def write_sample_data(data, sample_size):
    """
    Take a sample data from the train set to mine FDs
    :param data: Pandas DF object
    :param sample_size: Number of rows to take the sample
    """
    sample_data = data.head(sample_size)
    sample_data.to_csv('../tane-1.0/original/sample.orig', sep=',', header=False, index=False)


def write_dat_file():
    """
    To run the tane API the data frame needs to be converted to .dat file
    :return:
    """
    command1 = 'cd ../tane-1.0/original/'
    command2 = '../bin/select.perl ../descriptions/data.dsc'
    command = command1 + '&&' + command2
    print(command)
    p = subprocess.Popen(command, shell=True,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
    # allow external program to work
    p.wait()


def import_fds(attribute_mappings):
    fd_path = '../tane-1.0/output/'
    with open(fd_path + 'sample.log', 'r') as f:
        unstructured_fds = f.read()
        multi_parent_fds = []
        mappings = []
        regex = '[0-9 ]+-> [0-9]+'
        fds = re.findall(regex, unstructured_fds)

        for fd in fds:
            fd = fd.split(' ')
            fd.remove('->')
            parents = []

            # Not that for an FD a, c -> b  a and c are parents and b is a child
            # iterate over parents in an FD to map it with the attribute name
            # If the fd has multiple parents
            if len(fd) > 2:
                for parent in fd[:-1]:
                    parents.append(attribute_mappings[parent])
                child = attribute_mappings[fd[-1]]
                multi_parent_fds.append((parents, child))

            # If the fd has single parent
            else:
                fd_tuple = (attribute_mappings[fd[0]], attribute_mappings[fd[1]])
                mappings.append(fd_tuple)

    return mappings, multi_parent_fds


def map_attributes(attribute_names):
    """
    Map integers to attribute names starting from 1 because FDs are shown as integers and they need to be replaced by
    the attribute names for the readibility
    :param attribute_names: List having attribute names
    """
    attribute_mappings = {}
    counter = 1
    for attribute in attribute_names:
        attribute_mappings[str(counter)] = attribute
        counter += 1
    return attribute_mappings


def filter_out_attributes(data, curr_attributes):
    """
    Filter out unused columns from the dataframe
    :param curr_attributes: Current used attributes in variables
    :return: Filtered data frame
    curr_attributes
    """
    prev_attributes = [attr + '_Prev0' for attr in curr_attributes]
    all_attributes = prev_attributes + curr_attributes
    n_attributes = len(all_attributes)
    return data[all_attributes], n_attributes


def run_tane(data, sample_size, n_levels, attributes, threshold, algorithm):
    data, n_attributes = filter_out_attributes(data, attributes)
    write_sample_data(data, sample_size)
    write_dat_file()
    # dat_file_path = '../tane-1.0/data/data.dat'
    # fd_raw_output_path = '../tane-1.0/output/sample.log'
    #
    # if algorithm == 'taneg3':
    #     command_tane = '../tane-1.0/bin/taneg3 {} {} {} {} {}&> {}'.format(str(n_levels),
    #                                                                        str(sample_size),
    #                                                                        str(n_attributes),
    #                                                                        dat_file_path,
    #                                                                        str(threshold),
    #                                                                        fd_raw_output_path)
    # elif algorithm == 'tanemem':
    #     command_tane = '../tane-1.0/bin/tanemem {} {} {} {}&> {}'.format(str(n_levels),
    #                                                                      str(sample_size),
    #                                                                      str(n_attributes),
    #                                                                      dat_file_path,
    #                                                                      fd_raw_output_path)
    # elif algorithm == 'tane':
    #     command_tane = '../tane-1.0/bin/tane {} {} {} {}&> {}'.format(str(n_levels),
    #                                                                      str(sample_size),
    #                                                                      str(n_attributes),
    #                                                                      dat_file_path,
    #                                                                      fd_raw_output_path)
    # else:
    #     raise Exception('{} is not defined. The algorithm can be either taneg3, tanemem or tane'.format(str(algorithm)))
    #
    # print(command_tane)
    # p = subprocess.Popen(command_tane, shell=True,
    #                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
    # # allow external program to work
    # p.wait()
    # attribute_mapping = map_attributes(attributes)
    # return import_fds(attribute_mapping)
    return 0