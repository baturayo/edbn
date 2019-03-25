from TANE import map_attributes
import re


def import_metanome_fds(current_attributes):
    attribute_mappings = map_attributes(current_attributes)

    # FD Path
    fd_path = '../tane-1.0/output/'
    with open(fd_path + 'metanome.log', 'r') as f:
        unstructured_fds = f.read()
        multi_parent_fds = []
        mappings = []
        regex = '[0-9,]+->[0-9]+'
        fds = re.findall(regex, unstructured_fds)

        for fd in fds:
            fd = re.findall(r"[\w']+", fd)
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
import_metanome_fds(0)