from lie_algebra import cartan_matrix, root_system, weyl_group_order


def test_e8_invariants():
    roots = root_system("E8")
    assert len(roots) == 240
    assert cartan_matrix("E8").shape == (8, 8)
    assert weyl_group_order("E8") == 696729600
