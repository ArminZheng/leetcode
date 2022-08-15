from pyecharts.globals import ThemeType
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *


def bar():
    bar = Bar()
    bar.add_xaxis(["中", "美", "英"])  # axis 轴
    bar.add_yaxis("GDP", [30, 20, 10],  label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    bar.render("基础柱状图.html")


def timeline():
    bar1: Bar = Bar()
    bar1.add_xaxis(["中", "美", "英"])  # axis 轴
    bar1.add_yaxis("GDP", [30, 20, 10],
                   label_opts=LabelOpts(position="right"))
    bar1.reversal_axis()

    bar2 = Bar()
    bar2.add_xaxis(["中", "美", "英"])  # axis 轴
    bar2.add_yaxis("GDP", [35, 25, 18],
                   label_opts=LabelOpts(position="right"))
    bar2.reversal_axis()
    timeline = Timeline({"theme": ThemeType.LIGHT})
    timeline.add(bar1, "2021")
    timeline.add(bar2, "2022")

    timeline.add_schema(
        play_interval=1000,  # 毫秒
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=True
    )

    timeline.render("基础柱状图-时间线.html")


if __name__ == "__main__":
    timeline()
    
