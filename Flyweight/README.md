# Flyweight

•	Improves memory usage and speed by enabling (not enforcing) the sharing of objects’ (1, 2, 3) intrinsic state (color) and changing only its extrinsic state (x, y, radius) instead of creating new one. If a black circle is already created, send it and let the user change its extrinsic state.
1.	Flyweight Factory: Shape_Factory
2.	Flyweight: Shape
3.	Concrete Flyweight: Circle
4.	Unshared Concrete Flyweight: optional
