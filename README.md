# Combat sport game with OOD

![FVF](http://www.looponline.com.au/wp-content/uploads/2016/09/Mortal-Kombat-X-1.jpg)

### This code is flexible, because of many ood patterns and oop principles!


For instance:

* In [weapon](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/weapon.py) - _decorater pattern_ is used and because of that any fighting style 
(implementaion), with the same interface, can be changed, 
* In [fighting style](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/fighting_style.py) - _strategy pattern_ is used and classes(algorithms), defined here, can be used interchangeably,
* In [factory](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/factory.py) - _factory method and OCP_ is used, for that reason i can add new futures without keeping intension on the logic of conditional statements,
* In [fighter](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/fighter.py) - _observer pattern_ is used. In this case observable (object which want to be observed) is being observed by observer (object which want to observe),
* In [ways to choose](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/ways_to_choose.py) - __iterator pattern__ is used, which come in handy when different DS needed to be iterated over(python have **generator** instead but this helps me to understand oop better),
* In [complexity lvl of oponents](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/complexity_lvl_of_oponents.py) - __bridge pattern__ is used. Human being
don't need to be (is_a) a tractor to dig, he/she just need to have (has_a) a spade,
* In [ways to choose](https://github.com/GasparyanG/Combat-Sport-Game/blob/master/ways_to_choose.py) - _command pattern_ is used partially. Commands is ordered by one object(remote), which can(but in this scenario it isn't) keep track on commands by calling them again, undoing, asking about command history etc..

### Requirements to run program:
* Python 3.x.x
* make sure to be in required (its obviouse that you can't run any code if you not in right directory) path to run appropriate command

## approprate commands
### bash shell:
```
python3.5 starting_point.py
```
### powershell

```
python starting_point.py
```
