import json
from util import JsonUtils
from pyecharts.charts import Line
from pyecharts.options import (LabelOpts, LegendOpts, TitleOpts, ToolboxOpts,
                               VisualMapOpts)

if __name__ != "__main__":
    line = Line()
    line.add_xaxis(["Chinese", "America", "Britain"])
    line.add_yaxis("GDP", [30, 20, 25])

    # 设置全局配置项 set_global_opts
    line.set_global_opts(
        title_opts=TitleOpts(
            title="GDP 展示", pos_left="center", pos_bottom="1%"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True)
    )

    line.render()


def readTestFile():
    with open("美国.txt", "r", encoding="UTF-8") as f:
        us_data = f.read()
        us_data = us_data.replace("jsonp_xxx_xx(", "")
        us_data = us_data[:-2]
        us_dict = JsonUtils.fromJson(us_data)
        # print(type(us_dict))
        # print(us_dict)
        # dict 的 key 可以为任何类型, 包括数字; 但不能是字典和可变类型
        trend_data = us_dict["data"][0]["trend"]
        x_data = trend_data["updateDate"][:314]
        y_data = trend_data["list"][0]["data"][:314]


def readTrueFile():
    with open("美国.txt", "r", encoding="UTF-8") as f:
        us_data = f.read()
        us_dict = JsonUtils.fromJson(us_data)
        dataList = us_dict["Data"]
        x_data = [str(dataList[i]["UpdateTime"])
                  for i in range(0, len(dataList))]
        y_data = [dataList[i]["DeadCount"] for i in range(0, len(dataList))]
        print(len(x_data))
        print(len(y_data))
        line = Line()
        line.add_xaxis(x_data)
        line.add_yaxis("美国死亡人数", y_data, label_opts=LabelOpts(is_show=False))

        # 设置全局配置项 set_global_opts
        line.set_global_opts(
            title_opts=TitleOpts(
                title="美国疫情展示", pos_left="center", pos_bottom="1%"),
            legend_opts=LegendOpts(is_show=True),
            toolbox_opts=ToolboxOpts(is_show=True),
            visualmap_opts=VisualMapOpts(is_show=True)
        )
        line.render("美国疫情死亡人数.html")


readTrueFile()


def readFile():
    with open("美国.txt", "r", encoding="UTF-8") as f:
        result = json.load(f)  # load = loads(f.read())
        print(result)
        print(type(result))
