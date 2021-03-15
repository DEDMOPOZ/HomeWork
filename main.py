def parse_cookie(query: str) -> dict:
    list = query.split(";")
    tmp_dict = {}
    for i in list:
        tmp_list = i.split("=", 1)
        try:
            tmp_dict.update({tmp_list[0]:tmp_list[1]})
        except IndexError:
            break
    else: return {}

    return tmp_dict

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
