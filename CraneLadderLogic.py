#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:52:24 2025

@author: jaydenAndrew
"""

import tkinter as tk
from tkinter import Canvas

class CraneSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Crane Ladder Logic Simulation")

        # Crane state
        self.crane_x = 50  # Starting X position
        self.crane_y = 80  # Starting Y position (height)
        self.object_picked = False  # Object pick-up state
        self.running = False  # If system is started
        self.emergency = False  # Emergency stop state

        # Create canvas
        self.canvas = Canvas(self.root, width=500, height=400, bg="white")
        self.canvas.pack()

        # Control buttons
        self.btn_start = tk.Button(self.root, text="Start", command=self.start_system)
        self.btn_start.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_left = tk.Button(self.root, text="Move Left", command=self.move_left)
        self.btn_left.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_up = tk.Button(self.root, text="Move Up", command=self.move_up)
        self.btn_up.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_emergency = tk.Button(self.root, text="Emergency Stop", command=self.emergency_stop, bg="red")
        self.btn_emergency.pack(side=tk.RIGHT, padx=10, pady=10)

        self.update_ladder()

    def update_ladder(self):
        self.canvas.delete("all")

        # Ladder rails
        self.canvas.create_line(50, 50, 50, 350, width=5)
        self.canvas.create_line(450, 50, 450, 350, width=5)

        # Buttons
        self.draw_ladder_button(100, 60, "START", "green" if self.running else "white")
        self.draw_ladder_button(100, 120, "MOVE LEFT", "green" if self.crane_x > 50 else "white")
        self.draw_ladder_button(100, 180, "MOVE UP", "green" if self.object_picked else "white")
        self.draw_ladder_button(100, 240, "EMERGENCY", "red" if self.emergency else "white")

        # Crane visual
        self.canvas.create_rectangle(self.crane_x, self.crane_y, self.crane_x + 40, self.crane_y + 40, fill="blue")
        self.canvas.create_text(self.crane_x + 20, self.crane_y + 20, text="Crane", font=("Arial", 10), fill="white")

        # Object (if picked)
        if self.object_picked:
            self.canvas.create_rectangle(self.crane_x + 5, self.crane_y + 45, self.crane_x + 35, self.crane_y + 65, fill="brown")
            self.canvas.create_text(self.crane_x + 20, self.crane_y + 55, text="Box", font=("Arial", 10), fill="white")

    def draw_ladder_button(self, x, y, label, color):
        self.canvas.create_rectangle(x, y, x + 80, y + 40, outline="black", fill=color)
        self.canvas.create_text(x + 40, y + 20, text=label, font=("Arial", 10))

    def start_system(self):
        # Starts the system, allowing movement
        self.running = True
        self.emergency = False
        self.update_ladder()

    def move_left(self):
        # Moves the crane left and lowers it (simulating pick-up)
        if self.running and not self.emergency and self.crane_x < 200:
            self.animate_movement("left", 200, 150)
            self.object_picked = True
            self.update_ladder()

    def move_up(self):
        if self.running and not self.emergency and self.object_picked:
            self.animate_movement("up", 50, 80)
            self.object_picked = False  # Drops object at original position
            self.update_ladder()

    def emergency_stop(self):
       # Stops all operations immediately
        self.running = False
        self.emergency = True
        self.update_ladder()

    def animate_movement(self, direction, target_x, target_y):
        # Smooth animation for crane movement
        step_x = 2 if self.crane_x < target_x else -2
        step_y = 2 if self.crane_y < target_y else -2

        while self.crane_x != target_x or self.crane_y != target_y:
            if self.crane_x != target_x:
                self.crane_x += step_x
            if self.crane_y != target_y:
                self.crane_y += step_y
            self.update_ladder()
            self.root.update_idletasks()
            self.root.after(10)  # Controls animation speed

# Run the simulator
if __name__ == "__main__":
    root = tk.Tk()
    app = CraneSimulator(root)
    root.mainloop()
