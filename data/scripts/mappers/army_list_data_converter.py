class ArmyListDataConverter:

    def __init__(self, army_lists):
        self.__army_lists = army_lists

    def convert_to_json_dict(self):
        self.__army_lists.index = self.__army_lists.name
        self.__army_lists['additional_rules'] = self.__army_lists['additional_rules'].apply(eval)
        self.__army_lists['special_rules'] = self.__army_lists['special_rules'].apply(eval)
        self.__army_lists['rule_highlights'] = self.__army_lists['rule_highlights'].apply(eval)

        self.__army_lists = self.__army_lists[['additional_rules', 'special_rules', 'rule_highlights']]
        json_dict = self.__army_lists.to_dict(orient='index')
        json_dict = {f:{k:v for k,v in json_dict[f].items() if v != ""} for f in json_dict.keys()}

        return json_dict