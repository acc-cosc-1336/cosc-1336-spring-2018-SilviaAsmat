from src.final_exam.q_pie.pie_arc import PieArc
from src.final_exam.q_pie.pie_chart import PieChart

pie_arcs = [PieArc('one'),PieArc('two'),PieArc('three'),PieArc('four')]

pie_chart = PieChart(pie_arcs)

pie_chart.draw()
