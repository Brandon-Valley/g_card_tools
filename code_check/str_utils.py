


def multi_dim_split(dim_l, str_to_split):
    s_l = [str_to_split]
    for dim in dim_l:
        new_s_l = []
        for str_to_split in s_l:
            split_str_l = str_to_split.split(dim)
            for split_str in split_str_l:
                new_s_l.append(split_str)
        s_l = new_s_l
    return s_l