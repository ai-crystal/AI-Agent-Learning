# -*- coding: utf-8 -*-
"""第 1 章：企业项目交付阶段。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.figstyle import *

set_book("agent-enterprise-cases")


def f01_stages():
    fig, ax = canvas(3.2)
    stages = [
        (5, "任务切片", "选窄而可验证的任务"),
        (25, "离线原型", "历史样本 + 评测"),
        (45, "影子运行", "给建议，不影响流程"),
        (65, "人工确认", "低风险自动，高风险审批"),
        (85, "有限扩展", "按指标扩大范围"),
    ]
    for x, name, desc in stages:
        box(ax, x, 46, 12, 30, "", fc="#f8f7f3", ec="#b9b5ac")
        ax.text(x + 6, 67, name, fontsize=8.6, fontweight="bold", ha="center")
        ax.text(x + 6, 57, desc, fontsize=6.5, color="#444", ha="center", va="center")
    for x in (17, 37, 57, 77):
        arrow(ax, (x, 61), (x + 8, 61), color=GRAY)
    ax.text(50, 28, "每一步都要有退出条件，而不是“先上线再说”", fontsize=8.0, color=GRAY, ha="center")
    save(fig, "ch01-delivery-stages.png")


if __name__ == "__main__":
    f01_stages()
