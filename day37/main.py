"""
Project Calling Pixela API
"""

"""
NOTE: HTTP methods
GET: requests.get()
POST: requests.post()
PUT: requests.put()
DELETE: requests.delete()
"""

from helper import (
    create_user,
    create_graph,
    create_pixel,
    update_pixel,
    delete_pixel,
)


def main():
    
    """
    HACK:下記の感じでCLI化したら毎日実際に使えるアプリにできそう👇
    
    date = input('What date of pixcle do you want to edit')
    
    params = {
        graph_id: input('What graph do you want to edit')
    }
    
    
    
    """
    
    """
    NOTE:一番最初にだけ呼び出す処理（ユーザ作成、グラフ作成）
        インタフェースの余地あり
    res = _create_user()
    
    res = create_graph(
        id='graph1',
        graph_name='Coding Graph',
        unit='m',
        type='int',
        color='ichou'
        )
    
    """
    
    
    # res = create_pixel('graph1', '3')
    
    # res = update_pixel('graph1', '4')
    
    res = delete_pixel('graph1')
    
    print(res.text)


    
    
    
if __name__ == '__main__':
    main()