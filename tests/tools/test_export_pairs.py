from tools.export_pairs import Pair_exporter


def test_init():
    pe = Pair_exporter()
    assert type(pe) is Pair_exporter
    assert type(pe.dir) is str
    assert pe.dir == 'output/random_pairs_1024'

    pe2 = Pair_exporter(location='Winnie the Pooh')
    assert pe2.dir == 'Winnie the Pooh'


def test_gen_fname():
    pe = Pair_exporter(location='output/random_QRs')
    assert pe.gen_fname('stuff') == 'output/random_QRs/stuff.txt'


def test_is_num():
    pe = Pair_exporter()
    assert pe.is_num(14)
    assert pe.is_num(3.14)
    assert pe.is_num('15')
    assert pe.is_num('2.71')
    assert not pe.is_num('mep')
    assert not pe.is_num('3/14')
    assert not pe.is_num(pe)


def test_get_base_name():
    pe = Pair_exporter()
    file_name_1 = 'name.and_date.jpg'
    assert pe.get_base_name(file_name_1) == 'name.and_date'

    file_name_2 = 'name.and_date.jpg'
    assert pe.get_base_name(file_name_2, extension=True) == 'jpg'


def test_store_to_file():
    pass


def test_scan_dir():
    pass


def test_status_scan():
    pass


def test_check_file():
    pass


def test_update_status_file():
    pass


def test_store():
    pass
