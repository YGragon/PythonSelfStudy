from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    error_countys = []
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code


    # 如果没有找到指定的国家，则返回None
    return None