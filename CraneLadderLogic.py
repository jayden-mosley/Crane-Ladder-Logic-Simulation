#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:52:24 2025

@author: jaydenAndrew
"""

import tkinter as tk
from tkinter import Canvas

class CraneLadderSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Crane Ladder Logic Simulation")

        # Crane state
        self.crane_x = 150  # Initial X position
        self.crane_y = 50   # Initial Y position (top)
        self.motor_on = False
        self.latch = False  # Latching state
        
        # Create canvas for ladder logic
        self.ladder_canvas = Canvas(self.root, width=400, height=200, bg="white")
        self.ladder_canvas.pack()

        # Create canvas for crane qnimation
        self.crane_canvas = Canvas(self.root, width=400, height=200, bg="lightblue")
        self.crane_canvas.pack()

        # Control Buttons
        self.btn_start = tk.Button(self.root, text="Start", command=self.start_crane)
        self.btn_start.pack(side=tk.LEFT, padx=5, pady=10)

        self.btn_left = tk.Button(self.root, text="Move Left (Lower)", command=self.move_left)
        self.btn_left.pack(side=tk.LEFT, padx=5, pady=10)

        self.btn_up = tk.Button(self.root, text="Move Up", command=self.move_up)
        self.btn_up.pack(side=tk.LEFT, padx=5, pady=10)

        self.btn_stop = tk.Button(self.root, text="Emergency Stop", command=self.stop_crane)
        self.btn_stop.pack(side=tk.LEFT, padx=5, pady=10)

        # Draw initial state
        self.update_ladder()
        self.update_crane()

    def update_ladder(self):
        self.ladder_canvas.delete("all")

        # Draw ladder rails
        self.ladder_canvas.create_line(50, 20, 50, 180, width=5)
        self.ladder_canvas.create_line(350, 20, 350, 180, width=5)

        # Start button (normally open)
        start_color = "green" if self.motor_on else "white"
        self.ladder_canvas.create_rectangle(100, 30, 180, 70, outline="black", fill=start_color)
        self.ladder_canvas.create_text(140, 50, text="START", font=("Arial", 10))

        # Move left (lower crane)
        left_color = "green" if self.crane_x < 150 else "white"
        self.ladder_canvas.create_rectangle(100, 80, 180, 120, outline="black", fill=left_color)
        self.ladder_canvas.create_text(140, 100, text="MOVE LEFT", font=("Arial", 10))

        # Move up
        up_color = "green" if self.crane_y < 50 else "white"
        self.ladder_canvas.create_rectangle(100, 130, 180, 170, outline="black", fill=up_color)
        self.ladder_canvas.create_text(140, 150, text="MOVE UP", font=("Arial", 10))

        # Emergency Stop (normally closed)
        stop_color = "red" if not self.motor_on else "white"
        self.ladder_canvas.create_rectangle(250, 30, 330, 70, outline="black", fill=stop_color)
        self.ladder_canvas.create_text(290, 50, text="STOP", font=("Arial", 10))

        # Draw wiring
        self.ladder_canvas.create_line(50, 50, 100, 50, width=2)  # Start button wire
        self.ladder_canvas.create_line(180, 50, 250, 50, width=2)  # Start to Stop
        self.ladder_canvas.create_line(330, 50, 350, 50, width=2)  # Stop to rail
        self.ladder_canvas.create_line(50, 100, 100, 100, width=2)  # Move Left wire
        self.ladder_canvas.create_line(180, 100, 350, 100, width=2)  # Move Left to rail
        self.ladder_canvas.create_line(50, 150, 100, 150, width=2)  # Move Up wire
        self.ladder_canvas.create_line(180, 150, 350, 150, width=2)  # Move Up to rail

    def update_crane(self):
        self.crane_canvas.delete("all")

        # Crane structure
        self.crane_canvas.create_rectangle(50, 40, 350, 60, fill="gray")  # Overhead Beam
        self.crane_canvas.create_line(self.crane_x, 60, self.crane_x, self.crane_y, width=2)  # Cable

        # Crane hook
        self.crane_canvas.create_oval(self.crane_x-10, self.crane_y, self.crane_x+10, self.crane_y+20, fill="black")

        # Object (if lowered)
        if self.crane_y > 150:
            self.crane_canvas.create_rectangle(self.crane_x-15, self.crane_y+20, self.crane_x+15, self.crane_y+40, fill="brown")

    def start_crane(self):
        self.motor_on = True
        self.latch = True  # Enable latch
        self.update_ladder()

    def stop_crane(self):
        self.motor_on = False
        self.latch = False  # Disable latch
        self.update_ladder()

    def move_left(self):
        if self.motor_on and self.crane_x > 100:
            self.crane_x -= 50
            self.crane_y = 170  # Simulate crane lowering
            self.update_ladder()
            self.update_crane()

    def move_up(self):
        if self.motor_on and self.crane_y > 50:
            self.crane_y = 50  # Bring crane back up
            self.update_ladder()
            self.update_crane()

# Run the simulator
if __name__ == "__main__":
    root = tk.Tk()
    app = CraneLadderSimulator(root)
    root.mainloop()
