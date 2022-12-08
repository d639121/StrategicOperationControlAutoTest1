import os
import yaml

from config.read_config import rc


class GetData:

    def _get_yaml_path(self, yaml_path):
        api_yaml_path = os.path.join(rc.PROJECT_PATH, 'data', yaml_path)
        with open(api_yaml_path, mode="r", encoding="utf-8") as file:
            data = yaml.full_load(file)
        return data

    def get_data(self, yaml_path):
        data = self._get_yaml_path(yaml_path)
        return data

    def deal_data(self, data):
        '''
        封装整体方法
        :param data: 传入的数据
        :return: url, method, header, params, shared, check
        '''
        env = data.get('env')
        user = data.get('user')
        password = data.get('password')
        env = rc.get_env(env)
        return env, user, password


gtd = GetData()
