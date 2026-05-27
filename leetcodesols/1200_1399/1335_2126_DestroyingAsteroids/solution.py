class Solution:

    #Apparently this is optimal....
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        current_mass=mass
        asteroids.sort()
        for asteroid in asteroids: 
            if current_mass>=asteroid:
                current_mass+=asteroid
            else:
                return False
        return True
