from manim import *

class DotCircleLineAnimation(Scene):
    def construct(self):
        # Initial dot at origin
        dot = Dot()
        
        # Initial line adjacent to the dot at distance 0.5 * dot diameter
        # Dot diameter is 2 * dot.radius, so distance = 0.5 * 2 * dot.radius = dot.radius
        distance = dot.radius
        line = Line(start=RIGHT * distance, end=RIGHT * (distance + 1))
        
        self.add(dot, line)
        self.wait(0.5)
        
        # Circle emerges from the dot, enlarging to radius 1 (2 cm approx)
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle))
        self.wait(0.5)
        
        # Dot moves to boundary of circle (to the right side)
        boundary_point = circle.point_at_angle(0)  # angle 0 radians is to the right
        self.play(dot.animate.move_to(boundary_point))
        self.wait(0.5)
        
        # Dot moves around the boundary to the point adjacent to the line
        # The line is at x = distance = dot.radius, so the dot should move on circle boundary to angle where x = distance
        # On circle boundary: x = radius * cos(theta)
        # Solve radius * cos(theta) = distance => cos(theta) = distance / radius
        # radius = 1, distance = dot.radius (~0.05), so theta = arccos(distance)
        import numpy as np
        theta = np.arccos(distance)
        target_point = circle.point_at_angle(theta)
        self.play(MoveAlongPath(dot, Arc(radius=1, start_angle=0, angle=theta)))
        self.wait(0.5)
        
        # Dot moves to the line (line start point)
        self.play(dot.animate.move_to(line.get_start()))
        self.wait(1)