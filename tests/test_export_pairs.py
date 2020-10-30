from export_pairs import Pair_exporter


def test_init():
    pe = Pair_exporter()
    assert type(pe) is Pair_exporter
    assert type(pe.dir) is str
    assert pe.dir == '/output'

    pe2 = Pair_exporter(location='Winnie the Pooh')
    assert pe2.dir == 'Winnie the Pooh'
