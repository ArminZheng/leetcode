import json
from pyecharts.charts import Map
from pyecharts.options import *

if __name__ == "__main__":
    map = Map()
    data = [
        ("北京", 99),
        ("上海", 199),
        ("湖南", 299),
        ("台湾", 399),
        ("广东", 499),
        ("重庆", 599),
    ]
    map.add("Test Map", data, "china")

    map.set_global_opts(
        visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=[{
                                     "min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 11, "max": 100, "label": "11-100", "color": "#FF6666"},
            {"min": 101, "max": 500, "label": "101-500", "color": "#990033"}
        ]
        )
    )

    map.render("地图表格.html")


def covid19Map():
    with open("疫情地图.txt", "r", encoding="UTF-8") as f:
        data_dict = json.load(f)
    province_data_list = data_dict["areaTree"][0]["children"]
    data_list = [(province_data["name"], province_data["total"]["confirm"])
                 for province_data in province_data_list]
    map = Map()
    map.add("各省确诊人数", data_list, "china")
    map.set_global_opts(
        title_opts=TitleOpts(title="全国疫情地图"),
        visualmap_opts=VisualMapOpts(is_show=True,  # 是否显示
                                     is_piecewise=True,  # 是否分段
                                     pieces=[
                                         {"min": 1, "max": 99, "label": "1-99人",
                                             "color": "#CCFFFF"},
                                         {"min": 100, "max": 999,
                                             "label": "100-999", "color": "#FF6666"},
                                         {"min": 1000,
                                             "label": "1000+", "color": "#990033"}
                                     ])
    )
    map.render("全国疫情地图.html")
    
# python 和 js 都是动态类型语言, js 单独为弱类型语言 (强类型代表类型安全 严谨)
# 弱类型定义的语言，某一个变量被定义类型，该变量可以根据环境变化自动转换，不需要经过强制转换
# 动态语言与静态语言的根本不同，在于做数据类型检查是在 运行期间 还是 编译期间
# 性能有些时候并不那么重要


