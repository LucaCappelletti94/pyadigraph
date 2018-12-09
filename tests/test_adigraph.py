from pyadigraph import Adigraph
import networkx as nx
import numpy as np
import random
import filecmp
import os


def test_adigraph():
    seed = 7
    random.seed(seed)
    np.random.seed(seed)

    A = Adigraph(
        vertices_color_fallback="gray!90",
        edges_color_fallback="gray!90",
        sub_caption="My adigraph number {i} of {n}",
        sub_label="adigraph_{i}_{n}",
        caption="A graph generated with python and latex.",
        label="pyadigraph_example"
    )

    A.add_graph(
        nx.bipartite.random_graph(4, 4, 1),
        vertices_color={
            0: 'red!90',
            1: 'red!90',
            4: 'cyan!90',
            7: 'cyan!90'
        }
    )
    A.add_graph(
        nx.bipartite.random_graph(4, 4, 1),
        vertices_color={
            0: 'green!90',
            1: 'green!90',
            4: 'purple!90',
            7: 'purple!90'
        })

    A.save("test/result.tex")
    result = filecmp.cmp('test/expected.tex', 'test/result.tex')
    os.remove("test/result.tex")
    assert result
