def surround_by(a_list, c):
    if isinstance(a_list, list):
        return ['{c}{e}{c}'.format(c=c, e=e) for e in a_list]
    else:
        return a_list


class FilterModule(object):
    def filters(self):
        return {'surround_by': surround_by}
