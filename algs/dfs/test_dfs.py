import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from dfs import DFS
from google.minimum_paths_sum import Solution


def test_dfs_returns_empty_list_for_empty_tree():
    assert DFS()({}) == []


def test_dfs_returns_single_root_node():
    assert DFS()({"root": {}}) == ["root"]


def test_dfs_visits_tree_in_preorder():
    tree = {
        "root": {
            "alpha": {
                "a1": {},
                "a2": {},
            },
            "beta": {
                "b1": {},
            },
        }
    }

    assert DFS()(tree) == ["root", "alpha", "a1", "a2", "beta", "b1"]


def test_dfs_walks_depth_before_siblings():
    tree = {
        "root": {
            "left": {
                "left.left": {
                    "left.left.left": {},
                },
                "left.right": {},
            },
            "right": {
                "right.left": {},
            },
        }
    }

    assert DFS()(tree) == [
        "root",
        "left",
        "left.left",
        "left.left.left",
        "left.right",
        "right",
        "right.left",
    ]


def test_dfs_supports_multiple_top_level_roots():
    forest = {
        "one": {
            "one.child": {},
        },
        "two": {
            "two.child": {},
        },
    }

    assert DFS()(forest) == ["one", "one.child", "two", "two.child"]


def test_dfs_preserves_insertion_order_among_siblings():
    tree = {
        "root": {
            "third": {},
            "first": {},
            "second": {},
        }
    }

    assert DFS()(tree) == ["root", "third", "first", "second"]


def test_dfs_does_not_mutate_input_tree():
    tree = {
        "root": {
            "alpha": {
                "a1": {},
            },
            "beta": {},
        }
    }
    original = copy.deepcopy(tree)

    DFS()(tree)

    assert tree == original


def test_dfs_can_be_called_more_than_once_without_leaking_state():
    dfs = DFS()

    assert dfs({"a": {"b": {}}}) == ["a", "b"]
    assert dfs({"x": {"y": {}, "z": {}}}) == ["x", "y", "z"]


def test_minimum_path_sum():
    assert Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
