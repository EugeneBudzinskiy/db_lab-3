import re
from database import db


class BusinessLogicLayer:
    def __init__(self):
        self.empty_message = 'Fill up this field!'
        self.error_message = 'Wrong value!'
        self.exist_message = 'This value already exist!'
        self.non_exist_message = "This value doesn't exist!"

    def check_if_empty(self, data, data_decode, validation_result):
        for key in data_decode.keys():
            if not data[key]:
                validation_result[key] = self.empty_message
        return validation_result

    def check_if_regex(self, data, data_decode, validation_result):
        for key in data_decode.keys():
            if data[key]:
                if not re.search(data_decode[key]['regex'], data[key]):
                    validation_result[key] = self.error_message
        return validation_result

    def check_if_exist(self, table_name, data, data_decode, validation_result):
        for key in data_decode.keys():
            current_unique = data_decode[key]['unique']
            current_connected = data_decode[key]['connected']

            if current_unique and current_connected is None:
                if data[key]:
                    if DataAccessor.read_from_table(table_name=table_name, read_id=data[key]):
                        validation_result[key] = self.exist_message

            elif current_unique and current_connected is not None:
                if data[key]:
                    if not DataAccessor.read_from_table(table_name=current_connected, read_id=data[key]):
                        validation_result[key] = self.non_exist_message

        return validation_result

    def validate_addition(self, table_name, data, data_decode):
        validation_result = dict((k, None) for k in data_decode.keys())
        complete_data = dict((key, data[key]) if key in data.keys() else (key, None) for key in data_decode.keys())

        validation_result = self.check_if_exist(
            table_name=table_name, data=complete_data, data_decode=data_decode, validation_result=validation_result
        )
        validation_result = self.check_if_regex(
            data=complete_data, data_decode=data_decode, validation_result=validation_result
        )
        validation_result = self.check_if_empty(
            data=complete_data, data_decode=data_decode, validation_result=validation_result
        )

        return validation_result


class DataAccessorLayer:
    def __init__(self, orm):
        self.orm = orm

    @staticmethod
    def collect_data_to_tuple(collect, items):
        data = list()
        for idx, true_idx in items:
            val = collect.get(idx)
            if val:
                data.append(true_idx == val)
        return tuple(data)

    @staticmethod
    def collect_data_to_dict(collect, keys):
        data = dict()
        for key in keys:
            value = collect.get(key)
            if value:
                data[key] = value.strip()
        return data

    @staticmethod
    def get_pagination(data, get_query_data, rows_per_page):
        page = get_query_data.get('page', 1, type=int)
        return data.paginate(page=page, per_page=rows_per_page)

    def get_all_tables(self, get_query_data, join_decode, rows_per_page):
        data = self.orm.session.query(*join_decode['table_to_use'])

        for rule in join_decode['join_rule']:
            name, on = rule['name'], rule['on']
            data = data.join(name) if on is None else data.join(name, on)

        search_data = \
            self.collect_data_to_tuple(collect=get_query_data, items=join_decode['index_representation'].items())

        data = data.filter(*search_data) if search_data else data
        data = data.order_by(join_decode['order_by'])
        data = self.get_pagination(data=data, get_query_data=get_query_data, rows_per_page=rows_per_page)
        return data

    def get_single_table(self, table_name, validation_index, get_query_data, rows_per_page):
        search_data = self.collect_data_to_dict(collect=get_query_data, keys=validation_index)

        data = table_name.query.filter_by(**search_data) if search_data else table_name.query
        data = data.order_by(table_name.id)
        data = self.get_pagination(data=data, get_query_data=get_query_data, rows_per_page=rows_per_page)

        return data

    def create_in_table(self, table_name, data, column_to_create):
        create_data = self.collect_data_to_dict(collect=data, keys=column_to_create)
        self.orm.session.add(table_name(**create_data))
        self.orm.session.commit()

    def read_from_table(self, table_name, read_id):
        data = self.orm.session.query(table_name).filter(table_name.id == read_id).first() if read_id else None
        return data

    def update_in_table(self, table_name, edit_id, data, column_to_edit):
        update_data = self.collect_data_to_dict(collect=data, keys=column_to_edit)
        self.orm.session.query(table_name).filter(table_name.id == edit_id).update(update_data)
        self.orm.session.commit()

    def delete_from_table(self, table_name, delete_id):
        self.orm.session.query(table_name).filter(table_name.id == delete_id).delete()
        self.orm.session.commit()


DataAccessor = DataAccessorLayer(orm=db)
BusinessLogic = BusinessLogicLayer()
