# Combat sport game with OOD

### This code is flexible, because of many ood patterns and oop principles!


For instance:

* In [weapon](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/weapon.py) - __decorater pattern__ is used and because of that any fighting style 
(implementaion), with the same interface, can be changed, 
* In [fighting style](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/fighting_style.py) - __strategy pattern__ is used and classes(algorithms), defined here, can be used interchangeably,
* In [factory](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/factory.py) - __factory method and OCP__ is used, for that reason i can add new futures without keeping intension on the logic of conditional statements,
* In [fighter](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/fighter.py) - __observer pattern__ is used. In this case observable (object which want to be observed) is being observed by observer (object which want to observe),
* In [ways to choose](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/ways_to_choose.py) - __iterator pattern__ is used, which come in handy when different DS needed to be iterated over(python have **generator** instead but this helps me to understand oop better),
* In [complexity lvl of oponents](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/complexity_lvl_of_oponents.py) - __bridge pattern__ is used. Human being
don't need to be (is_a) a tractor to dig, he/she just need to have (has_a) a spade,
* In [ways to choose](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/ways_to_choose.py) - __command pattern__ is used partially. Commands is ordered by one object(remote), which can(but in this scenario it isn't) keep track on commands by calling them again, undoing, asking about command history etc..
