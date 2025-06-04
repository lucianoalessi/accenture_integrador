from models.sale import Sale


def test_is_high_value_true():
    venta = Sale(1, 101, 201, 301, 5, 0.0, 1500.0, "2024-01-01", "TX123")
    assert venta.is_high_value() == True

def test_is_high_value_false():
    venta = Sale(2, 101, 201, 301, 0.1, 50.0, "2024-01-01", "TX124")
    assert venta.is_hyigh_value() == False