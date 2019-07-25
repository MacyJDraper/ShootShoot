from enemy import Enemy

class Fleet():
    def __init__(self, row_count, column_count, initial_speed, enemy_img, starting_xcor, starting_ycor ):
        self.direction = 1
        self.speed = initial_speed
        self.ships = self.get_initial_ships(row_count, column_count, enemy_img, starting_xcor,starting_ycor)
    
    def get_initial_ships(self, row_count, column_count, enemy_img, starting_xcor, starting_ycor):
        initial_ships = []
        for row in range(0, row_count):
            for col in range(0, column_count):
                current_xcor = starting_xcor + col * enemy_img.get_height()
                current_ycor = starting_ycor + row * enemy_img.get_height()
                initial_ships.append(Enemy(enemy_img, current_xcor, current_ycor))
        return initial_ships
    
    def move_over(self, left_wall, right_wall):
        for ship in self.ships:
            if ship.has_collided_with_left_wall(left_wall) or ship.has_collided_with_right_wall(right_wall):
                ship.move_down()
                self.change_direction()
                break
        for ship in self.ships:
            ship.xcor += ship.direction * self.speed

    def move_down(self):
        for ship in self.ships:
            ship.move_down(10)
   
    def change_direction(self):
        for ship in self.ships:
            ship.direction *= -1
    