# TODO здесь писать код
class MyDict(dict):

    def get_dict(self, key, value=0):
        if key in self:
            return self[key]
        else:
            return value


num_dict = MyDict()
num_dict['tom'] = 1
print(num_dict.get_dict('qq'))
