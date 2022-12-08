import inspect
import os
from datetime import datetime
from functools import wraps

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_base_path = os.path.join(base_path, 'img')


def screenshot(driver, case_name, img_base_path):
    screenshotPath = os.path.join(img_base_path, case_name)
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    screen_shot_name = 'CheckPoint_NG.png'
    screen_img = screenshotPath + '_' + time_now + '_' +screen_shot_name
    driver.get_sreenshot_as_file(screen_img)
    return screen_img


def get_current_function_name():
    return inspect.stack()[1][3]


def screenshot_about_case(func):
    @wraps(func)
    def get_screenshot_about_case(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as e:
            case_name = '{}_{} invoked'.format(self.__class__.__name__, get_current_function_name())
            screenshotPath = os.path.join(img_base_path, case_name)
            time_now = datetime.now().strftime('%Y%m%d%H%M%S')
            screen_shot_name = 'CheckPoint_NG.png'
            screen_img = screenshotPath + '_' + time_now + '_' + screen_shot_name
            self.driver.get_sreenshot_as_file(screen_img)
            raise e
    return get_screenshot_about_case