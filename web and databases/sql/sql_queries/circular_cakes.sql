SELECT Product.ProductCode, Name, Location, Price, ServingSize FROM Product 
INNER JOIN Cake on Product.ProductCode = Cake.ProductCode
WHERE Shape = 'Circle'