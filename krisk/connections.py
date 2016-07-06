
from collections import OrderedDict
from IPython.display import Javascript
import json
from krisk.util import join_current_dir

ECHARTS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/echarts/3.2.0/'
ECHARTS_FILE = 'echarts.min'
d_paths = OrderedDict({})
THEMES = ['dark','vintage','roma','shine','infographic','macarons']
THEMES_URL='//echarts.baidu.com/asset/theme/'
PATH_LOCAL = 'pandas-echarts/krisk/static'
#TODO FIX LOCAL PATH!

def init_notebook(online=True):
    """Inject Javascript to notebook, default using local js.
    
    """
    return Javascript("""
    require.config({
                 baseUrl : '%s',
                 paths: {
                     echarts: 'echarts.min'
                 }
    });
    """ % PATH_LOCAL)
    
def get_paths():
    return ['echarts'] + THEMES