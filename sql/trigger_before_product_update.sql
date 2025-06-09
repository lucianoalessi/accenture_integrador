USE sales_accenture;

DELIMITER //

CREATE TRIGGER before_product_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.ModifyDate = NOW();
END //

DELIMITER ;
