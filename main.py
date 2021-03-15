def parse(query: str) -> dict:
        list = query.split(";")
        tmp_dict = {}
        for i in list:
            tmp_list = i.split("=", 1)
            try:
                tmp_dict.update({tmp_list[0]: tmp_list[1]})
            except IndexError:
                break
        else:
            return {}

        return tmp_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}