Задание №1

Potas@Laptop-Igor ~
$ ssh 39617a90-437a-48bf-b89c-4d39e57574f0@serverhub.praktikum-services.ru -p 4554
morty@afd1015bca5c:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

scooter_rent=# SELECT c.login, 
               COUNT(o."inDelivery") 
FROM "Couriers" AS c 
INNER JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" = True 
and o.finished = False 
and o.cancelled = False 
GROUP BY c.login;


 login  | count
--------+-------
 James  |     8
 Michae |     2
 Robert |     8
 Thomas |     2
(4 rows)




Задание №2

Найден баг - Не записываются данныые со статусом "-1" в поле "canсelled" БД scooter_rent при отмене заказа. 

Potas@Laptop-Igor ~
$ ssh 8a71d862-260f-4be4-8770-db847c02989f@serverhub.praktikum-services.ru -p 4554
morty@6933cb204526:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

scooter_rent=# SELECT track,
CASE
    WHEN "inDelivery" = True and finished = False and cancelled = False THEN '1'
    WHEN "inDelivery" = True and finished = True and cancelled = False THEN '2'
    WHEN cancelled = True THEN '-1'
    ELSE '0'
    END
FROM "Orders";
 track  | case
--------+------
 602780 | 0
 314218 | 1
 314218 | 1
 928821 | 1
 928821 | 1
 677569 | 0
 258582 | 2
 258582 | 2
(8 rows)