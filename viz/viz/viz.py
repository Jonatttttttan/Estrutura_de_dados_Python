import graphviz
from networkx.algorithms.structuralholes import constraint

from EstruturaDeDados.test_tree import example_tree

dot = graphviz.Digraph(comment="The Round Table")

dot.node("A", "King Arthur")
dot.node("B", "Sir Bedevere the Wise")
dot.node("L", "Sir Lancelot the Brave")

dot.edges(["AB", "AL"])
dot.edge("B", "L", constraint='false')

#dot.render('viz/round-table.gv', view=True) # Gera descrição para usar no graphviz online



