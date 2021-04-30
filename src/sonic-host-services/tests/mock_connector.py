class MockConnector(object):
    STATE_DB = None
    CONFIG_DB = None
    data = {"MGMT_PORT|eth1": {"description": "snowflake", "admin_status": "up"}}

    def __init__(self, host):
        pass

    def connect(self, db_id):
        pass

    def delete_all_by_pattern(self, db_name, pattern):
        pass

    def get(self, db_id, key, field):
        return MockConnector.data[key][field]

    def set(self, db_id, key, field, val):
        MockConnector.data[key] = {}
        MockConnector.data[key][field] = val

    def keys(self, db_id, pattern):
        match = pattern.split('*')[0]
        ret = []
        for key in MockConnector.data.keys():
            if match in key:
                ret.append(key)

        return ret

    def get_all(self, db_id, key):
        return MockConnector.data[key]
